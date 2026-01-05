# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class ListLoadBalancersRequest(DaraModel):
    def __init__(
        self,
        address_ip_version: str = None,
        address_type: str = None,
        dnsname: str = None,
        ipv_6address_type: str = None,
        load_balancer_bussiness_status: str = None,
        load_balancer_ids: List[str] = None,
        load_balancer_names: List[str] = None,
        load_balancer_status: str = None,
        max_results: int = None,
        next_token: str = None,
        pay_type: str = None,
        resource_group_id: str = None,
        tag: List[main_models.ListLoadBalancersRequestTag] = None,
        vpc_ids: List[str] = None,
        zone_id: str = None,
    ):
        # The IP version. Valid values:
        # 
        # *   **IPv4**
        # *   **DualStack**
        self.address_ip_version = address_ip_version
        # The network type. Valid values:
        # 
        # *   **Internet**: The ALB instance uses a public IP address. The domain name of the ALB instance is resolved to the public IP address. Therefore, the ALB instance can be accessed over the Internet.
        # *   **Intranet**: The ALB instance uses a private IP address. The domain name of the ALB instance is resolved to the private IP address. In this case, the ALB instance can be accessed over the VPC where the ALB instance is deployed.
        self.address_type = address_type
        # The domain name.
        self.dnsname = dnsname
        # The type of IPv6 address that is used by the ALB instance. Valid values:
        # 
        # *   **Internet**: The ALB instance uses a public IP address. The domain name of the ALB instance is resolved to the public IP address. Therefore, the ALB instance can be accessed over the Internet.
        # *   **Intranet**: The ALB instance uses a private IP address. The domain name of the ALB instance is resolved to the private IP address. Therefore, the ALB instance can be accessed over the VPC in which the ALB instance is deployed.
        self.ipv_6address_type = ipv_6address_type
        # The service status of the ALB instance. Valid values:
        # 
        # *   **Abnormal**
        # *   **Normal**
        self.load_balancer_bussiness_status = load_balancer_bussiness_status
        # The instance IDs. You can specify at most 20 ALB instance IDs.
        self.load_balancer_ids = load_balancer_ids
        # The instance names. You can specify at most 10 instance names.
        self.load_balancer_names = load_balancer_names
        # The status of the ALB instance. Valid values:
        # 
        # *   **Inactive**: The ALB instance is disabled. The listeners do not forward traffic.
        # *   **Active**: The ALB instance is running.
        # *   **Provisioning**: The ALB instance is being created.
        # *   **Configuring**: The ALB instance is being modified.
        # *   **CreateFailed**: The system failed to create the ALB instance. In this case, you are not charged for the ALB instance. You can only delete the ALB instance. By default, the system deletes the ALB instances that are in the CreateFailed state within the last day.
        self.load_balancer_status = load_balancer_status
        # The number of entries to return on each page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of **NextToken**.
        self.next_token = next_token
        # The billing method of the ALB instance. Set the value to
        # 
        # **PostPay**, which specifies the pay-as-you-go billing method. This is the default value.
        self.pay_type = pay_type
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags added to the ALB instance.
        self.tag = tag
        # The ID of the VPC to which the ALB instance belongs. You can specify at most 10 VPC IDs.
        self.vpc_ids = vpc_ids
        # The ID of the zone where the ALB instance is deployed.
        # 
        # You can call the [DescribeZones](https://help.aliyun.com/document_detail/189196.html) operation to query zones.
        self.zone_id = zone_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_ip_version is not None:
            result['AddressIpVersion'] = self.address_ip_version

        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.dnsname is not None:
            result['DNSName'] = self.dnsname

        if self.ipv_6address_type is not None:
            result['Ipv6AddressType'] = self.ipv_6address_type

        if self.load_balancer_bussiness_status is not None:
            result['LoadBalancerBussinessStatus'] = self.load_balancer_bussiness_status

        if self.load_balancer_ids is not None:
            result['LoadBalancerIds'] = self.load_balancer_ids

        if self.load_balancer_names is not None:
            result['LoadBalancerNames'] = self.load_balancer_names

        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vpc_ids is not None:
            result['VpcIds'] = self.vpc_ids

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')

        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('DNSName') is not None:
            self.dnsname = m.get('DNSName')

        if m.get('Ipv6AddressType') is not None:
            self.ipv_6address_type = m.get('Ipv6AddressType')

        if m.get('LoadBalancerBussinessStatus') is not None:
            self.load_balancer_bussiness_status = m.get('LoadBalancerBussinessStatus')

        if m.get('LoadBalancerIds') is not None:
            self.load_balancer_ids = m.get('LoadBalancerIds')

        if m.get('LoadBalancerNames') is not None:
            self.load_balancer_names = m.get('LoadBalancerNames')

        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListLoadBalancersRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VpcIds') is not None:
            self.vpc_ids = m.get('VpcIds')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ListLoadBalancersRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can specify at most 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        self.key = key
        # The tag value. You can specify at most 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
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

