# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeInstancesRequest(DaraModel):
    def __init__(
        self,
        eip_addresses: List[str] = None,
        ens_region_id: str = None,
        ens_region_ids: str = None,
        ens_service_id: str = None,
        image_id: str = None,
        instance_id: str = None,
        instance_ids: str = None,
        instance_name: str = None,
        instance_resource_type: str = None,
        instance_type: str = None,
        intranet_ip: str = None,
        network_id: str = None,
        order_by_params: str = None,
        page_number: int = None,
        page_size: str = None,
        search_key: str = None,
        security_group_id: str = None,
        service_status: List[str] = None,
        status: str = None,
        tags: List[main_models.DescribeInstancesRequestTags] = None,
        v_switch_id: str = None,
    ):
        self.eip_addresses = eip_addresses
        # The region ID.
        self.ens_region_id = ens_region_id
        # The IDs of the regions. The value is a JSON array that consists of up to 100 IDs. Separate multiple IDs with commas (,).
        self.ens_region_ids = ens_region_ids
        # The ID of the edge service. You can use the ID to query information about the instances that are created in the edge service.
        self.ens_service_id = ens_service_id
        # The ID of the image.
        self.image_id = image_id
        # The ID of the instance.
        self.instance_id = instance_id
        # The IDs of the instances. The value is a JSON array that consists of up to 100 IDs. Separate IDs with commas (,).
        self.instance_ids = instance_ids
        # The name of the instance.
        self.instance_name = instance_name
        # The condition that you want to use to filter instances by category. Valid values:
        # 
        # *   EnsInstance: ENS instances that you purchase.
        # *   EnsService: ENS instances that belong to edge services.
        # *   BuildMachine: ENS instances that are configured with image builders.
        # *   EnsPostPaidInstance: Pay-as-you-go ENS instances that you purchase.
        self.instance_resource_type = instance_resource_type
        # The instance type.
        self.instance_type = instance_type
        # The internal IP address of the instance.
        self.intranet_ip = intranet_ip
        # The ID of the network.
        self.network_id = network_id
        # The method that you want to use to sort instances. The value of this parameter is in the JSON format.
        # 
        # You can sort instances by name, expiration time, node ID, or creation time. You can specify one or more methods.
        self.order_by_params = order_by_params
        # The page number. Pages start from page **1**.
        # 
        # Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. The maximum value is **100**.
        # 
        # Default value: **10**.
        self.page_size = page_size
        # The keyword that you use to query the logs of the service. You can specify the values of parameters such as **ip**, **InstanceName**, and **InstanceId** as the keyword.
        self.search_key = search_key
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The status of the service. Valid values.
        self.service_status = service_status
        # The status of the instance. Valid values:
        # 
        # *   Running
        # *   Stopped
        # *   Expired
        self.status = status
        # The tags that are added to the resource. This operation does not return tag information. You can call this operation in combination with the tag-related operations.
        self.tags = tags
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip_addresses is not None:
            result['EipAddresses'] = self.eip_addresses

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.ens_region_ids is not None:
            result['EnsRegionIds'] = self.ens_region_ids

        if self.ens_service_id is not None:
            result['EnsServiceId'] = self.ens_service_id

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_resource_type is not None:
            result['InstanceResourceType'] = self.instance_resource_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.order_by_params is not None:
            result['OrderByParams'] = self.order_by_params

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipAddresses') is not None:
            self.eip_addresses = m.get('EipAddresses')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('EnsRegionIds') is not None:
            self.ens_region_ids = m.get('EnsRegionIds')

        if m.get('EnsServiceId') is not None:
            self.ens_service_id = m.get('EnsServiceId')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceResourceType') is not None:
            self.instance_resource_type = m.get('InstanceResourceType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('OrderByParams') is not None:
            self.order_by_params = m.get('OrderByParams')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeInstancesRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeInstancesRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag that are to add to the instance. Valid values: 1 to 20.
        self.key = key
        # The tag value of the instance. Valid values: 1 to 20.
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

