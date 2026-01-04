# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomerGatewaysResponseBody(DaraModel):
    def __init__(
        self,
        customer_gateways: main_models.DescribeCustomerGatewaysResponseBodyCustomerGateways = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about customer gateways.
        self.customer_gateways = customer_gateways
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.customer_gateways:
            self.customer_gateways.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_gateways is not None:
            result['CustomerGateways'] = self.customer_gateways.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerGateways') is not None:
            temp_model = main_models.DescribeCustomerGatewaysResponseBodyCustomerGateways()
            self.customer_gateways = temp_model.from_map(m.get('CustomerGateways'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCustomerGatewaysResponseBodyCustomerGateways(DaraModel):
    def __init__(
        self,
        customer_gateway: List[main_models.DescribeCustomerGatewaysResponseBodyCustomerGatewaysCustomerGateway] = None,
    ):
        self.customer_gateway = customer_gateway

    def validate(self):
        if self.customer_gateway:
            for v1 in self.customer_gateway:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomerGateway'] = []
        if self.customer_gateway is not None:
            for k1 in self.customer_gateway:
                result['CustomerGateway'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.customer_gateway = []
        if m.get('CustomerGateway') is not None:
            for k1 in m.get('CustomerGateway'):
                temp_model = main_models.DescribeCustomerGatewaysResponseBodyCustomerGatewaysCustomerGateway()
                self.customer_gateway.append(temp_model.from_map(k1))

        return self

class DescribeCustomerGatewaysResponseBodyCustomerGatewaysCustomerGateway(DaraModel):
    def __init__(
        self,
        asn: int = None,
        auth_key: str = None,
        create_time: int = None,
        customer_gateway_id: str = None,
        description: str = None,
        ip_address: str = None,
        name: str = None,
        resource_group_id: str = None,
        tags: main_models.DescribeCustomerGatewaysResponseBodyCustomerGatewaysCustomerGatewayTags = None,
    ):
        # The autonomous system number (ASN) of the gateway device in the data center.
        self.asn = asn
        # The authentication key that is used to connect to the gateway device in the data center by using Border Gateway Protocol (BGP).
        self.auth_key = auth_key
        # The time when the customer gateway was created. Unit: millisecond.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The customer gateway ID.
        self.customer_gateway_id = customer_gateway_id
        # The description of the customer gateway.
        self.description = description
        # The IP address of the gateway device in the data center.
        self.ip_address = ip_address
        # The name of the customer gateway.
        self.name = name
        # The ID of the resource group to which the customer gateway belongs.
        # 
        # You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to query resource groups.
        self.resource_group_id = resource_group_id
        # The tags that are added to the customer gateway.
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asn is not None:
            result['Asn'] = self.asn

        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.customer_gateway_id is not None:
            result['CustomerGatewayId'] = self.customer_gateway_id

        if self.description is not None:
            result['Description'] = self.description

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.name is not None:
            result['Name'] = self.name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Asn') is not None:
            self.asn = m.get('Asn')

        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CustomerGatewayId') is not None:
            self.customer_gateway_id = m.get('CustomerGatewayId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeCustomerGatewaysResponseBodyCustomerGatewaysCustomerGatewayTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeCustomerGatewaysResponseBodyCustomerGatewaysCustomerGatewayTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeCustomerGatewaysResponseBodyCustomerGatewaysCustomerGatewayTagsTag] = None,
    ):
        self.tag = tag

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
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeCustomerGatewaysResponseBodyCustomerGatewaysCustomerGatewayTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeCustomerGatewaysResponseBodyCustomerGatewaysCustomerGatewayTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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

