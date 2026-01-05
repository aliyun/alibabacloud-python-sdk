# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudPhoneNodesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        node_model: List[main_models.DescribeCloudPhoneNodesResponseBodyNodeModel] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   ****
        self.next_token = next_token
        # The matrixes.
        self.node_model = node_model
        # The request ID.
        self.request_id = request_id
        # The total number of cloud phone instances.
        self.total_count = total_count

    def validate(self):
        if self.node_model:
            for v1 in self.node_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['NodeModel'] = []
        if self.node_model is not None:
            for k1 in self.node_model:
                result['NodeModel'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.node_model = []
        if m.get('NodeModel') is not None:
            for k1 in m.get('NodeModel'):
                temp_model = main_models.DescribeCloudPhoneNodesResponseBodyNodeModel()
                self.node_model.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCloudPhoneNodesResponseBodyNodeModel(DaraModel):
    def __init__(
        self,
        bandwidth_package_id: str = None,
        bandwidth_package_status: str = None,
        bandwidth_package_type: str = None,
        biz_tags: List[main_models.DescribeCloudPhoneNodesResponseBodyNodeModelBizTags] = None,
        charge_type: str = None,
        cpu: str = None,
        gmt_create: str = None,
        gmt_expired: str = None,
        gmt_modified: str = None,
        instance_type: str = None,
        memory: int = None,
        network_id: str = None,
        network_infos: List[main_models.DescribeCloudPhoneNodesResponseBodyNodeModelNetworkInfos] = None,
        network_type: str = None,
        node_id: str = None,
        node_name: str = None,
        phone_count: int = None,
        phone_data_info: main_models.DescribeCloudPhoneNodesResponseBodyNodeModelPhoneDataInfo = None,
        region_id: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
        server_type: str = None,
        share_data_volume: int = None,
        status: str = None,
        swap_size: int = None,
        v_switch_id: str = None,
    ):
        self.bandwidth_package_id = bandwidth_package_id
        self.bandwidth_package_status = bandwidth_package_status
        self.bandwidth_package_type = bandwidth_package_type
        self.biz_tags = biz_tags
        # The billing method.
        self.charge_type = charge_type
        # The number of CPU cores.
        self.cpu = cpu
        # The creation time.
        self.gmt_create = gmt_create
        # The expiration time of the subscription matrix.
        self.gmt_expired = gmt_expired
        # The last modification time.
        self.gmt_modified = gmt_modified
        self.instance_type = instance_type
        # The memory size. Unit: GB.
        self.memory = memory
        # The network ID.
        self.network_id = network_id
        self.network_infos = network_infos
        self.network_type = network_type
        # The matrix ID.
        self.node_id = node_id
        # The matrix name.
        self.node_name = node_name
        # The number of cloud phone instances per matrix.
        self.phone_count = phone_count
        self.phone_data_info = phone_data_info
        # The region ID.
        self.region_id = region_id
        # The height of the resolution. Unit: pixel.
        self.resolution_height = resolution_height
        # The width of the resolution. Unit: pixel.
        self.resolution_width = resolution_width
        # The matrix specification.
        self.server_type = server_type
        # The size of the shared storage. Unit: GiB.
        self.share_data_volume = share_data_volume
        # The matrix status.
        self.status = status
        self.swap_size = swap_size
        # The vSwitch ID.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.biz_tags:
            for v1 in self.biz_tags:
                 if v1:
                    v1.validate()
        if self.network_infos:
            for v1 in self.network_infos:
                 if v1:
                    v1.validate()
        if self.phone_data_info:
            self.phone_data_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.bandwidth_package_status is not None:
            result['BandwidthPackageStatus'] = self.bandwidth_package_status

        if self.bandwidth_package_type is not None:
            result['BandwidthPackageType'] = self.bandwidth_package_type

        result['BizTags'] = []
        if self.biz_tags is not None:
            for k1 in self.biz_tags:
                result['BizTags'].append(k1.to_map() if k1 else None)

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_expired is not None:
            result['GmtExpired'] = self.gmt_expired

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        result['NetworkInfos'] = []
        if self.network_infos is not None:
            for k1 in self.network_infos:
                result['NetworkInfos'].append(k1.to_map() if k1 else None)

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.phone_count is not None:
            result['PhoneCount'] = self.phone_count

        if self.phone_data_info is not None:
            result['PhoneDataInfo'] = self.phone_data_info.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height

        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width

        if self.server_type is not None:
            result['ServerType'] = self.server_type

        if self.share_data_volume is not None:
            result['ShareDataVolume'] = self.share_data_volume

        if self.status is not None:
            result['Status'] = self.status

        if self.swap_size is not None:
            result['SwapSize'] = self.swap_size

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('BandwidthPackageStatus') is not None:
            self.bandwidth_package_status = m.get('BandwidthPackageStatus')

        if m.get('BandwidthPackageType') is not None:
            self.bandwidth_package_type = m.get('BandwidthPackageType')

        self.biz_tags = []
        if m.get('BizTags') is not None:
            for k1 in m.get('BizTags'):
                temp_model = main_models.DescribeCloudPhoneNodesResponseBodyNodeModelBizTags()
                self.biz_tags.append(temp_model.from_map(k1))

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtExpired') is not None:
            self.gmt_expired = m.get('GmtExpired')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        self.network_infos = []
        if m.get('NetworkInfos') is not None:
            for k1 in m.get('NetworkInfos'):
                temp_model = main_models.DescribeCloudPhoneNodesResponseBodyNodeModelNetworkInfos()
                self.network_infos.append(temp_model.from_map(k1))

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('PhoneCount') is not None:
            self.phone_count = m.get('PhoneCount')

        if m.get('PhoneDataInfo') is not None:
            temp_model = main_models.DescribeCloudPhoneNodesResponseBodyNodeModelPhoneDataInfo()
            self.phone_data_info = temp_model.from_map(m.get('PhoneDataInfo'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')

        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')

        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')

        if m.get('ShareDataVolume') is not None:
            self.share_data_volume = m.get('ShareDataVolume')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SwapSize') is not None:
            self.swap_size = m.get('SwapSize')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeCloudPhoneNodesResponseBodyNodeModelPhoneDataInfo(DaraModel):
    def __init__(
        self,
        phone_data_id: str = None,
        phone_data_volume: int = None,
    ):
        self.phone_data_id = phone_data_id
        self.phone_data_volume = phone_data_volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.phone_data_id is not None:
            result['PhoneDataId'] = self.phone_data_id

        if self.phone_data_volume is not None:
            result['PhoneDataVolume'] = self.phone_data_volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneDataId') is not None:
            self.phone_data_id = m.get('PhoneDataId')

        if m.get('PhoneDataVolume') is not None:
            self.phone_data_volume = m.get('PhoneDataVolume')

        return self

class DescribeCloudPhoneNodesResponseBodyNodeModelNetworkInfos(DaraModel):
    def __init__(
        self,
        bandwidth_package_id: str = None,
        bandwidth_package_type: str = None,
        network_id: str = None,
        network_type: str = None,
        v_switch_id: str = None,
    ):
        self.bandwidth_package_id = bandwidth_package_id
        self.bandwidth_package_type = bandwidth_package_type
        self.network_id = network_id
        self.network_type = network_type
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.bandwidth_package_type is not None:
            result['BandwidthPackageType'] = self.bandwidth_package_type

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('BandwidthPackageType') is not None:
            self.bandwidth_package_type = m.get('BandwidthPackageType')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeCloudPhoneNodesResponseBodyNodeModelBizTags(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

