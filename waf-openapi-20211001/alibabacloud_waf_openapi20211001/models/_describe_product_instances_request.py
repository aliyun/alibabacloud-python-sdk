# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeProductInstancesRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_user_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_domain: str = None,
        resource_instance_access_status: str = None,
        resource_instance_id: str = None,
        resource_instance_ip: str = None,
        resource_instance_name: str = None,
        resource_ip: str = None,
        resource_manager_resource_group_id: str = None,
        resource_name: str = None,
        resource_product: str = None,
        resource_region_id: str = None,
    ):
        # Instance ID of the WAF instance.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query instance ID of the current WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The UID of the resource ownership user.
        self.owner_user_id = owner_user_id
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page when paging. Default value: **10**.
        self.page_size = page_size
        # The region where the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The domain name that is added to WAF.
        # > This parameter is supported only when the cloud service type is ddos.
        self.resource_domain = resource_domain
        # The WAF protection status.
        self.resource_instance_access_status = resource_instance_access_status
        # The instance ID of the cloud service.
        self.resource_instance_id = resource_instance_id
        # The IP address of the instance that is added to WAF.
        self.resource_instance_ip = resource_instance_ip
        # The name of the instance that is added to WAF.
        self.resource_instance_name = resource_instance_name
        # The public IP address of the cloud service.
        self.resource_ip = resource_ip
        # The Alibaba Cloud resource group ID.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The instance name of the cloud service.
        self.resource_name = resource_name
        # The type of the cloud service. Valid values:
        # 
        # - **clb4**: Layer 4 CLB.
        # 
        # - **clb7**: Layer 7 CLB.
        # 
        # - **ecs**: ECS.
        # - **nlb**: NLB.
        # - **ddos**: Anti-DDoS.
        self.resource_product = resource_product
        # The region ID of the cloud service. Valid values:
        # - **cn-chengdu**: China Southwest 1 (Chengdu).
        # 
        # - **cn-beijing**: China North 2 (Beijing).
        # 
        # - **cn-zhangjiakou**: China North 3 (Zhangjiakou).
        # 
        # - **cn-hangzhou**: China East 1 (Hangzhou).
        # 
        # - **cn-shanghai**: China East 2 (Shanghai).
        # 
        # - **cn-shenzhen**: China South 1 (Shenzhen).
        # 
        # - **cn-qingdao**: China North 1 (Qingdao).
        # 
        # - **cn-hongkong**: Hong Kong (China).
        # 
        # - **ap-southeast-3**: Malaysia (Kuala Lumpur).
        # 
        # - **ap-southeast-5**: Indonesia (Jakarta).
        self.resource_region_id = resource_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_domain is not None:
            result['ResourceDomain'] = self.resource_domain

        if self.resource_instance_access_status is not None:
            result['ResourceInstanceAccessStatus'] = self.resource_instance_access_status

        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id

        if self.resource_instance_ip is not None:
            result['ResourceInstanceIp'] = self.resource_instance_ip

        if self.resource_instance_name is not None:
            result['ResourceInstanceName'] = self.resource_instance_name

        if self.resource_ip is not None:
            result['ResourceIp'] = self.resource_ip

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_product is not None:
            result['ResourceProduct'] = self.resource_product

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceDomain') is not None:
            self.resource_domain = m.get('ResourceDomain')

        if m.get('ResourceInstanceAccessStatus') is not None:
            self.resource_instance_access_status = m.get('ResourceInstanceAccessStatus')

        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')

        if m.get('ResourceInstanceIp') is not None:
            self.resource_instance_ip = m.get('ResourceInstanceIp')

        if m.get('ResourceInstanceName') is not None:
            self.resource_instance_name = m.get('ResourceInstanceName')

        if m.get('ResourceIp') is not None:
            self.resource_ip = m.get('ResourceIp')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceProduct') is not None:
            self.resource_product = m.get('ResourceProduct')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        return self

