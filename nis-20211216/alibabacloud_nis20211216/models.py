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
        # 
        # This parameter is required.
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
        # 
        # This parameter is required.
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
        # The key of tag N to add to the resource. The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        # 
        # You can add up to 20 tags in each call.
        self.key = key
        # The value of tag N to add to the resource. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag value cannot start with `aliyun` or `acs:`.
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
        resource_group_id: str = None,
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
        # 
        # This parameter is required.
        self.network_path_name = network_path_name
        # The protocol type. Valid values:
        # 
        # *   **tcp**: Transmission Control Protocol (TCP)
        # *   **udp**: User Datagram Protocol (UDP)
        # *   **icmp**: Internet Control Message Protocol (ICMP)
        self.protocol = protocol
        # The region ID of the network path that you want to create.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The ID of the source resource.
        # 
        # This parameter is required.
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
        # 
        # This parameter is required.
        self.source_type = source_type
        # The tags to add to the resource.
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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
        # The key of the tag to add to the resource. The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        # 
        # You can add up to 20 tags in each call.
        self.key = key
        # The value of the tag to add to the resource. The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag value cannot start with `acs:` or `aliyun`. The tag value can be an empty string.
        # 
        # You can add up to 20 tag values in each call.
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
        # The ID of the network path. You can call the [CreateNetworkPath](https://help.aliyun.com/document_detail/2366522.html) operation to obtain the ID of the network path.
        # 
        # This parameter is required.
        self.network_path_id = network_path_id
        # The ID of the region for which you want to create a task for analyzing network reachability.
        self.region_id = region_id
        # The tags to add to the resource.
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
        # 
        # This parameter is required.
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
        # 
        # This parameter is required.
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
        data: bool = None,
        request_id: str = None,
    ):
        # Result of operation.
        # 
        # - **true**: Delete Success.
        # - **false**: Delete Fail.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
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
        # 
        # This parameter is required.
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
        # 
        # This parameter is required.
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
        data: bool = None,
        request_id: str = None,
    ):
        # Result of operation.
        # - **true**: Delete Success.
        # - **false**: Delete Fail.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
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


class DeleteNisInspectionReportRequest(TeaModel):
    def __init__(
        self,
        inspection_report_id: str = None,
    ):
        # This parameter is required.
        self.inspection_report_id = inspection_report_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inspection_report_id is not None:
            result['InspectionReportId'] = self.inspection_report_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InspectionReportId') is not None:
            self.inspection_report_id = m.get('InspectionReportId')
        return self


class DeleteNisInspectionReportResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteNisInspectionReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteNisInspectionReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteNisInspectionReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNisInspectionTaskRequest(TeaModel):
    def __init__(
        self,
        inspection_task_id: str = None,
    ):
        # This parameter is required.
        self.inspection_task_id = inspection_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inspection_task_id is not None:
            result['InspectionTaskId'] = self.inspection_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InspectionTaskId') is not None:
            self.inspection_task_id = m.get('InspectionTaskId')
        return self


class DeleteNisInspectionTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteNisInspectionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteNisInspectionTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteNisInspectionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNisInspectionRecommendationResourcesRequest(TeaModel):
    def __init__(
        self,
        inspection_report_id: str = None,
        language: str = None,
        max_results: int = None,
        next_token: str = None,
        recommendation_code: str = None,
    ):
        # This parameter is required.
        self.inspection_report_id = inspection_report_id
        self.language = language
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.recommendation_code = recommendation_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inspection_report_id is not None:
            result['InspectionReportId'] = self.inspection_report_id
        if self.language is not None:
            result['Language'] = self.language
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.recommendation_code is not None:
            result['RecommendationCode'] = self.recommendation_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InspectionReportId') is not None:
            self.inspection_report_id = m.get('InspectionReportId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RecommendationCode') is not None:
            self.recommendation_code = m.get('RecommendationCode')
        return self


class DescribeNisInspectionRecommendationResourcesResponseBodyResourceList(TeaModel):
    def __init__(
        self,
        analysis_data: str = None,
        resource_id: str = None,
        resource_name: str = None,
    ):
        self.analysis_data = analysis_data
        self.resource_id = resource_id
        self.resource_name = resource_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_data is not None:
            result['AnalysisData'] = self.analysis_data
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalysisData') is not None:
            self.analysis_data = m.get('AnalysisData')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        return self


class DescribeNisInspectionRecommendationResourcesResponseBody(TeaModel):
    def __init__(
        self,
        inspection_report_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resource_list: List[DescribeNisInspectionRecommendationResourcesResponseBodyResourceList] = None,
        total_count: int = None,
    ):
        self.inspection_report_id = inspection_report_id
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.resource_list = resource_list
        self.total_count = total_count

    def validate(self):
        if self.resource_list:
            for k in self.resource_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inspection_report_id is not None:
            result['InspectionReportId'] = self.inspection_report_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceList'] = []
        if self.resource_list is not None:
            for k in self.resource_list:
                result['ResourceList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InspectionReportId') is not None:
            self.inspection_report_id = m.get('InspectionReportId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k in m.get('ResourceList'):
                temp_model = DescribeNisInspectionRecommendationResourcesResponseBodyResourceList()
                self.resource_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeNisInspectionRecommendationResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNisInspectionRecommendationResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeNisInspectionRecommendationResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNisInspectionReportCheckItemsRequest(TeaModel):
    def __init__(
        self,
        category_code: str = None,
        inspection_report_id: str = None,
        language: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_type: List[str] = None,
        risk_level: List[str] = None,
    ):
        self.category_code = category_code
        # This parameter is required.
        self.inspection_report_id = inspection_report_id
        self.language = language
        self.max_results = max_results
        self.next_token = next_token
        self.resource_type = resource_type
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_code is not None:
            result['CategoryCode'] = self.category_code
        if self.inspection_report_id is not None:
            result['InspectionReportId'] = self.inspection_report_id
        if self.language is not None:
            result['Language'] = self.language
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryCode') is not None:
            self.category_code = m.get('CategoryCode')
        if m.get('InspectionReportId') is not None:
            self.inspection_report_id = m.get('InspectionReportId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class DescribeNisInspectionReportCheckItemsShrinkRequest(TeaModel):
    def __init__(
        self,
        category_code: str = None,
        inspection_report_id: str = None,
        language: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_type_shrink: str = None,
        risk_level_shrink: str = None,
    ):
        self.category_code = category_code
        # This parameter is required.
        self.inspection_report_id = inspection_report_id
        self.language = language
        self.max_results = max_results
        self.next_token = next_token
        self.resource_type_shrink = resource_type_shrink
        self.risk_level_shrink = risk_level_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_code is not None:
            result['CategoryCode'] = self.category_code
        if self.inspection_report_id is not None:
            result['InspectionReportId'] = self.inspection_report_id
        if self.language is not None:
            result['Language'] = self.language
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_type_shrink is not None:
            result['ResourceType'] = self.resource_type_shrink
        if self.risk_level_shrink is not None:
            result['RiskLevel'] = self.risk_level_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryCode') is not None:
            self.category_code = m.get('CategoryCode')
        if m.get('InspectionReportId') is not None:
            self.inspection_report_id = m.get('InspectionReportId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceType') is not None:
            self.resource_type_shrink = m.get('ResourceType')
        if m.get('RiskLevel') is not None:
            self.risk_level_shrink = m.get('RiskLevel')
        return self


class DescribeNisInspectionReportCheckItemsResponseBodyCheckItemListCheckResultList(TeaModel):
    def __init__(
        self,
        count: int = None,
        risk_level: str = None,
    ):
        self.count = count
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class DescribeNisInspectionReportCheckItemsResponseBodyCheckItemListRecommendationList(TeaModel):
    def __init__(
        self,
        abnormality: str = None,
        metadata: str = None,
        reason: str = None,
        recommendation_code: str = None,
        risk_level: str = None,
        suggestion: str = None,
    ):
        self.abnormality = abnormality
        self.metadata = metadata
        self.reason = reason
        self.recommendation_code = recommendation_code
        self.risk_level = risk_level
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abnormality is not None:
            result['Abnormality'] = self.abnormality
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.recommendation_code is not None:
            result['RecommendationCode'] = self.recommendation_code
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Abnormality') is not None:
            self.abnormality = m.get('Abnormality')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RecommendationCode') is not None:
            self.recommendation_code = m.get('RecommendationCode')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class DescribeNisInspectionReportCheckItemsResponseBodyCheckItemList(TeaModel):
    def __init__(
        self,
        category_code: str = None,
        check_item_code: str = None,
        check_item_name: str = None,
        check_result_list: List[DescribeNisInspectionReportCheckItemsResponseBodyCheckItemListCheckResultList] = None,
        description: str = None,
        recommendation_list: List[DescribeNisInspectionReportCheckItemsResponseBodyCheckItemListRecommendationList] = None,
        resource_type: str = None,
    ):
        self.category_code = category_code
        self.check_item_code = check_item_code
        self.check_item_name = check_item_name
        self.check_result_list = check_result_list
        self.description = description
        self.recommendation_list = recommendation_list
        self.resource_type = resource_type

    def validate(self):
        if self.check_result_list:
            for k in self.check_result_list:
                if k:
                    k.validate()
        if self.recommendation_list:
            for k in self.recommendation_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_code is not None:
            result['CategoryCode'] = self.category_code
        if self.check_item_code is not None:
            result['CheckItemCode'] = self.check_item_code
        if self.check_item_name is not None:
            result['CheckItemName'] = self.check_item_name
        result['CheckResultList'] = []
        if self.check_result_list is not None:
            for k in self.check_result_list:
                result['CheckResultList'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        result['RecommendationList'] = []
        if self.recommendation_list is not None:
            for k in self.recommendation_list:
                result['RecommendationList'].append(k.to_map() if k else None)
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryCode') is not None:
            self.category_code = m.get('CategoryCode')
        if m.get('CheckItemCode') is not None:
            self.check_item_code = m.get('CheckItemCode')
        if m.get('CheckItemName') is not None:
            self.check_item_name = m.get('CheckItemName')
        self.check_result_list = []
        if m.get('CheckResultList') is not None:
            for k in m.get('CheckResultList'):
                temp_model = DescribeNisInspectionReportCheckItemsResponseBodyCheckItemListCheckResultList()
                self.check_result_list.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.recommendation_list = []
        if m.get('RecommendationList') is not None:
            for k in m.get('RecommendationList'):
                temp_model = DescribeNisInspectionReportCheckItemsResponseBodyCheckItemListRecommendationList()
                self.recommendation_list.append(temp_model.from_map(k))
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeNisInspectionReportCheckItemsResponseBody(TeaModel):
    def __init__(
        self,
        check_item_list: List[DescribeNisInspectionReportCheckItemsResponseBodyCheckItemList] = None,
        inspection_report_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.check_item_list = check_item_list
        self.inspection_report_id = inspection_report_id
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.check_item_list:
            for k in self.check_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CheckItemList'] = []
        if self.check_item_list is not None:
            for k in self.check_item_list:
                result['CheckItemList'].append(k.to_map() if k else None)
        if self.inspection_report_id is not None:
            result['InspectionReportId'] = self.inspection_report_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_item_list = []
        if m.get('CheckItemList') is not None:
            for k in m.get('CheckItemList'):
                temp_model = DescribeNisInspectionReportCheckItemsResponseBodyCheckItemList()
                self.check_item_list.append(temp_model.from_map(k))
        if m.get('InspectionReportId') is not None:
            self.inspection_report_id = m.get('InspectionReportId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeNisInspectionReportCheckItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNisInspectionReportCheckItemsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeNisInspectionReportCheckItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNisInspectionReportStatusRequest(TeaModel):
    def __init__(
        self,
        inspection_report_id: str = None,
    ):
        # This parameter is required.
        self.inspection_report_id = inspection_report_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inspection_report_id is not None:
            result['InspectionReportId'] = self.inspection_report_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InspectionReportId') is not None:
            self.inspection_report_id = m.get('InspectionReportId')
        return self


class DescribeNisInspectionReportStatusResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        inspection_project: str = None,
        inspection_report_id: str = None,
        inspection_task_id: str = None,
        inspection_task_name: str = None,
        request_id: str = None,
        start_time: str = None,
        status: str = None,
    ):
        self.end_time = end_time
        self.inspection_project = inspection_project
        self.inspection_report_id = inspection_report_id
        self.inspection_task_id = inspection_task_id
        self.inspection_task_name = inspection_task_name
        self.request_id = request_id
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.inspection_project is not None:
            result['InspectionProject'] = self.inspection_project
        if self.inspection_report_id is not None:
            result['InspectionReportId'] = self.inspection_report_id
        if self.inspection_task_id is not None:
            result['InspectionTaskId'] = self.inspection_task_id
        if self.inspection_task_name is not None:
            result['InspectionTaskName'] = self.inspection_task_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InspectionProject') is not None:
            self.inspection_project = m.get('InspectionProject')
        if m.get('InspectionReportId') is not None:
            self.inspection_report_id = m.get('InspectionReportId')
        if m.get('InspectionTaskId') is not None:
            self.inspection_task_id = m.get('InspectionTaskId')
        if m.get('InspectionTaskName') is not None:
            self.inspection_task_name = m.get('InspectionTaskName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeNisInspectionReportStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNisInspectionReportStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeNisInspectionReportStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNisInspectionReportSummaryRequest(TeaModel):
    def __init__(
        self,
        inspection_report_id: str = None,
    ):
        # This parameter is required.
        self.inspection_report_id = inspection_report_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inspection_report_id is not None:
            result['InspectionReportId'] = self.inspection_report_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InspectionReportId') is not None:
            self.inspection_report_id = m.get('InspectionReportId')
        return self


class DescribeNisInspectionReportSummaryResponseBodySummaryPassRateSummary(TeaModel):
    def __init__(
        self,
        pass_rate: float = None,
        pass_rate_scope: str = None,
    ):
        self.pass_rate = pass_rate
        self.pass_rate_scope = pass_rate_scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pass_rate is not None:
            result['PassRate'] = self.pass_rate
        if self.pass_rate_scope is not None:
            result['PassRateScope'] = self.pass_rate_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PassRate') is not None:
            self.pass_rate = m.get('PassRate')
        if m.get('PassRateScope') is not None:
            self.pass_rate_scope = m.get('PassRateScope')
        return self


class DescribeNisInspectionReportSummaryResponseBodySummaryRiskSummary(TeaModel):
    def __init__(
        self,
        resource_count: int = None,
        risk_count: int = None,
        risk_level: str = None,
        risk_type: str = None,
    ):
        self.resource_count = resource_count
        self.risk_count = risk_count
        self.risk_level = risk_level
        self.risk_type = risk_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.risk_type is not None:
            result['RiskType'] = self.risk_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('RiskType') is not None:
            self.risk_type = m.get('RiskType')
        return self


class DescribeNisInspectionReportSummaryResponseBodySummary(TeaModel):
    def __init__(
        self,
        check_item_count: int = None,
        check_resource_count: int = None,
        pass_rate_summary: List[DescribeNisInspectionReportSummaryResponseBodySummaryPassRateSummary] = None,
        risk_summary: List[DescribeNisInspectionReportSummaryResponseBodySummaryRiskSummary] = None,
    ):
        self.check_item_count = check_item_count
        self.check_resource_count = check_resource_count
        self.pass_rate_summary = pass_rate_summary
        self.risk_summary = risk_summary

    def validate(self):
        if self.pass_rate_summary:
            for k in self.pass_rate_summary:
                if k:
                    k.validate()
        if self.risk_summary:
            for k in self.risk_summary:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_item_count is not None:
            result['CheckItemCount'] = self.check_item_count
        if self.check_resource_count is not None:
            result['CheckResourceCount'] = self.check_resource_count
        result['PassRateSummary'] = []
        if self.pass_rate_summary is not None:
            for k in self.pass_rate_summary:
                result['PassRateSummary'].append(k.to_map() if k else None)
        result['RiskSummary'] = []
        if self.risk_summary is not None:
            for k in self.risk_summary:
                result['RiskSummary'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckItemCount') is not None:
            self.check_item_count = m.get('CheckItemCount')
        if m.get('CheckResourceCount') is not None:
            self.check_resource_count = m.get('CheckResourceCount')
        self.pass_rate_summary = []
        if m.get('PassRateSummary') is not None:
            for k in m.get('PassRateSummary'):
                temp_model = DescribeNisInspectionReportSummaryResponseBodySummaryPassRateSummary()
                self.pass_rate_summary.append(temp_model.from_map(k))
        self.risk_summary = []
        if m.get('RiskSummary') is not None:
            for k in m.get('RiskSummary'):
                temp_model = DescribeNisInspectionReportSummaryResponseBodySummaryRiskSummary()
                self.risk_summary.append(temp_model.from_map(k))
        return self


class DescribeNisInspectionReportSummaryResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        inspection_report_id: str = None,
        inspection_task_id: str = None,
        request_id: str = None,
        start_time: str = None,
        status: str = None,
        summary: DescribeNisInspectionReportSummaryResponseBodySummary = None,
    ):
        self.end_time = end_time
        self.inspection_report_id = inspection_report_id
        self.inspection_task_id = inspection_task_id
        self.request_id = request_id
        self.start_time = start_time
        self.status = status
        self.summary = summary

    def validate(self):
        if self.summary:
            self.summary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.inspection_report_id is not None:
            result['InspectionReportId'] = self.inspection_report_id
        if self.inspection_task_id is not None:
            result['InspectionTaskId'] = self.inspection_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.summary is not None:
            result['Summary'] = self.summary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InspectionReportId') is not None:
            self.inspection_report_id = m.get('InspectionReportId')
        if m.get('InspectionTaskId') is not None:
            self.inspection_task_id = m.get('InspectionTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Summary') is not None:
            temp_model = DescribeNisInspectionReportSummaryResponseBodySummary()
            self.summary = temp_model.from_map(m['Summary'])
        return self


class DescribeNisInspectionReportSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNisInspectionReportSummaryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeNisInspectionReportSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNisInspectionTaskRequest(TeaModel):
    def __init__(
        self,
        inspection_task_id: str = None,
    ):
        # This parameter is required.
        self.inspection_task_id = inspection_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inspection_task_id is not None:
            result['InspectionTaskId'] = self.inspection_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InspectionTaskId') is not None:
            self.inspection_task_id = m.get('InspectionTaskId')
        return self


class DescribeNisInspectionTaskResponseBodyCheckResourceList(TeaModel):
    def __init__(
        self,
        check_scope: str = None,
        resource_type: str = None,
    ):
        self.check_scope = check_scope
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_scope is not None:
            result['CheckScope'] = self.check_scope
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckScope') is not None:
            self.check_scope = m.get('CheckScope')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeNisInspectionTaskResponseBody(TeaModel):
    def __init__(
        self,
        check_resource_list: List[DescribeNisInspectionTaskResponseBodyCheckResourceList] = None,
        create_time: str = None,
        inspection_interval: str = None,
        inspection_name: str = None,
        inspection_project: str = None,
        inspection_task_id: str = None,
        inspection_trigger_time: str = None,
        last_update_report_id: str = None,
        last_update_time: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.check_resource_list = check_resource_list
        self.create_time = create_time
        self.inspection_interval = inspection_interval
        self.inspection_name = inspection_name
        self.inspection_project = inspection_project
        self.inspection_task_id = inspection_task_id
        self.inspection_trigger_time = inspection_trigger_time
        self.last_update_report_id = last_update_report_id
        self.last_update_time = last_update_time
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.check_resource_list:
            for k in self.check_resource_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CheckResourceList'] = []
        if self.check_resource_list is not None:
            for k in self.check_resource_list:
                result['CheckResourceList'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.inspection_interval is not None:
            result['InspectionInterval'] = self.inspection_interval
        if self.inspection_name is not None:
            result['InspectionName'] = self.inspection_name
        if self.inspection_project is not None:
            result['InspectionProject'] = self.inspection_project
        if self.inspection_task_id is not None:
            result['InspectionTaskId'] = self.inspection_task_id
        if self.inspection_trigger_time is not None:
            result['InspectionTriggerTime'] = self.inspection_trigger_time
        if self.last_update_report_id is not None:
            result['LastUpdateReportId'] = self.last_update_report_id
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_resource_list = []
        if m.get('CheckResourceList') is not None:
            for k in m.get('CheckResourceList'):
                temp_model = DescribeNisInspectionTaskResponseBodyCheckResourceList()
                self.check_resource_list.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InspectionInterval') is not None:
            self.inspection_interval = m.get('InspectionInterval')
        if m.get('InspectionName') is not None:
            self.inspection_name = m.get('InspectionName')
        if m.get('InspectionProject') is not None:
            self.inspection_project = m.get('InspectionProject')
        if m.get('InspectionTaskId') is not None:
            self.inspection_task_id = m.get('InspectionTaskId')
        if m.get('InspectionTriggerTime') is not None:
            self.inspection_trigger_time = m.get('InspectionTriggerTime')
        if m.get('LastUpdateReportId') is not None:
            self.last_update_report_id = m.get('LastUpdateReportId')
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeNisInspectionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNisInspectionTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeNisInspectionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInternetTupleRequest(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        begin_time: int = None,
        cloud_ip: str = None,
        cloud_ip_list: List[str] = None,
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
        # The IDs of member accounts.
        self.account_ids = account_ids
        # The beginning of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The local IP address.
        self.cloud_ip = cloud_ip
        # The local IP addresses for filtering.
        self.cloud_ip_list = cloud_ip_list
        # The local Internet service provider (ISP).
        # 
        # >  In most cases, the value is Alibaba or Alibaba Cloud.
        self.cloud_isp = cloud_isp
        # The local port.
        # 
        # >  This parameter is required only if you set GroupBy to CloudPort.
        self.cloud_port = cloud_port
        # The direction of the Internet traffic that you want to query. Valid values:
        # 
        # *   **in**: inbound
        # *   **out**: outbound
        # 
        # This parameter is required.
        self.direction = direction
        # The end of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the Alibaba Cloud instance.
        self.instance_id = instance_id
        # The instance IDs for filtering.
        self.instance_list = instance_list
        # The metric for data ranking. Default value: **ByteCount**. This value indicates that Internet traffic data is ranked by traffic volume.
        # 
        # Valid values:
        # 
        # *   Rtt
        # *   ByteCount
        # *   PacketCount
        # *   RetransmitRate
        self.order_by = order_by
        # The remote city.
        # 
        # >  This parameter is required only if you set **TupleType** to **2** or **5**.
        self.other_city = other_city
        # The remote country.
        # 
        # >  This parameter is required only if you set **TupleType** to **2** or **5**.
        self.other_country = other_country
        # The remote IP address.
        # 
        # > This parameter is required only when you set **TupleType** to **2** or **5**.
        self.other_ip = other_ip
        # The remote ISP.
        # 
        # > This parameter is required if you want to view the information about the remote ISP.
        self.other_isp = other_isp
        # The remote port.
        # 
        # > This parameter is required only when you set **TupleType** to **5**.
        self.other_port = other_port
        # The protocol number.
        # 
        # > All protocols are supported. This parameter is required only when you set **TupleType** to **5**.
        self.protocol = protocol
        # The ID of the region for which you want to query the Internet traffic.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The order in which instances are ranked by Internet traffic. Valid values:
        # 
        # *   **desc**: the descending order
        # *   **asc**: the ascending order
        self.sort = sort
        # Specifies top-N traffic data to display. Default value: **10**. This value specifies to display top-10 traffic data by default. Max value: **100**.
        self.top_n = top_n
        # The type of the tuple. Valid values:
        # 
        # *   **1**: 1-tuple
        # *   **2**: 2-tuple
        # *   **5**: 5-tuple
        # 
        # This parameter is required.
        self.tuple_type = tuple_type
        # Specifies whether to enable the multi-account management feature. Default value: **false**. This value specifies that the multi-account management feature is disabled.
        # 
        # >  By default, the multi-account management feature is not available. If you want to use this feature, contact your account manager to apply for permissions.
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
        if self.cloud_ip_list is not None:
            result['CloudIpList'] = self.cloud_ip_list
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
        if m.get('CloudIpList') is not None:
            self.cloud_ip_list = m.get('CloudIpList')
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
        account_ids: List[int] = None,
        begin_time: int = None,
        cloud_ip: str = None,
        cloud_ip_list_shrink: str = None,
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
        # The IDs of member accounts.
        self.account_ids = account_ids
        # The beginning of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The local IP address.
        self.cloud_ip = cloud_ip
        # The local IP addresses for filtering.
        self.cloud_ip_list_shrink = cloud_ip_list_shrink
        # The local Internet service provider (ISP).
        # 
        # >  In most cases, the value is Alibaba or Alibaba Cloud.
        self.cloud_isp = cloud_isp
        # The local port.
        # 
        # >  This parameter is required only if you set GroupBy to CloudPort.
        self.cloud_port = cloud_port
        # The direction of the Internet traffic that you want to query. Valid values:
        # 
        # *   **in**: inbound
        # *   **out**: outbound
        # 
        # This parameter is required.
        self.direction = direction
        # The end of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the Alibaba Cloud instance.
        self.instance_id = instance_id
        # The instance IDs for filtering.
        self.instance_list_shrink = instance_list_shrink
        # The metric for data ranking. Default value: **ByteCount**. This value indicates that Internet traffic data is ranked by traffic volume.
        # 
        # Valid values:
        # 
        # *   Rtt
        # *   ByteCount
        # *   PacketCount
        # *   RetransmitRate
        self.order_by = order_by
        # The remote city.
        # 
        # >  This parameter is required only if you set **TupleType** to **2** or **5**.
        self.other_city = other_city
        # The remote country.
        # 
        # >  This parameter is required only if you set **TupleType** to **2** or **5**.
        self.other_country = other_country
        # The remote IP address.
        # 
        # > This parameter is required only when you set **TupleType** to **2** or **5**.
        self.other_ip = other_ip
        # The remote ISP.
        # 
        # > This parameter is required if you want to view the information about the remote ISP.
        self.other_isp = other_isp
        # The remote port.
        # 
        # > This parameter is required only when you set **TupleType** to **5**.
        self.other_port = other_port
        # The protocol number.
        # 
        # > All protocols are supported. This parameter is required only when you set **TupleType** to **5**.
        self.protocol = protocol
        # The ID of the region for which you want to query the Internet traffic.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The order in which instances are ranked by Internet traffic. Valid values:
        # 
        # *   **desc**: the descending order
        # *   **asc**: the ascending order
        self.sort = sort
        # Specifies top-N traffic data to display. Default value: **10**. This value specifies to display top-10 traffic data by default. Max value: **100**.
        self.top_n = top_n
        # The type of the tuple. Valid values:
        # 
        # *   **1**: 1-tuple
        # *   **2**: 2-tuple
        # *   **5**: 5-tuple
        # 
        # This parameter is required.
        self.tuple_type = tuple_type
        # Specifies whether to enable the multi-account management feature. Default value: **false**. This value specifies that the multi-account management feature is disabled.
        # 
        # >  By default, the multi-account management feature is not available. If you want to use this feature, contact your account manager to apply for permissions.
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
        if self.cloud_ip_list_shrink is not None:
            result['CloudIpList'] = self.cloud_ip_list_shrink
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
        if m.get('CloudIpList') is not None:
            self.cloud_ip_list_shrink = m.get('CloudIpList')
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
        retransmit_rate: float = None,
        rtt: float = None,
    ):
        # The access point of Alibaba Cloud.
        # 
        # >  This parameter is valid only if you set **InstanceId** to the instance ID of an Anycast elastic IP address (EIP).
        self.access_region = access_region
        # The beginning of the time range that you queried. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.begin_time = begin_time
        # The traffic volume. Unit: bytes.
        self.byte_count = byte_count
        # The local city.
        self.cloud_city = cloud_city
        # The local country or region.
        self.cloud_country = cloud_country
        # The local IP address.
        self.cloud_ip = cloud_ip
        # The local ISP.
        self.cloud_isp = cloud_isp
        # The local port.
        self.cloud_port = cloud_port
        # The service code of the instance to which the local IP address belongs.
        self.cloud_product = cloud_product
        # The local province.
        self.cloud_province = cloud_province
        # The direction of Internet traffic. Valid values:
        # 
        # *   **in**: inbound
        # *   **out**: outbound
        self.direction = direction
        # The inbound traffic volume. Unit: bytes.
        self.in_byte_count = in_byte_count
        # The number of inbound disordered packets.
        self.in_out_order_count = in_out_order_count
        # The number of inbound packets.
        self.in_packet_count = in_packet_count
        # The number of inbound repeated packets.
        self.in_retran_count = in_retran_count
        # The ID of the instance to which the local IP address belongs.
        self.instance_id = instance_id
        # The remote city. In most cases, this parameter is empty if you set **OtherCountry** to a country except China.
        self.other_city = other_city
        # The remote country or region.
        self.other_country = other_country
        # The remote IP address.
        self.other_ip = other_ip
        # The remote ISP.
        self.other_isp = other_isp
        # The remote port.
        self.other_port = other_port
        # The service code of the instance to which the remote IP address belongs. If the IP address is not on the cloud, this parameter is empty.
        self.other_product = other_product
        # The remote province. In most cases, this parameter is empty if you set **OtherCountry** to a country except China.
        self.other_province = other_province
        # The outbound traffic volume. Unit: bytes.
        self.out_byte_count = out_byte_count
        # The number of disordered packets.
        self.out_order_count = out_order_count
        # The number of outbound disordered packets.
        self.out_out_order_count = out_out_order_count
        # The number of outbound packets.
        self.out_packet_count = out_packet_count
        # The number of outbound repeated packets.
        self.out_retran_count = out_retran_count
        # The number of packets.
        self.packet_count = packet_count
        # The protocol number.
        self.protocol = protocol
        # The retransmission rate of TCP packets.
        self.retransmit_rate = retransmit_rate
        # The round-trip time (RTT). Unit: milliseconds.
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
        if self.retransmit_rate is not None:
            result['RetransmitRate'] = self.retransmit_rate
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
        if m.get('RetransmitRate') is not None:
            self.retransmit_rate = m.get('RetransmitRate')
        if m.get('Rtt') is not None:
            self.rtt = m.get('Rtt')
        return self


class GetInternetTupleResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetInternetTupleResponseBodyData] = None,
        request_id: str = None,
    ):
        # The ranking result of Internet traffic data.
        self.data = data
        # The request ID.
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
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The end of the time range to query in milliseconds. The time range specified by **BeginTime** and **EndTime** cannot exceed **86400000** milliseconds (24 hours).
        self.end_time = end_time
        # Query ranking statistics for a specific IP address. If you specify this parameter, you do not need to specify **TopN** or **OrderBy**.
        self.ip = ip
        # The ID of the NAT gateway.
        # 
        # This parameter is required.
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
        # 
        # This parameter is required.
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


class GetNisNetworkMetricsRequestDimensions(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetNisNetworkMetricsRequest(TeaModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        begin_time: int = None,
        dimensions: List[GetNisNetworkMetricsRequestDimensions] = None,
        end_time: int = None,
        metric_name: str = None,
        region_no: str = None,
        resource_type: str = None,
        scan_by: str = None,
        use_cross_account: bool = None,
    ):
        self.account_ids = account_ids
        self.begin_time = begin_time
        # This parameter is required.
        self.dimensions = dimensions
        self.end_time = end_time
        # This parameter is required.
        self.metric_name = metric_name
        # This parameter is required.
        self.region_no = region_no
        # This parameter is required.
        self.resource_type = resource_type
        self.scan_by = scan_by
        self.use_cross_account = use_cross_account

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scan_by is not None:
            result['ScanBy'] = self.scan_by
        if self.use_cross_account is not None:
            result['UseCrossAccount'] = self.use_cross_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = GetNisNetworkMetricsRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ScanBy') is not None:
            self.scan_by = m.get('ScanBy')
        if m.get('UseCrossAccount') is not None:
            self.use_cross_account = m.get('UseCrossAccount')
        return self


class GetNisNetworkMetricsShrinkRequest(TeaModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        begin_time: int = None,
        dimensions_shrink: str = None,
        end_time: int = None,
        metric_name: str = None,
        region_no: str = None,
        resource_type: str = None,
        scan_by: str = None,
        use_cross_account: bool = None,
    ):
        self.account_ids = account_ids
        self.begin_time = begin_time
        # This parameter is required.
        self.dimensions_shrink = dimensions_shrink
        self.end_time = end_time
        # This parameter is required.
        self.metric_name = metric_name
        # This parameter is required.
        self.region_no = region_no
        # This parameter is required.
        self.resource_type = resource_type
        self.scan_by = scan_by
        self.use_cross_account = use_cross_account

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
        if self.dimensions_shrink is not None:
            result['Dimensions'] = self.dimensions_shrink
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scan_by is not None:
            result['ScanBy'] = self.scan_by
        if self.use_cross_account is not None:
            result['UseCrossAccount'] = self.use_cross_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('Dimensions') is not None:
            self.dimensions_shrink = m.get('Dimensions')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ScanBy') is not None:
            self.scan_by = m.get('ScanBy')
        if m.get('UseCrossAccount') is not None:
            self.use_cross_account = m.get('UseCrossAccount')
        return self


class GetNisNetworkMetricsResponseBodyDataMetrics(TeaModel):
    def __init__(
        self,
        time_stamp: int = None,
        value: float = None,
    ):
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetNisNetworkMetricsResponseBodyData(TeaModel):
    def __init__(
        self,
        metrics: List[GetNisNetworkMetricsResponseBodyDataMetrics] = None,
        unit: str = None,
    ):
        self.metrics = metrics
        self.unit = unit

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = GetNisNetworkMetricsResponseBodyDataMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class GetNisNetworkMetricsResponseBody(TeaModel):
    def __init__(
        self,
        data: GetNisNetworkMetricsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetNisNetworkMetricsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNisNetworkMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNisNetworkMetricsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetNisNetworkMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNisNetworkRankingRequestFilter(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetNisNetworkRankingRequest(TeaModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        begin_time: int = None,
        direction: str = None,
        end_time: int = None,
        filter: List[GetNisNetworkRankingRequestFilter] = None,
        group_by: str = None,
        order_by: str = None,
        region_no: str = None,
        resource_type: str = None,
        sort: str = None,
        top_n: int = None,
        use_cross_account: bool = None,
    ):
        self.account_ids = account_ids
        self.begin_time = begin_time
        # This parameter is required.
        self.direction = direction
        self.end_time = end_time
        self.filter = filter
        # This parameter is required.
        self.group_by = group_by
        # This parameter is required.
        self.order_by = order_by
        # This parameter is required.
        self.region_no = region_no
        # This parameter is required.
        self.resource_type = resource_type
        self.sort = sort
        self.top_n = top_n
        self.use_cross_account = use_cross_account

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.group_by is not None:
            result['GroupBy'] = self.group_by
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.top_n is not None:
            result['TopN'] = self.top_n
        if self.use_cross_account is not None:
            result['UseCrossAccount'] = self.use_cross_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = GetNisNetworkRankingRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('TopN') is not None:
            self.top_n = m.get('TopN')
        if m.get('UseCrossAccount') is not None:
            self.use_cross_account = m.get('UseCrossAccount')
        return self


class GetNisNetworkRankingShrinkRequest(TeaModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        begin_time: int = None,
        direction: str = None,
        end_time: int = None,
        filter_shrink: str = None,
        group_by: str = None,
        order_by: str = None,
        region_no: str = None,
        resource_type: str = None,
        sort: str = None,
        top_n: int = None,
        use_cross_account: bool = None,
    ):
        self.account_ids = account_ids
        self.begin_time = begin_time
        # This parameter is required.
        self.direction = direction
        self.end_time = end_time
        self.filter_shrink = filter_shrink
        # This parameter is required.
        self.group_by = group_by
        # This parameter is required.
        self.order_by = order_by
        # This parameter is required.
        self.region_no = region_no
        # This parameter is required.
        self.resource_type = resource_type
        self.sort = sort
        self.top_n = top_n
        self.use_cross_account = use_cross_account

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
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink
        if self.group_by is not None:
            result['GroupBy'] = self.group_by
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.top_n is not None:
            result['TopN'] = self.top_n
        if self.use_cross_account is not None:
            result['UseCrossAccount'] = self.use_cross_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Filter') is not None:
            self.filter_shrink = m.get('Filter')
        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('TopN') is not None:
            self.top_n = m.get('TopN')
        if m.get('UseCrossAccount') is not None:
            self.use_cross_account = m.get('UseCrossAccount')
        return self


class GetNisNetworkRankingResponseBodyData(TeaModel):
    def __init__(
        self,
        active_session_count: float = None,
        asn: str = None,
        attachment_id: str = None,
        bandwidth_package_id: str = None,
        byte_count: float = None,
        city: str = None,
        country: str = None,
        destination_ip: str = None,
        destination_isp: str = None,
        destination_port: str = None,
        destination_region_no: str = None,
        destination_zone: str = None,
        ip: str = None,
        in_bps: float = None,
        in_pps: float = None,
        instance_id: str = None,
        isp: str = None,
        new_session_per_second: float = None,
        out_bps: float = None,
        out_pps: float = None,
        packet_count: float = None,
        protocol: str = None,
        province: str = None,
        rtt: float = None,
        region_no: str = None,
        retransmit_rate: float = None,
        source_ip: str = None,
        source_isp: str = None,
        source_port: str = None,
        source_zone: str = None,
        vbr_id: str = None,
    ):
        self.active_session_count = active_session_count
        self.asn = asn
        self.attachment_id = attachment_id
        self.bandwidth_package_id = bandwidth_package_id
        self.byte_count = byte_count
        self.city = city
        self.country = country
        self.destination_ip = destination_ip
        self.destination_isp = destination_isp
        self.destination_port = destination_port
        self.destination_region_no = destination_region_no
        self.destination_zone = destination_zone
        self.ip = ip
        self.in_bps = in_bps
        self.in_pps = in_pps
        self.instance_id = instance_id
        self.isp = isp
        self.new_session_per_second = new_session_per_second
        self.out_bps = out_bps
        self.out_pps = out_pps
        self.packet_count = packet_count
        self.protocol = protocol
        self.province = province
        self.rtt = rtt
        self.region_no = region_no
        self.retransmit_rate = retransmit_rate
        self.source_ip = source_ip
        self.source_isp = source_isp
        self.source_port = source_port
        self.source_zone = source_zone
        self.vbr_id = vbr_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_session_count is not None:
            result['ActiveSessionCount'] = self.active_session_count
        if self.asn is not None:
            result['Asn'] = self.asn
        if self.attachment_id is not None:
            result['AttachmentId'] = self.attachment_id
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.byte_count is not None:
            result['ByteCount'] = self.byte_count
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.destination_ip is not None:
            result['DestinationIp'] = self.destination_ip
        if self.destination_isp is not None:
            result['DestinationIsp'] = self.destination_isp
        if self.destination_port is not None:
            result['DestinationPort'] = self.destination_port
        if self.destination_region_no is not None:
            result['DestinationRegionNo'] = self.destination_region_no
        if self.destination_zone is not None:
            result['DestinationZone'] = self.destination_zone
        if self.ip is not None:
            result['IP'] = self.ip
        if self.in_bps is not None:
            result['InBps'] = self.in_bps
        if self.in_pps is not None:
            result['InPps'] = self.in_pps
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.new_session_per_second is not None:
            result['NewSessionPerSecond'] = self.new_session_per_second
        if self.out_bps is not None:
            result['OutBps'] = self.out_bps
        if self.out_pps is not None:
            result['OutPps'] = self.out_pps
        if self.packet_count is not None:
            result['PacketCount'] = self.packet_count
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.province is not None:
            result['Province'] = self.province
        if self.rtt is not None:
            result['RTT'] = self.rtt
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.retransmit_rate is not None:
            result['RetransmitRate'] = self.retransmit_rate
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.source_isp is not None:
            result['SourceIsp'] = self.source_isp
        if self.source_port is not None:
            result['SourcePort'] = self.source_port
        if self.source_zone is not None:
            result['SourceZone'] = self.source_zone
        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveSessionCount') is not None:
            self.active_session_count = m.get('ActiveSessionCount')
        if m.get('Asn') is not None:
            self.asn = m.get('Asn')
        if m.get('AttachmentId') is not None:
            self.attachment_id = m.get('AttachmentId')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('ByteCount') is not None:
            self.byte_count = m.get('ByteCount')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('DestinationIp') is not None:
            self.destination_ip = m.get('DestinationIp')
        if m.get('DestinationIsp') is not None:
            self.destination_isp = m.get('DestinationIsp')
        if m.get('DestinationPort') is not None:
            self.destination_port = m.get('DestinationPort')
        if m.get('DestinationRegionNo') is not None:
            self.destination_region_no = m.get('DestinationRegionNo')
        if m.get('DestinationZone') is not None:
            self.destination_zone = m.get('DestinationZone')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InBps') is not None:
            self.in_bps = m.get('InBps')
        if m.get('InPps') is not None:
            self.in_pps = m.get('InPps')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('NewSessionPerSecond') is not None:
            self.new_session_per_second = m.get('NewSessionPerSecond')
        if m.get('OutBps') is not None:
            self.out_bps = m.get('OutBps')
        if m.get('OutPps') is not None:
            self.out_pps = m.get('OutPps')
        if m.get('PacketCount') is not None:
            self.packet_count = m.get('PacketCount')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RTT') is not None:
            self.rtt = m.get('RTT')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('RetransmitRate') is not None:
            self.retransmit_rate = m.get('RetransmitRate')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SourceIsp') is not None:
            self.source_isp = m.get('SourceIsp')
        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')
        if m.get('SourceZone') is not None:
            self.source_zone = m.get('SourceZone')
        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')
        return self


class GetNisNetworkRankingResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetNisNetworkRankingResponseBodyData] = None,
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
                temp_model = GetNisNetworkRankingResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNisNetworkRankingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNisNetworkRankingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetNisNetworkRankingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTransitRouterFlowTopNRequest(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        bandwith_package_id: str = None,
        begin_time: int = None,
        cen_id: str = None,
        direction: str = None,
        end_time: int = None,
        group_by: str = None,
        order_by: str = None,
        other_ip: str = None,
        other_port: str = None,
        other_region: str = None,
        protocol: str = None,
        sort: str = None,
        this_ip: str = None,
        this_port: str = None,
        this_region: str = None,
        top_n: int = None,
        use_multi_account: bool = None,
    ):
        # The IDs of the member accounts.
        self.account_ids = account_ids
        # The ID of the CEN bandwidth plan.
        self.bandwith_package_id = bandwith_package_id
        # The beginning of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. The maximum time range that you can query is 24 hours.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The CEN instance ID.
        self.cen_id = cen_id
        # The direction of the inter-region traffic in the local regions or for the local IP addresses. Valid values:
        # 
        # *   **in**: inbound traffic
        # *   **out**: outbound traffic
        # 
        # This parameter is required.
        self.direction = direction
        # The end of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. The maximum time range that you can query is 24 hours.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The dimension for ranking inter-region traffic data. The value of this parameter is case-sensitive. Valid values:
        # 
        # *   **1Tuple**: queries the rankings of inter-region traffic data for the local regions, Cloud Enterprise Network (CEN) instances, and IP addresses.
        # *   **2Tuple**: queries the rankings of inter-region traffic data for the local and remote regions, and the local and remote IP addresses.
        # *   **5Tuple**: queries the rankings of inter-region traffic data for the local and remote IP addresses, local and remote ports, and protocols.
        # *   **Cen**: queries the rankings of inter-region traffic data for CEN instances.
        # *   **RegionPair**: queries the rankings of inter-region traffic data for the local and remote regions.
        # *   **Port**: queries the rankings of inter-region traffic data for the local and remote ports.
        # *   **Protocol**: queries the rankings of inter-region traffic data for the protocols.
        # 
        # This parameter is required.
        self.group_by = group_by
        # The metric for ranking inter-region traffic data. Default value: Bytes. This value specifies that inter-region traffic data is ranked by traffic volume.
        self.order_by = order_by
        # The remote IP address.
        self.other_ip = other_ip
        # The remote port.
        self.other_port = other_port
        # The remote region.
        self.other_region = other_region
        # The protocol number.
        # 
        # >  All protocols are supported. This parameter is required only if you set **GroupBy** to **5Tuple** or **Protocol**.
        self.protocol = protocol
        # The order for ranking inter-region traffic data. Valid values:
        # 
        # *   **desc**: descending order
        # *   **asc**: ascending order
        self.sort = sort
        # The local IP address.
        self.this_ip = this_ip
        # The local port.
        self.this_port = this_port
        # The local region where the **local IP address** resides.
        self.this_region = this_region
        # Specifies the maximum number of data entries to display. Default value: **10**. Maximum value: 100.
        self.top_n = top_n
        # Specifies whether to enable the multi-account management feature. Default value: **false**. This value specifies that the multi-account management feature is disabled.
        # 
        # >  By default, the multi-account management feature is not available. If you want to use this feature, contact your account manager to apply for permissions.
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
        if self.bandwith_package_id is not None:
            result['BandwithPackageId'] = self.bandwith_package_id
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group_by is not None:
            result['GroupBy'] = self.group_by
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.other_ip is not None:
            result['OtherIp'] = self.other_ip
        if self.other_port is not None:
            result['OtherPort'] = self.other_port
        if self.other_region is not None:
            result['OtherRegion'] = self.other_region
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.this_ip is not None:
            result['ThisIp'] = self.this_ip
        if self.this_port is not None:
            result['ThisPort'] = self.this_port
        if self.this_region is not None:
            result['ThisRegion'] = self.this_region
        if self.top_n is not None:
            result['TopN'] = self.top_n
        if self.use_multi_account is not None:
            result['UseMultiAccount'] = self.use_multi_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('BandwithPackageId') is not None:
            self.bandwith_package_id = m.get('BandwithPackageId')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OtherIp') is not None:
            self.other_ip = m.get('OtherIp')
        if m.get('OtherPort') is not None:
            self.other_port = m.get('OtherPort')
        if m.get('OtherRegion') is not None:
            self.other_region = m.get('OtherRegion')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('ThisIp') is not None:
            self.this_ip = m.get('ThisIp')
        if m.get('ThisPort') is not None:
            self.this_port = m.get('ThisPort')
        if m.get('ThisRegion') is not None:
            self.this_region = m.get('ThisRegion')
        if m.get('TopN') is not None:
            self.top_n = m.get('TopN')
        if m.get('UseMultiAccount') is not None:
            self.use_multi_account = m.get('UseMultiAccount')
        return self


class GetTransitRouterFlowTopNShrinkRequest(TeaModel):
    def __init__(
        self,
        account_ids_shrink: str = None,
        bandwith_package_id: str = None,
        begin_time: int = None,
        cen_id: str = None,
        direction: str = None,
        end_time: int = None,
        group_by: str = None,
        order_by: str = None,
        other_ip: str = None,
        other_port: str = None,
        other_region: str = None,
        protocol: str = None,
        sort: str = None,
        this_ip: str = None,
        this_port: str = None,
        this_region: str = None,
        top_n: int = None,
        use_multi_account: bool = None,
    ):
        # The IDs of the member accounts.
        self.account_ids_shrink = account_ids_shrink
        # The ID of the CEN bandwidth plan.
        self.bandwith_package_id = bandwith_package_id
        # The beginning of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. The maximum time range that you can query is 24 hours.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The CEN instance ID.
        self.cen_id = cen_id
        # The direction of the inter-region traffic in the local regions or for the local IP addresses. Valid values:
        # 
        # *   **in**: inbound traffic
        # *   **out**: outbound traffic
        # 
        # This parameter is required.
        self.direction = direction
        # The end of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. The maximum time range that you can query is 24 hours.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The dimension for ranking inter-region traffic data. The value of this parameter is case-sensitive. Valid values:
        # 
        # *   **1Tuple**: queries the rankings of inter-region traffic data for the local regions, Cloud Enterprise Network (CEN) instances, and IP addresses.
        # *   **2Tuple**: queries the rankings of inter-region traffic data for the local and remote regions, and the local and remote IP addresses.
        # *   **5Tuple**: queries the rankings of inter-region traffic data for the local and remote IP addresses, local and remote ports, and protocols.
        # *   **Cen**: queries the rankings of inter-region traffic data for CEN instances.
        # *   **RegionPair**: queries the rankings of inter-region traffic data for the local and remote regions.
        # *   **Port**: queries the rankings of inter-region traffic data for the local and remote ports.
        # *   **Protocol**: queries the rankings of inter-region traffic data for the protocols.
        # 
        # This parameter is required.
        self.group_by = group_by
        # The metric for ranking inter-region traffic data. Default value: Bytes. This value specifies that inter-region traffic data is ranked by traffic volume.
        self.order_by = order_by
        # The remote IP address.
        self.other_ip = other_ip
        # The remote port.
        self.other_port = other_port
        # The remote region.
        self.other_region = other_region
        # The protocol number.
        # 
        # >  All protocols are supported. This parameter is required only if you set **GroupBy** to **5Tuple** or **Protocol**.
        self.protocol = protocol
        # The order for ranking inter-region traffic data. Valid values:
        # 
        # *   **desc**: descending order
        # *   **asc**: ascending order
        self.sort = sort
        # The local IP address.
        self.this_ip = this_ip
        # The local port.
        self.this_port = this_port
        # The local region where the **local IP address** resides.
        self.this_region = this_region
        # Specifies the maximum number of data entries to display. Default value: **10**. Maximum value: 100.
        self.top_n = top_n
        # Specifies whether to enable the multi-account management feature. Default value: **false**. This value specifies that the multi-account management feature is disabled.
        # 
        # >  By default, the multi-account management feature is not available. If you want to use this feature, contact your account manager to apply for permissions.
        self.use_multi_account = use_multi_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids_shrink is not None:
            result['AccountIds'] = self.account_ids_shrink
        if self.bandwith_package_id is not None:
            result['BandwithPackageId'] = self.bandwith_package_id
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group_by is not None:
            result['GroupBy'] = self.group_by
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.other_ip is not None:
            result['OtherIp'] = self.other_ip
        if self.other_port is not None:
            result['OtherPort'] = self.other_port
        if self.other_region is not None:
            result['OtherRegion'] = self.other_region
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.this_ip is not None:
            result['ThisIp'] = self.this_ip
        if self.this_port is not None:
            result['ThisPort'] = self.this_port
        if self.this_region is not None:
            result['ThisRegion'] = self.this_region
        if self.top_n is not None:
            result['TopN'] = self.top_n
        if self.use_multi_account is not None:
            result['UseMultiAccount'] = self.use_multi_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids_shrink = m.get('AccountIds')
        if m.get('BandwithPackageId') is not None:
            self.bandwith_package_id = m.get('BandwithPackageId')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OtherIp') is not None:
            self.other_ip = m.get('OtherIp')
        if m.get('OtherPort') is not None:
            self.other_port = m.get('OtherPort')
        if m.get('OtherRegion') is not None:
            self.other_region = m.get('OtherRegion')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('ThisIp') is not None:
            self.this_ip = m.get('ThisIp')
        if m.get('ThisPort') is not None:
            self.this_port = m.get('ThisPort')
        if m.get('ThisRegion') is not None:
            self.this_region = m.get('ThisRegion')
        if m.get('TopN') is not None:
            self.top_n = m.get('TopN')
        if m.get('UseMultiAccount') is not None:
            self.use_multi_account = m.get('UseMultiAccount')
        return self


class GetTransitRouterFlowTopNResponseBodyTransitRouterFlowTopN(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        bandwith_package_id: str = None,
        bytes: float = None,
        cen_id: str = None,
        end_time: str = None,
        other_ip: str = None,
        other_port: str = None,
        other_region: str = None,
        packets: float = None,
        protocol: str = None,
        start_time: str = None,
        this_ip: str = None,
        this_port: str = None,
        this_region: str = None,
    ):
        # The account ID.
        self.account_id = account_id
        # The ID of the CEN bandwidth plan.
        self.bandwith_package_id = bandwith_package_id
        # The total volume of traffic in the specified time range.
        self.bytes = bytes
        # The CEN instance ID.
        self.cen_id = cen_id
        # The end of the time range that you queried. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.end_time = end_time
        # The remote IP address.
        self.other_ip = other_ip
        # The remote port.
        self.other_port = other_port
        # The remote region where the **remote IP address** resides.
        self.other_region = other_region
        # The total number of packets in the specified time range.
        self.packets = packets
        # The protocol number.
        self.protocol = protocol
        # The beginning of the time range that you queried. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time
        # The local IP address.
        self.this_ip = this_ip
        # The local port.
        self.this_port = this_port
        # The local region where the **local IP address** resides.
        self.this_region = this_region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.bandwith_package_id is not None:
            result['BandwithPackageId'] = self.bandwith_package_id
        if self.bytes is not None:
            result['Bytes'] = self.bytes
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.other_ip is not None:
            result['OtherIp'] = self.other_ip
        if self.other_port is not None:
            result['OtherPort'] = self.other_port
        if self.other_region is not None:
            result['OtherRegion'] = self.other_region
        if self.packets is not None:
            result['Packets'] = self.packets
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.this_ip is not None:
            result['ThisIp'] = self.this_ip
        if self.this_port is not None:
            result['ThisPort'] = self.this_port
        if self.this_region is not None:
            result['ThisRegion'] = self.this_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('BandwithPackageId') is not None:
            self.bandwith_package_id = m.get('BandwithPackageId')
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OtherIp') is not None:
            self.other_ip = m.get('OtherIp')
        if m.get('OtherPort') is not None:
            self.other_port = m.get('OtherPort')
        if m.get('OtherRegion') is not None:
            self.other_region = m.get('OtherRegion')
        if m.get('Packets') is not None:
            self.packets = m.get('Packets')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ThisIp') is not None:
            self.this_ip = m.get('ThisIp')
        if m.get('ThisPort') is not None:
            self.this_port = m.get('ThisPort')
        if m.get('ThisRegion') is not None:
            self.this_region = m.get('ThisRegion')
        return self


class GetTransitRouterFlowTopNResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        transit_router_flow_top_n: List[GetTransitRouterFlowTopNResponseBodyTransitRouterFlowTopN] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The ranking result of inter-region traffic data.
        self.transit_router_flow_top_n = transit_router_flow_top_n

    def validate(self):
        if self.transit_router_flow_top_n:
            for k in self.transit_router_flow_top_n:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TransitRouterFlowTopN'] = []
        if self.transit_router_flow_top_n is not None:
            for k in self.transit_router_flow_top_n:
                result['TransitRouterFlowTopN'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.transit_router_flow_top_n = []
        if m.get('TransitRouterFlowTopN') is not None:
            for k in m.get('TransitRouterFlowTopN'):
                temp_model = GetTransitRouterFlowTopNResponseBodyTransitRouterFlowTopN()
                self.transit_router_flow_top_n.append(temp_model.from_map(k))
        return self


class GetTransitRouterFlowTopNResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTransitRouterFlowTopNResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetTransitRouterFlowTopNResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVbrFlowTopNRequest(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        attachment_id: str = None,
        begin_time: int = None,
        cen_id: str = None,
        cloud_ip: str = None,
        cloud_port: str = None,
        direction: str = None,
        end_time: int = None,
        group_by: str = None,
        order_by: str = None,
        other_ip: str = None,
        other_port: str = None,
        protocol: str = None,
        region_id: str = None,
        sort: str = None,
        top_n: int = None,
        use_multi_account: bool = None,
        virtual_border_router_id: str = None,
    ):
        # The IDs of member accounts.
        self.account_ids = account_ids
        # The CEN connection ID.
        self.attachment_id = attachment_id
        # The beginning of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. The maximum time range that you can query is 24 hours.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The CEN instance ID.
        self.cen_id = cen_id
        # The local IP address.
        self.cloud_ip = cloud_ip
        # The local port.
        # 
        # >  This parameter is required only if you set **GroupBy** to **CloudPort**.
        self.cloud_port = cloud_port
        # The direction of the hybrid cloud traffic in the local regions or for the local IP addresses. Valid values:
        # 
        # *   **in**: traffic from a data center to Alibaba Cloud
        # *   **out**: traffic from Alibaba Cloud to a data center
        # 
        # This parameter is required.
        self.direction = direction
        # The end of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. The maximum time range that you can query is 24 hours.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The dimension for ranking hybrid cloud traffic data. The value of this parameter is case-sensitive. Valid values:
        # 
        # *   **1Tuple**: queries the rankings of hybrid cloud traffic data for the Cloud Enterprise Network (CEN) instances, CEN connections, virtual border routers (VBRs), and IP addresses.
        # *   **2Tuple**: queries the rankings of hybrid cloud traffic data for the local and remote IP addresses.
        # *   **5Tuple**: queries the rankings of hybrid cloud traffic data for the local and remote IP addresses, local and remote ports, and protocols.
        # *   **CloudPort**: queries the rankings of hybrid cloud traffic data for the local ports.
        # *   **OtherPort**: queries the rankings of hybrid cloud traffic data for the remote ports.
        # *   **Protocol**: queries the rankings of hybrid cloud traffic data for the protocols.
        # 
        # This parameter is required.
        self.group_by = group_by
        # The metric for ranking hybrid cloud traffic data. Default value: Bytes. This value specifies that hybrid cloud traffic data is ranked by traffic volumes.
        self.order_by = order_by
        # The remote IP address.
        self.other_ip = other_ip
        # The remote port.
        # 
        # >  This parameter is required only if you set **GroupBy** to **OtherPort**.
        self.other_port = other_port
        # The protocol number.
        # 
        # >  All protocols are supported. This parameter is required only if you set **GroupBy** to **5Tuple** or **Protocol**.
        self.protocol = protocol
        # The local region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The order for ranking hybrid cloud traffic data. Valid values:
        # 
        # *   **desc**: descending order
        # *   **asc**: ascending order
        self.sort = sort
        # Specifies top-N traffic data to display. Default value: **10**. This value specifies that top-10 traffic data is displayed by default. Maximum value: **100**.
        self.top_n = top_n
        # Specifies whether to enable the multi-account management feature. Default value: **false**. This value specifies that the multi-account management feature is disabled.
        # 
        # >  By default, the multi-account management feature is not available. If you want to use this feature, contact your account manager to apply for permissions.
        self.use_multi_account = use_multi_account
        # The ID of the VBR that is associated with the Express Connect circuit.
        self.virtual_border_router_id = virtual_border_router_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.attachment_id is not None:
            result['AttachmentId'] = self.attachment_id
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cloud_ip is not None:
            result['CloudIp'] = self.cloud_ip
        if self.cloud_port is not None:
            result['CloudPort'] = self.cloud_port
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group_by is not None:
            result['GroupBy'] = self.group_by
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.other_ip is not None:
            result['OtherIp'] = self.other_ip
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
        if self.use_multi_account is not None:
            result['UseMultiAccount'] = self.use_multi_account
        if self.virtual_border_router_id is not None:
            result['VirtualBorderRouterId'] = self.virtual_border_router_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('AttachmentId') is not None:
            self.attachment_id = m.get('AttachmentId')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CloudIp') is not None:
            self.cloud_ip = m.get('CloudIp')
        if m.get('CloudPort') is not None:
            self.cloud_port = m.get('CloudPort')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OtherIp') is not None:
            self.other_ip = m.get('OtherIp')
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
        if m.get('UseMultiAccount') is not None:
            self.use_multi_account = m.get('UseMultiAccount')
        if m.get('VirtualBorderRouterId') is not None:
            self.virtual_border_router_id = m.get('VirtualBorderRouterId')
        return self


class GetVbrFlowTopNShrinkRequest(TeaModel):
    def __init__(
        self,
        account_ids_shrink: str = None,
        attachment_id: str = None,
        begin_time: int = None,
        cen_id: str = None,
        cloud_ip: str = None,
        cloud_port: str = None,
        direction: str = None,
        end_time: int = None,
        group_by: str = None,
        order_by: str = None,
        other_ip: str = None,
        other_port: str = None,
        protocol: str = None,
        region_id: str = None,
        sort: str = None,
        top_n: int = None,
        use_multi_account: bool = None,
        virtual_border_router_id: str = None,
    ):
        # The IDs of member accounts.
        self.account_ids_shrink = account_ids_shrink
        # The CEN connection ID.
        self.attachment_id = attachment_id
        # The beginning of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. The maximum time range that you can query is 24 hours.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The CEN instance ID.
        self.cen_id = cen_id
        # The local IP address.
        self.cloud_ip = cloud_ip
        # The local port.
        # 
        # >  This parameter is required only if you set **GroupBy** to **CloudPort**.
        self.cloud_port = cloud_port
        # The direction of the hybrid cloud traffic in the local regions or for the local IP addresses. Valid values:
        # 
        # *   **in**: traffic from a data center to Alibaba Cloud
        # *   **out**: traffic from Alibaba Cloud to a data center
        # 
        # This parameter is required.
        self.direction = direction
        # The end of the time range to query. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. The maximum time range that you can query is 24 hours.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The dimension for ranking hybrid cloud traffic data. The value of this parameter is case-sensitive. Valid values:
        # 
        # *   **1Tuple**: queries the rankings of hybrid cloud traffic data for the Cloud Enterprise Network (CEN) instances, CEN connections, virtual border routers (VBRs), and IP addresses.
        # *   **2Tuple**: queries the rankings of hybrid cloud traffic data for the local and remote IP addresses.
        # *   **5Tuple**: queries the rankings of hybrid cloud traffic data for the local and remote IP addresses, local and remote ports, and protocols.
        # *   **CloudPort**: queries the rankings of hybrid cloud traffic data for the local ports.
        # *   **OtherPort**: queries the rankings of hybrid cloud traffic data for the remote ports.
        # *   **Protocol**: queries the rankings of hybrid cloud traffic data for the protocols.
        # 
        # This parameter is required.
        self.group_by = group_by
        # The metric for ranking hybrid cloud traffic data. Default value: Bytes. This value specifies that hybrid cloud traffic data is ranked by traffic volumes.
        self.order_by = order_by
        # The remote IP address.
        self.other_ip = other_ip
        # The remote port.
        # 
        # >  This parameter is required only if you set **GroupBy** to **OtherPort**.
        self.other_port = other_port
        # The protocol number.
        # 
        # >  All protocols are supported. This parameter is required only if you set **GroupBy** to **5Tuple** or **Protocol**.
        self.protocol = protocol
        # The local region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The order for ranking hybrid cloud traffic data. Valid values:
        # 
        # *   **desc**: descending order
        # *   **asc**: ascending order
        self.sort = sort
        # Specifies top-N traffic data to display. Default value: **10**. This value specifies that top-10 traffic data is displayed by default. Maximum value: **100**.
        self.top_n = top_n
        # Specifies whether to enable the multi-account management feature. Default value: **false**. This value specifies that the multi-account management feature is disabled.
        # 
        # >  By default, the multi-account management feature is not available. If you want to use this feature, contact your account manager to apply for permissions.
        self.use_multi_account = use_multi_account
        # The ID of the VBR that is associated with the Express Connect circuit.
        self.virtual_border_router_id = virtual_border_router_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids_shrink is not None:
            result['AccountIds'] = self.account_ids_shrink
        if self.attachment_id is not None:
            result['AttachmentId'] = self.attachment_id
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cloud_ip is not None:
            result['CloudIp'] = self.cloud_ip
        if self.cloud_port is not None:
            result['CloudPort'] = self.cloud_port
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group_by is not None:
            result['GroupBy'] = self.group_by
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.other_ip is not None:
            result['OtherIp'] = self.other_ip
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
        if self.use_multi_account is not None:
            result['UseMultiAccount'] = self.use_multi_account
        if self.virtual_border_router_id is not None:
            result['VirtualBorderRouterId'] = self.virtual_border_router_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids_shrink = m.get('AccountIds')
        if m.get('AttachmentId') is not None:
            self.attachment_id = m.get('AttachmentId')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CloudIp') is not None:
            self.cloud_ip = m.get('CloudIp')
        if m.get('CloudPort') is not None:
            self.cloud_port = m.get('CloudPort')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OtherIp') is not None:
            self.other_ip = m.get('OtherIp')
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
        if m.get('UseMultiAccount') is not None:
            self.use_multi_account = m.get('UseMultiAccount')
        if m.get('VirtualBorderRouterId') is not None:
            self.virtual_border_router_id = m.get('VirtualBorderRouterId')
        return self


class GetVbrFlowTopNResponseBodyVirtualBorderRouterFlowlogTopN(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        attachment_id: str = None,
        bytes: float = None,
        cloud_ip: str = None,
        cloud_port: str = None,
        cloud_region: str = None,
        other_ip: str = None,
        other_port: str = None,
        packets: float = None,
        protocol: str = None,
        virtual_border_router_id: str = None,
    ):
        # The account ID.
        self.account_id = account_id
        # The CEN connection ID.
        self.attachment_id = attachment_id
        # The total volume of traffic in the specified time range.
        self.bytes = bytes
        # The local IP address.
        self.cloud_ip = cloud_ip
        # The local port.
        self.cloud_port = cloud_port
        # The local region where the local IP address resides.
        self.cloud_region = cloud_region
        # The remote IP address.
        self.other_ip = other_ip
        # The remote port.
        self.other_port = other_port
        # The total number of packets in the specified time range.
        self.packets = packets
        # The protocol number.
        self.protocol = protocol
        # The ID of the VBR that is associated with the Express Connect circuit.
        self.virtual_border_router_id = virtual_border_router_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.attachment_id is not None:
            result['AttachmentId'] = self.attachment_id
        if self.bytes is not None:
            result['Bytes'] = self.bytes
        if self.cloud_ip is not None:
            result['CloudIp'] = self.cloud_ip
        if self.cloud_port is not None:
            result['CloudPort'] = self.cloud_port
        if self.cloud_region is not None:
            result['CloudRegion'] = self.cloud_region
        if self.other_ip is not None:
            result['OtherIp'] = self.other_ip
        if self.other_port is not None:
            result['OtherPort'] = self.other_port
        if self.packets is not None:
            result['Packets'] = self.packets
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.virtual_border_router_id is not None:
            result['VirtualBorderRouterId'] = self.virtual_border_router_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AttachmentId') is not None:
            self.attachment_id = m.get('AttachmentId')
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')
        if m.get('CloudIp') is not None:
            self.cloud_ip = m.get('CloudIp')
        if m.get('CloudPort') is not None:
            self.cloud_port = m.get('CloudPort')
        if m.get('CloudRegion') is not None:
            self.cloud_region = m.get('CloudRegion')
        if m.get('OtherIp') is not None:
            self.other_ip = m.get('OtherIp')
        if m.get('OtherPort') is not None:
            self.other_port = m.get('OtherPort')
        if m.get('Packets') is not None:
            self.packets = m.get('Packets')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('VirtualBorderRouterId') is not None:
            self.virtual_border_router_id = m.get('VirtualBorderRouterId')
        return self


class GetVbrFlowTopNResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        virtual_border_router_flowlog_top_n: List[GetVbrFlowTopNResponseBodyVirtualBorderRouterFlowlogTopN] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The ranking result of hybrid cloud traffic data.
        self.virtual_border_router_flowlog_top_n = virtual_border_router_flowlog_top_n

    def validate(self):
        if self.virtual_border_router_flowlog_top_n:
            for k in self.virtual_border_router_flowlog_top_n:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VirtualBorderRouterFlowlogTopN'] = []
        if self.virtual_border_router_flowlog_top_n is not None:
            for k in self.virtual_border_router_flowlog_top_n:
                result['VirtualBorderRouterFlowlogTopN'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.virtual_border_router_flowlog_top_n = []
        if m.get('VirtualBorderRouterFlowlogTopN') is not None:
            for k in m.get('VirtualBorderRouterFlowlogTopN'):
                temp_model = GetVbrFlowTopNResponseBodyVirtualBorderRouterFlowlogTopN()
                self.virtual_border_router_flowlog_top_n.append(temp_model.from_map(k))
        return self


class GetVbrFlowTopNResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVbrFlowTopNResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetVbrFlowTopNResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNisInspectionResourceTypeResponseBodyResourceTypeList(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
    ):
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListNisInspectionResourceTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_type_list: List[ListNisInspectionResourceTypeResponseBodyResourceTypeList] = None,
    ):
        self.request_id = request_id
        self.resource_type_list = resource_type_list

    def validate(self):
        if self.resource_type_list:
            for k in self.resource_type_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceTypeList'] = []
        if self.resource_type_list is not None:
            for k in self.resource_type_list:
                result['ResourceTypeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_type_list = []
        if m.get('ResourceTypeList') is not None:
            for k in m.get('ResourceTypeList'):
                temp_model = ListNisInspectionResourceTypeResponseBodyResourceTypeList()
                self.resource_type_list.append(temp_model.from_map(k))
        return self


class ListNisInspectionResourceTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNisInspectionResourceTypeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListNisInspectionResourceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNisInspectionTaskReportsRequest(TeaModel):
    def __init__(
        self,
        inspection_task_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # This parameter is required.
        self.inspection_task_id = inspection_task_id
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inspection_task_id is not None:
            result['InspectionTaskId'] = self.inspection_task_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InspectionTaskId') is not None:
            self.inspection_task_id = m.get('InspectionTaskId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListNisInspectionTaskReportsResponseBodyInspectionReportList(TeaModel):
    def __init__(
        self,
        inspection_report_id: str = None,
    ):
        self.inspection_report_id = inspection_report_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inspection_report_id is not None:
            result['InspectionReportId'] = self.inspection_report_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InspectionReportId') is not None:
            self.inspection_report_id = m.get('InspectionReportId')
        return self


class ListNisInspectionTaskReportsResponseBody(TeaModel):
    def __init__(
        self,
        inspection_report_list: List[ListNisInspectionTaskReportsResponseBodyInspectionReportList] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.inspection_report_list = inspection_report_list
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.inspection_report_list:
            for k in self.inspection_report_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InspectionReportList'] = []
        if self.inspection_report_list is not None:
            for k in self.inspection_report_list:
                result['InspectionReportList'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.inspection_report_list = []
        if m.get('InspectionReportList') is not None:
            for k in m.get('InspectionReportList'):
                temp_model = ListNisInspectionTaskReportsResponseBodyInspectionReportList()
                self.inspection_report_list.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNisInspectionTaskReportsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNisInspectionTaskReportsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListNisInspectionTaskReportsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNisInspectionTasksRequest(TeaModel):
    def __init__(
        self,
        inspection_name: str = None,
        inspection_project: str = None,
        inspection_task_id: str = None,
        max_results: int = None,
        next_token: str = None,
        status: str = None,
    ):
        self.inspection_name = inspection_name
        self.inspection_project = inspection_project
        self.inspection_task_id = inspection_task_id
        self.max_results = max_results
        self.next_token = next_token
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inspection_name is not None:
            result['InspectionName'] = self.inspection_name
        if self.inspection_project is not None:
            result['InspectionProject'] = self.inspection_project
        if self.inspection_task_id is not None:
            result['InspectionTaskId'] = self.inspection_task_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InspectionName') is not None:
            self.inspection_name = m.get('InspectionName')
        if m.get('InspectionProject') is not None:
            self.inspection_project = m.get('InspectionProject')
        if m.get('InspectionTaskId') is not None:
            self.inspection_task_id = m.get('InspectionTaskId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListNisInspectionTasksResponseBodyInspectionTaskList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        inspection_name: str = None,
        inspection_project: str = None,
        inspection_task_id: str = None,
        last_update_report_id: str = None,
        status: str = None,
    ):
        self.create_time = create_time
        self.inspection_name = inspection_name
        self.inspection_project = inspection_project
        self.inspection_task_id = inspection_task_id
        self.last_update_report_id = last_update_report_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.inspection_name is not None:
            result['InspectionName'] = self.inspection_name
        if self.inspection_project is not None:
            result['InspectionProject'] = self.inspection_project
        if self.inspection_task_id is not None:
            result['InspectionTaskId'] = self.inspection_task_id
        if self.last_update_report_id is not None:
            result['LastUpdateReportId'] = self.last_update_report_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InspectionName') is not None:
            self.inspection_name = m.get('InspectionName')
        if m.get('InspectionProject') is not None:
            self.inspection_project = m.get('InspectionProject')
        if m.get('InspectionTaskId') is not None:
            self.inspection_task_id = m.get('InspectionTaskId')
        if m.get('LastUpdateReportId') is not None:
            self.last_update_report_id = m.get('LastUpdateReportId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListNisInspectionTasksResponseBody(TeaModel):
    def __init__(
        self,
        inspection_task_list: List[ListNisInspectionTasksResponseBodyInspectionTaskList] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.inspection_task_list = inspection_task_list
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.inspection_task_list:
            for k in self.inspection_task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InspectionTaskList'] = []
        if self.inspection_task_list is not None:
            for k in self.inspection_task_list:
                result['InspectionTaskList'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.inspection_task_list = []
        if m.get('InspectionTaskList') is not None:
            for k in m.get('InspectionTaskList'):
                temp_model = ListNisInspectionTasksResponseBodyInspectionTaskList()
                self.inspection_task_list.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNisInspectionTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNisInspectionTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListNisInspectionTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartNisInspectionTaskRequest(TeaModel):
    def __init__(
        self,
        inspection_task_id: str = None,
    ):
        # This parameter is required.
        self.inspection_task_id = inspection_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inspection_task_id is not None:
            result['InspectionTaskId'] = self.inspection_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InspectionTaskId') is not None:
            self.inspection_task_id = m.get('InspectionTaskId')
        return self


class StartNisInspectionTaskResponseBody(TeaModel):
    def __init__(
        self,
        inspection_report_id: str = None,
        request_id: str = None,
    ):
        self.inspection_report_id = inspection_report_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inspection_report_id is not None:
            result['InspectionReportId'] = self.inspection_report_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InspectionReportId') is not None:
            self.inspection_report_id = m.get('InspectionReportId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartNisInspectionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartNisInspectionTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = StartNisInspectionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNisInspectionTaskRequest(TeaModel):
    def __init__(
        self,
        inspection_task_id: str = None,
        status: str = None,
    ):
        # This parameter is required.
        self.inspection_task_id = inspection_task_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inspection_task_id is not None:
            result['InspectionTaskId'] = self.inspection_task_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InspectionTaskId') is not None:
            self.inspection_task_id = m.get('InspectionTaskId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateNisInspectionTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateNisInspectionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateNisInspectionTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateNisInspectionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


