# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AllocateAnycastEipAddressRequestTag(TeaModel):
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


class AllocateAnycastEipAddressRequest(TeaModel):
    def __init__(
        self,
        bandwidth: str = None,
        client_token: str = None,
        description: str = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
        name: str = None,
        resource_group_id: str = None,
        service_location: str = None,
        tag: List[AllocateAnycastEipAddressRequestTag] = None,
    ):
        # The maximum bandwidth of the Anycast EIP. Unit: Mbit/s.
        # 
        # Valid values: **200** to **1000**.
        # 
        # Default value: **1000**.
        # 
        # > The maximum bandwidth is not a guaranteed service and is for reference only.
        self.bandwidth = bandwidth
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The description of the Anycast EIP.
        # 
        # The description must be 0 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The billing method of the Anycast EIP.
        # 
        # Set the value to **PostPaid**, which specifies the pay-as-you-go billing method.
        self.instance_charge_type = instance_charge_type
        # The metering method of the Anycast EIP.
        # 
        # Set the value to **PayByTraffic**, which specifies the pay-by-data-transfer metering method.
        self.internet_charge_type = internet_charge_type
        # The name of the Anycast EIP.
        # 
        # The name must be 0 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter.
        self.name = name
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The access area of the Anycast EIP.
        # 
        # Set the value to **international**, which specifies the areas outside the Chinese mainland.
        # 
        # This parameter is required.
        self.service_location = service_location
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
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = AllocateAnycastEipAddressRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class AllocateAnycastEipAddressResponseBody(TeaModel):
    def __init__(
        self,
        anycast_id: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # The ID of the Anycast EIP.
        self.anycast_id = anycast_id
        # The order ID.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AllocateAnycastEipAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AllocateAnycastEipAddressResponseBody = None,
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
            temp_model = AllocateAnycastEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateAnycastEipAddressRequestPopLocations(TeaModel):
    def __init__(
        self,
        pop_location: str = None,
    ):
        # The information about the access points in associated access areas when you associate an Anycast EIP with an endpoint.
        # 
        # If this is your first time to associate an Anycast EIP with an endpoint, ignore this parameter. The system automatically associates all access areas.
        # 
        # You can call the [DescribeAnycastPopLocations](https://help.aliyun.com/document_detail/171938.html) operation to query information about access points in supported access areas.
        self.pop_location = pop_location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pop_location is not None:
            result['PopLocation'] = self.pop_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PopLocation') is not None:
            self.pop_location = m.get('PopLocation')
        return self


class AssociateAnycastEipAddressRequest(TeaModel):
    def __init__(
        self,
        anycast_id: str = None,
        association_mode: str = None,
        bind_instance_id: str = None,
        bind_instance_region_id: str = None,
        bind_instance_type: str = None,
        client_token: str = None,
        dry_run: bool = None,
        pop_locations: List[AssociateAnycastEipAddressRequestPopLocations] = None,
        private_ip_address: str = None,
    ):
        # The ID of the Anycast EIP.
        # 
        # This parameter is required.
        self.anycast_id = anycast_id
        # The association mode. Valid values:
        # 
        # *   **Default**: the default mode. In this mode, the endpoint to be associated serves as the default origin server.
        # *   **Normal**: the standard mode. In this mode, the endpoint to be associated serves as a standard origin server.
        # 
        # > You can associate endpoints in multiple regions with an Anycast EIP. However, only one endpoint can serve as the default origin server. Others serve as standard origin servers. If you do not specify or add an access point, requests are forwarded to the default origin server.\\
        # 
        # 
        # *   If this is your first time to associate an Anycast EIP with an endpoint, set the value to **Default**.
        # *   If not, you can also set the value to **Default**, which specifies a new default origin server. In this case, the previous origin server functions as a standard origin server.
        self.association_mode = association_mode
        # The ID of the endpoint with which you want to associate the Anycast EIP.
        # 
        # This parameter is required.
        self.bind_instance_id = bind_instance_id
        # The ID of the region where the endpoint is deployed.
        # 
        # You can associate Anycast EIPs only with endpoints in specific regions. You can call the [DescribeAnycastServerRegions](https://help.aliyun.com/document_detail/171939.html) operation to query the region IDs.
        # 
        # This parameter is required.
        self.bind_instance_region_id = bind_instance_region_id
        # The type of endpoint with which you want to associate the Anycast EIP. Valid values:
        # 
        # *   **SlbInstance**: internal-facing Server Load Balancer (SLB) instance that is deployed in a virtual private cloud (VPC)
        # *   **NetworkInterface**: elastic network interface (ENI)
        # 
        # This parameter is required.
        self.bind_instance_type = bind_instance_type
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**(default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The information about the access points in associated access areas when you associate an Anycast EIP with an endpoint.
        # 
        # If this is your first time to associate an Anycast EIP with an endpoint, ignore this parameter. The system automatically associates all access areas.
        # 
        # You can call the [DescribeAnycastPopLocations](https://help.aliyun.com/document_detail/171938.html) operation to query information about access points in supported access areas.
        self.pop_locations = pop_locations
        # The secondary private IP address of the ENI with which you want to associate the Anycast EIP.
        # 
        # This parameter is valid only when you set **BindInstanceType** to **NetworkInterface**. If you do not set this parameter, the primary private IP address of the ENI is used.
        self.private_ip_address = private_ip_address

    def validate(self):
        if self.pop_locations:
            for k in self.pop_locations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.association_mode is not None:
            result['AssociationMode'] = self.association_mode
        if self.bind_instance_id is not None:
            result['BindInstanceId'] = self.bind_instance_id
        if self.bind_instance_region_id is not None:
            result['BindInstanceRegionId'] = self.bind_instance_region_id
        if self.bind_instance_type is not None:
            result['BindInstanceType'] = self.bind_instance_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        result['PopLocations'] = []
        if self.pop_locations is not None:
            for k in self.pop_locations:
                result['PopLocations'].append(k.to_map() if k else None)
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('AssociationMode') is not None:
            self.association_mode = m.get('AssociationMode')
        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')
        if m.get('BindInstanceRegionId') is not None:
            self.bind_instance_region_id = m.get('BindInstanceRegionId')
        if m.get('BindInstanceType') is not None:
            self.bind_instance_type = m.get('BindInstanceType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        self.pop_locations = []
        if m.get('PopLocations') is not None:
            for k in m.get('PopLocations'):
                temp_model = AssociateAnycastEipAddressRequestPopLocations()
                self.pop_locations.append(temp_model.from_map(k))
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        return self


class AssociateAnycastEipAddressResponseBody(TeaModel):
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


class AssociateAnycastEipAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssociateAnycastEipAddressResponseBody = None,
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
            temp_model = AssociateAnycastEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        new_resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the resource group to which you want to move the resource.
        # > You can use resource groups to facilitate resource grouping and permission management for an Alibaba Cloud. For more information, see [What is resource management?](https://help.aliyun.com/document_detail/158855.html)
        # 
        # This parameter is required.
        self.new_resource_group_id = new_resource_group_id
        # The resource ID.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource for which you want to modify the resource group. Valid value: **ANYCASTEIPADDRESS**.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
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


class ChangeResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeResourceGroupResponseBody = None,
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
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAnycastEipAddressRequest(TeaModel):
    def __init__(
        self,
        anycast_id: str = None,
        bind_instance_id: str = None,
        ip: str = None,
    ):
        # The ID of the Anycast EIP.
        # 
        # > You must specify **Ip** or **AnycastId**.
        self.anycast_id = anycast_id
        # The ID of the endpoint with which the Anycast EIP is associated.
        self.bind_instance_id = bind_instance_id
        # The IP address of the Anycast EIP.
        # 
        # > You must specify **Ip** or **AnycastId**.
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.bind_instance_id is not None:
            result['BindInstanceId'] = self.bind_instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoListPopLocations(TeaModel):
    def __init__(
        self,
        pop_location: str = None,
    ):
        # The information about the access points in associated access areas when you associate an Anycast EIP with a cloud resource.
        # 
        # If this is your first time associating an Anycast EIP with an endpoint, the system returns information about access points in all access areas.
        self.pop_location = pop_location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pop_location is not None:
            result['PopLocation'] = self.pop_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PopLocation') is not None:
            self.pop_location = m.get('PopLocation')
        return self


class DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoList(TeaModel):
    def __init__(
        self,
        association_mode: str = None,
        bind_instance_id: str = None,
        bind_instance_region_id: str = None,
        bind_instance_type: str = None,
        bind_time: str = None,
        pop_locations: List[DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoListPopLocations] = None,
        private_ip_address: str = None,
        status: str = None,
    ):
        # The association mode. Valid values:
        # 
        # *   **Default**: the default mode. In this mode, the associated endpoint serves as the default origin server.
        # *   **Normal**: the standard mode. In this mode, the associated endpoint serves as a standard origin server.
        self.association_mode = association_mode
        # The ID of the endpoint with which the Anycast EIP is associated.
        self.bind_instance_id = bind_instance_id
        # The ID of the region in which the endpoint is deployed.
        self.bind_instance_region_id = bind_instance_region_id
        # The type of endpoint with which the Anycast EIP is associated. Valid values:
        # 
        # *   **SlbInstance**: a CLB instance in a VPC.
        # *   **NetworkInterface**: an elastic network interface (ENI).
        self.bind_instance_type = bind_instance_type
        # The time when the Anycast EIP was associated.
        # 
        # The time follows the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format. The time is displayed in UTC.
        self.bind_time = bind_time
        # The information about the access points in associated access areas when you associate an Anycast EIP with a cloud resource.
        # 
        # If this is your first time associating an Anycast EIP with an endpoint, the system returns information about access points in all access areas.
        self.pop_locations = pop_locations
        # The secondary private IP address of the associated ENI.
        # 
        # This parameter is valid only when **BindInstanceType** is set to **NetworkInterface**.
        self.private_ip_address = private_ip_address
        # The status of the endpoint. Valid values:
        # 
        # *   **BINDING**\
        # *   **BINDED**\
        # *   **UNBINDING**\
        # *   **DELETED**\
        # *   **MODIFYING**\
        self.status = status

    def validate(self):
        if self.pop_locations:
            for k in self.pop_locations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.association_mode is not None:
            result['AssociationMode'] = self.association_mode
        if self.bind_instance_id is not None:
            result['BindInstanceId'] = self.bind_instance_id
        if self.bind_instance_region_id is not None:
            result['BindInstanceRegionId'] = self.bind_instance_region_id
        if self.bind_instance_type is not None:
            result['BindInstanceType'] = self.bind_instance_type
        if self.bind_time is not None:
            result['BindTime'] = self.bind_time
        result['PopLocations'] = []
        if self.pop_locations is not None:
            for k in self.pop_locations:
                result['PopLocations'].append(k.to_map() if k else None)
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationMode') is not None:
            self.association_mode = m.get('AssociationMode')
        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')
        if m.get('BindInstanceRegionId') is not None:
            self.bind_instance_region_id = m.get('BindInstanceRegionId')
        if m.get('BindInstanceType') is not None:
            self.bind_instance_type = m.get('BindInstanceType')
        if m.get('BindTime') is not None:
            self.bind_time = m.get('BindTime')
        self.pop_locations = []
        if m.get('PopLocations') is not None:
            for k in m.get('PopLocations'):
                temp_model = DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoListPopLocations()
                self.pop_locations.append(temp_model.from_map(k))
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAnycastEipAddressResponseBodyTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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


class DescribeAnycastEipAddressResponseBody(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        anycast_eip_bind_info_list: List[DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoList] = None,
        anycast_id: str = None,
        bandwidth: int = None,
        bid: str = None,
        business_status: str = None,
        create_time: str = None,
        description: str = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
        ip_address: str = None,
        name: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        service_location: str = None,
        service_managed: int = None,
        status: str = None,
        tags: List[DescribeAnycastEipAddressResponseBodyTags] = None,
    ):
        # The ID of the account to which the Anycast EIP belongs.
        self.ali_uid = ali_uid
        # The information about the endpoint with which the Anycast EIP is associated.
        self.anycast_eip_bind_info_list = anycast_eip_bind_info_list
        # The ID of the Anycast EIP.
        self.anycast_id = anycast_id
        # The maximum bandwidth of the Anycast EIP. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The BID of the account to which the Anycast EIP belongs.
        self.bid = bid
        # The status of the Anycast EIP. Valid values:
        # 
        # *   **Normal**: running as expected
        # *   **FinancialLocked**: locked due to overdue payments
        # *   **RiskExpired**: locked due to security reasons.
        self.business_status = business_status
        # The point in time at which the Anycast EIP was created.
        # 
        # The time follows the ISO8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the Anycast EIP.
        self.description = description
        # The billing method of the Anycast EIP.
        # 
        # Only **PostPaid** may be returned, which indicates the pay-as-you-go billing method.
        self.instance_charge_type = instance_charge_type
        # The metering method of the Anycast EIP.
        # 
        # Only **PayByTraffic** may be returned, which indicates the pay-by-data-transfer metering method.
        self.internet_charge_type = internet_charge_type
        # The IP address of the Anycast EIP.
        self.ip_address = ip_address
        # The name of the Anycast EIP.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The access area of the Anycast EIP.
        # 
        # Only **international** may be returned, which indicates the areas outside the Chinese mainland.
        self.service_location = service_location
        # Indicates whether the instance is managed. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no.
        self.service_managed = service_managed
        # The status of the Anycast EIP.
        # 
        # *   **Associating**\
        # *   **Unassociating**\
        # *   **Allocated**\
        # *   **Associated**\
        # *   **Modifying**\
        # *   **Releasing**\
        # *   **Released**\
        self.status = status
        # The information about the tags.
        self.tags = tags

    def validate(self):
        if self.anycast_eip_bind_info_list:
            for k in self.anycast_eip_bind_info_list:
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
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        result['AnycastEipBindInfoList'] = []
        if self.anycast_eip_bind_info_list is not None:
            for k in self.anycast_eip_bind_info_list:
                result['AnycastEipBindInfoList'].append(k.to_map() if k else None)
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location
        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        self.anycast_eip_bind_info_list = []
        if m.get('AnycastEipBindInfoList') is not None:
            for k in m.get('AnycastEipBindInfoList'):
                temp_model = DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoList()
                self.anycast_eip_bind_info_list.append(temp_model.from_map(k))
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')
        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeAnycastEipAddressResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeAnycastEipAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAnycastEipAddressResponseBody = None,
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
            temp_model = DescribeAnycastEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAnycastPopLocationsRequest(TeaModel):
    def __init__(
        self,
        service_location: str = None,
    ):
        # The access area of the Anycast elastic IP address (EIP).
        # 
        # Set the value to **international**, which specifies the areas outside the Chinese mainland.
        self.service_location = service_location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')
        return self


class DescribeAnycastPopLocationsResponseBodyAnycastPopLocationList(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        region_name: str = None,
    ):
        # The ID of the region where the access point is deployed.
        self.region_id = region_id
        # The name of the region where the access point is deployed.
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class DescribeAnycastPopLocationsResponseBody(TeaModel):
    def __init__(
        self,
        anycast_pop_location_list: List[DescribeAnycastPopLocationsResponseBodyAnycastPopLocationList] = None,
        count: str = None,
        request_id: str = None,
    ):
        # The list of access points in the specified access area.
        self.anycast_pop_location_list = anycast_pop_location_list
        # The number of access points.
        self.count = count
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.anycast_pop_location_list:
            for k in self.anycast_pop_location_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AnycastPopLocationList'] = []
        if self.anycast_pop_location_list is not None:
            for k in self.anycast_pop_location_list:
                result['AnycastPopLocationList'].append(k.to_map() if k else None)
        if self.count is not None:
            result['Count'] = self.count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.anycast_pop_location_list = []
        if m.get('AnycastPopLocationList') is not None:
            for k in m.get('AnycastPopLocationList'):
                temp_model = DescribeAnycastPopLocationsResponseBodyAnycastPopLocationList()
                self.anycast_pop_location_list.append(temp_model.from_map(k))
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAnycastPopLocationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAnycastPopLocationsResponseBody = None,
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
            temp_model = DescribeAnycastPopLocationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAnycastServerRegionsRequest(TeaModel):
    def __init__(
        self,
        service_location: str = None,
    ):
        # The access area from which you use the Anycast EIP to communicate with the Internet.
        # 
        # Set the value to **international**, which specifies the areas outside the Chinese mainland.
        # 
        # This parameter is required.
        self.service_location = service_location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')
        return self


class DescribeAnycastServerRegionsResponseBodyAnycastServerRegionList(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        region_name: str = None,
    ):
        # The ID of the region.
        self.region_id = region_id
        # The name of the region.
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class DescribeAnycastServerRegionsResponseBody(TeaModel):
    def __init__(
        self,
        anycast_server_region_list: List[DescribeAnycastServerRegionsResponseBodyAnycastServerRegionList] = None,
        count: str = None,
        request_id: str = None,
    ):
        # The list of regions where you can associate Anycast EIPs with endpoints.
        self.anycast_server_region_list = anycast_server_region_list
        # The number of returned entries.
        self.count = count
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.anycast_server_region_list:
            for k in self.anycast_server_region_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AnycastServerRegionList'] = []
        if self.anycast_server_region_list is not None:
            for k in self.anycast_server_region_list:
                result['AnycastServerRegionList'].append(k.to_map() if k else None)
        if self.count is not None:
            result['Count'] = self.count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.anycast_server_region_list = []
        if m.get('AnycastServerRegionList') is not None:
            for k in m.get('AnycastServerRegionList'):
                temp_model = DescribeAnycastServerRegionsResponseBodyAnycastServerRegionList()
                self.anycast_server_region_list.append(temp_model.from_map(k))
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAnycastServerRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAnycastServerRegionsResponseBody = None,
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
            temp_model = DescribeAnycastServerRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnycastEipAddressesRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You can specify up to 20 tag keys. You cannot specify empty strings as tag keys.
        # 
        # The key can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The key must start with a letter but cannot start with `aliyun` or `acs:`. The key cannot contain `http://` or `https://`.
        # 
        # >  You must specify at least one of **Tag.N** (**Tag.N.Key** and **Tag.N.Value**).
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values. It can be an empty string.
        # 
        # The value cannot exceed 128 characters in length and can contain digits, periods (.), underscores (_), and hyphens (-). The value must start with a letter but cannot start with `aliyun` or `acs:`. The value cannot contain `http://` or `https://`.
        # 
        # >  You must specify at least one of **Tag.N** (**Tag.N.Key** and **Tag.N.Value**).
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


class ListAnycastEipAddressesRequest(TeaModel):
    def __init__(
        self,
        anycast_eip_address: str = None,
        anycast_id: str = None,
        anycast_ids: List[str] = None,
        bind_instance_ids: List[str] = None,
        business_status: str = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        resource_group_id: str = None,
        service_location: str = None,
        status: str = None,
        tags: List[ListAnycastEipAddressesRequestTags] = None,
    ):
        # The IP address that is allocated to the Anycast EIP.
        self.anycast_eip_address = anycast_eip_address
        # The ID of the Anycast EIP.
        # 
        # >  To ensure the accuracy of the query result, we do not recommend that you specify **AnycastIds** and **AnycastId** at the same time.
        self.anycast_id = anycast_id
        # The IDs of Anycast EIPs.
        # 
        # You can enter at most 50 Anycast EIP IDs.
        # 
        # >  To ensure the accuracy of the query result, we do not recommend that you specify **AnycastIds** and **AnycastId** at the same time.
        self.anycast_ids = anycast_ids
        # The IDs of the cloud resources with which the Anycast EIPs are associated.
        # 
        # You can enter at most 100 cloud resource IDs.
        self.bind_instance_ids = bind_instance_ids
        # The service status of the Anycast EIP. Valid values:
        # 
        # *   **Normal**\
        # *   **FinancialLocked**\
        self.business_status = business_status
        # The billing method of the Anycast EIP.
        # 
        # Set the value to **PostPaid**, which specifies the pay-as-you-go billing method.
        self.instance_charge_type = instance_charge_type
        # The metering method of the Anycast EIP.
        # 
        # Set the value to **PayByTraffic**, which specifies the pay-by-data-transfer metering method.
        self.internet_charge_type = internet_charge_type
        # The number of entries to return on each page. Valid values: **20 to 100**. Default value: **50**.
        self.max_results = max_results
        # The name of the Anycast EIP.
        # 
        # The name must be 0 to 128 characters in length, and can contain digits, hyphens (-), and underscores (_). The name must start with a letter.
        self.name = name
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The access area of the Anycast EIP.
        # 
        # Set the value to **international**, which specifies the regions outside the Chinese mainland.
        self.service_location = service_location
        # The status of the Anycast EIP. Valid values:
        # 
        # *   **Associating**\
        # *   **Unassociating**\
        # *   **Allocated**\
        # *   **Associated**\
        # *   **Modifying**\
        # *   **Releasing**\
        # *   **Released**\
        self.status = status
        # The tags.
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
        if self.anycast_eip_address is not None:
            result['AnycastEipAddress'] = self.anycast_eip_address
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.anycast_ids is not None:
            result['AnycastIds'] = self.anycast_ids
        if self.bind_instance_ids is not None:
            result['BindInstanceIds'] = self.bind_instance_ids
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnycastEipAddress') is not None:
            self.anycast_eip_address = m.get('AnycastEipAddress')
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('AnycastIds') is not None:
            self.anycast_ids = m.get('AnycastIds')
        if m.get('BindInstanceIds') is not None:
            self.bind_instance_ids = m.get('BindInstanceIds')
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListAnycastEipAddressesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListAnycastEipAddressesResponseBodyAnycastListAnycastEipBindInfoList(TeaModel):
    def __init__(
        self,
        bind_instance_id: str = None,
        bind_instance_region_id: str = None,
        bind_instance_type: str = None,
        bind_time: str = None,
    ):
        # The ID of the cloud resource with which the Anycast EIP is associated.
        self.bind_instance_id = bind_instance_id
        # The ID of the region where the cloud resource is deployed.
        self.bind_instance_region_id = bind_instance_region_id
        # The type of cloud resource with which the Anycast EIP is associated.
        # 
        # *   **SlbInstance**: an internal-facing Classic Load Balancer (CLB) instance deployed in a virtual private cloud (VPC). CLB is formerly known as Server Load Balancer (SLB).
        # *   **NetworkInterface**: an elastic network interface (ENI).
        self.bind_instance_type = bind_instance_type
        # The time when the Anycast EIP was associated.
        self.bind_time = bind_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_instance_id is not None:
            result['BindInstanceId'] = self.bind_instance_id
        if self.bind_instance_region_id is not None:
            result['BindInstanceRegionId'] = self.bind_instance_region_id
        if self.bind_instance_type is not None:
            result['BindInstanceType'] = self.bind_instance_type
        if self.bind_time is not None:
            result['BindTime'] = self.bind_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')
        if m.get('BindInstanceRegionId') is not None:
            self.bind_instance_region_id = m.get('BindInstanceRegionId')
        if m.get('BindInstanceType') is not None:
            self.bind_instance_type = m.get('BindInstanceType')
        if m.get('BindTime') is not None:
            self.bind_time = m.get('BindTime')
        return self


class ListAnycastEipAddressesResponseBodyAnycastListTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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


class ListAnycastEipAddressesResponseBodyAnycastList(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        anycast_eip_bind_info_list: List[ListAnycastEipAddressesResponseBodyAnycastListAnycastEipBindInfoList] = None,
        anycast_id: str = None,
        bandwidth: int = None,
        business_status: str = None,
        create_time: str = None,
        description: str = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
        ip_address: str = None,
        name: str = None,
        resource_group_id: str = None,
        service_location: str = None,
        service_managed: int = None,
        status: str = None,
        tags: List[ListAnycastEipAddressesResponseBodyAnycastListTags] = None,
    ):
        # The ID of the account to which the Anycast EIP belongs.
        self.ali_uid = ali_uid
        # The list of cloud resources with which the Anycast EIPs are associated.
        self.anycast_eip_bind_info_list = anycast_eip_bind_info_list
        # The ID of the Anycast EIP.
        self.anycast_id = anycast_id
        # The maximum bandwidth of the Anycast EIP. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The service status of the Anycast EIP. Valid values:
        # 
        # *   **Normal**\
        # *   **FinancialLocked**\
        self.business_status = business_status
        # The time when the Anycast EIP was created.
        self.create_time = create_time
        # The description of the Anycast EIP.
        self.description = description
        # The billing method of the Anycast EIP.
        # 
        # **PostPaid**: pay-as-you-go
        self.instance_charge_type = instance_charge_type
        # The metering method of the Anycast EIP.
        # 
        # **PayByTraffic**: pay-by-data-transfer
        self.internet_charge_type = internet_charge_type
        # The IP address of the Anycast EIP.
        self.ip_address = ip_address
        # The name of the Anycast EIP.
        self.name = name
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The access area of the Anycast EIP.
        # 
        # **international**: regions outside the Chinese mainland
        self.service_location = service_location
        # Indicates whether the resource is created by the service account.
        # 
        # *   **0**: no
        # *   **1**: yes
        self.service_managed = service_managed
        # The status of the Anycast EIP.
        # 
        # *   **Associating**\
        # *   **Unassociating**\
        # *   **Allocated**\
        # *   **Associated**\
        # *   **Modifying**\
        # *   **Releasing**\
        # *   **Released**\
        self.status = status
        # The information about the tags.
        self.tags = tags

    def validate(self):
        if self.anycast_eip_bind_info_list:
            for k in self.anycast_eip_bind_info_list:
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
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        result['AnycastEipBindInfoList'] = []
        if self.anycast_eip_bind_info_list is not None:
            for k in self.anycast_eip_bind_info_list:
                result['AnycastEipBindInfoList'].append(k.to_map() if k else None)
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location
        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        self.anycast_eip_bind_info_list = []
        if m.get('AnycastEipBindInfoList') is not None:
            for k in m.get('AnycastEipBindInfoList'):
                temp_model = ListAnycastEipAddressesResponseBodyAnycastListAnycastEipBindInfoList()
                self.anycast_eip_bind_info_list.append(temp_model.from_map(k))
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')
        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListAnycastEipAddressesResponseBodyAnycastListTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListAnycastEipAddressesResponseBody(TeaModel):
    def __init__(
        self,
        anycast_list: List[ListAnycastEipAddressesResponseBodyAnycastList] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of Anycast EIPs.
        self.anycast_list = anycast_list
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If **NextToken** is not empty, the value of NextToken can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.anycast_list:
            for k in self.anycast_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AnycastList'] = []
        if self.anycast_list is not None:
            for k in self.anycast_list:
                result['AnycastList'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.anycast_list = []
        if m.get('AnycastList') is not None:
            for k in m.get('AnycastList'):
                temp_model = ListAnycastEipAddressesResponseBodyAnycastList()
                self.anycast_list.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAnycastEipAddressesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAnycastEipAddressesResponseBody = None,
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
            temp_model = ListAnycastEipAddressesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be a up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        # 
        # > You must specify **ResourceId.N** or **Tag.N** (**Tag.N.Key** or **Tag.N.Value**).
        self.key = key
        # The value of tag N. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # It can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        # 
        # > You must specify **ResourceId.N** or **Tag.N** (**Tag.N.Key** or **Tag.N.Value**).
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # The number of entries per page. Valid values: **1** to **50**. Default value: **50**.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If this is your first query or no next queries are to be sent, ignore this parameter.
        # *   You must specify the token that is obtained from the previous query as the value of **NextToken**.
        self.next_token = next_token
        # The resource IDs.
        self.resource_id = resource_id
        # The resource type. Set the value to **ANYCASTEIPADDRESS**.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag information.
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The resource ID.
        self.resource_id = resource_id
        # The resource type. Only **ANYCASTEIPADDRESS** may be returned.
        self.resource_type = resource_type
        # The key of tag N.
        self.tag_key = tag_key
        # The value of tag N.
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


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value is returned for **NextToken**, the value is the token that determines the start point of the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The resources to which the tags are added.
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAnycastEipAddressAttributeRequest(TeaModel):
    def __init__(
        self,
        anycast_id: str = None,
        description: str = None,
        name: str = None,
    ):
        # The ID of the Anycast EIP.
        # 
        # This parameter is required.
        self.anycast_id = anycast_id
        # The description of the Anycast EIP.
        # 
        # The description must be 0 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The name of the Anycast EIP.
        # 
        # The name must be 0 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ModifyAnycastEipAddressAttributeResponseBody(TeaModel):
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


class ModifyAnycastEipAddressAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAnycastEipAddressAttributeResponseBody = None,
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
            temp_model = ModifyAnycastEipAddressAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAnycastEipAddressSpecRequest(TeaModel):
    def __init__(
        self,
        anycast_id: str = None,
        bandwidth: str = None,
    ):
        # The ID of the Anycast EIP.
        # 
        # This parameter is required.
        self.anycast_id = anycast_id
        # The maximum bandwidth of the Anycast EIP. Unit: Mbit/s.
        # 
        # Valid values: **200** to **1000**.
        # 
        # This parameter is required.
        self.bandwidth = bandwidth

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        return self


class ModifyAnycastEipAddressSpecResponseBody(TeaModel):
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


class ModifyAnycastEipAddressSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAnycastEipAddressSpecResponseBody = None,
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
            temp_model = ModifyAnycastEipAddressSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseAnycastEipAddressRequest(TeaModel):
    def __init__(
        self,
        anycast_id: str = None,
        client_token: str = None,
    ):
        # The ID of the Anycast EIP to be released.
        # 
        # This parameter is required.
        self.anycast_id = anycast_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ReleaseAnycastEipAddressResponseBody(TeaModel):
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


class ReleaseAnycastEipAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseAnycastEipAddressResponseBody = None,
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
            temp_model = ReleaseAnycastEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N to add to the resource. You must enter at least one tag key and at most 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 128 characters in length and cannot start with acs: or aliyun. It cannot contain `http://` or `https://`.
        # 
        # > When you call this operation, **Tag.N.Key** is required.
        self.key = key
        # The value of tag N to add to the resource. You must enter at least one tag value and at most 20 tag values. The tag value can be an empty string.
        # 
        # It can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        # 
        # > When you call this operation, **Tag.N.Value** is required.
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
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        # The resource ID. You can specify at most 20 IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. Set the value to **ANYCASTEIPADDRESS**.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag information.
        # 
        # This parameter is required.
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
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values:
        # 
        # **true**\
        # 
        # **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnassociateAnycastEipAddressRequest(TeaModel):
    def __init__(
        self,
        anycast_id: str = None,
        bind_instance_id: str = None,
        bind_instance_region_id: str = None,
        bind_instance_type: str = None,
        client_token: str = None,
        dry_run: str = None,
        private_ip_address: str = None,
    ):
        # The ID of the Anycast EIP.
        # 
        # This parameter is required.
        self.anycast_id = anycast_id
        # The ID of the endpoint from which you want to disassociate the Anycast EIP.
        # 
        # This parameter is required.
        self.bind_instance_id = bind_instance_id
        # The region where the endpoint is deployed.
        # 
        # This parameter is required.
        self.bind_instance_region_id = bind_instance_region_id
        # The type of endpoint from which you want to disassociate the Anycast EIP. Valid values:
        # 
        # *   **SlbInstance**: an internal-facing Server Load Balancer (SLB) instance that is deployed in a virtual private cloud (VPC)
        # *   **NetworkInterface**: elastic network interface (ENI)
        # 
        # This parameter is required.
        self.bind_instance_type = bind_instance_type
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The secondary private IP address of the ENI from which you want to disassociate the Anycast EIP.
        # 
        # This parameter is valid only when you set **BindInstanceType** to **NetworkInterface**. If you do not specify this parameter, the primary private IP address of the ENI is used.
        self.private_ip_address = private_ip_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.bind_instance_id is not None:
            result['BindInstanceId'] = self.bind_instance_id
        if self.bind_instance_region_id is not None:
            result['BindInstanceRegionId'] = self.bind_instance_region_id
        if self.bind_instance_type is not None:
            result['BindInstanceType'] = self.bind_instance_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')
        if m.get('BindInstanceRegionId') is not None:
            self.bind_instance_region_id = m.get('BindInstanceRegionId')
        if m.get('BindInstanceType') is not None:
            self.bind_instance_type = m.get('BindInstanceType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        return self


class UnassociateAnycastEipAddressResponseBody(TeaModel):
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


class UnassociateAnycastEipAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnassociateAnycastEipAddressResponseBody = None,
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
            temp_model = UnassociateAnycastEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # The resource ID. You can specify up to 20 resource IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. Set the value to **ANYCASTEIPADDRESS**.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The key of the tag that you want to remove. You can specify at most 20 tag keys. The tag key cannot be an empty string.
        # 
        # A tag key can be up to 128 characters in length. It cannot start with aliyun or acs:, and cannot contain `http://` or `https://`.
        self.tag_key = tag_key

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values:
        # 
        # **true**\
        # 
        # **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAnycastEipAddressAssociationsRequestPopLocationAddList(TeaModel):
    def __init__(
        self,
        pop_location: str = None,
    ):
        # The access points in the access areas to be added.
        # 
        # You can call the [DescribeAnycastPopLocations](https://help.aliyun.com/document_detail/171938.html) operation to query the access points in supported access areas.
        self.pop_location = pop_location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pop_location is not None:
            result['PopLocation'] = self.pop_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PopLocation') is not None:
            self.pop_location = m.get('PopLocation')
        return self


class UpdateAnycastEipAddressAssociationsRequestPopLocationDeleteList(TeaModel):
    def __init__(
        self,
        pop_location: str = None,
    ):
        # The access points in the access areas to be deleted.
        # 
        # >  If the access point in the access area is associated with a default origin server, you cannot delete the access point in the access area.
        self.pop_location = pop_location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pop_location is not None:
            result['PopLocation'] = self.pop_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PopLocation') is not None:
            self.pop_location = m.get('PopLocation')
        return self


class UpdateAnycastEipAddressAssociationsRequest(TeaModel):
    def __init__(
        self,
        anycast_id: str = None,
        association_mode: str = None,
        bind_instance_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        pop_location_add_list: List[UpdateAnycastEipAddressAssociationsRequestPopLocationAddList] = None,
        pop_location_delete_list: List[UpdateAnycastEipAddressAssociationsRequestPopLocationDeleteList] = None,
    ):
        # The ID of the Anycast EIP.
        # 
        # This parameter is required.
        self.anycast_id = anycast_id
        # The association mode. Valid values:
        # 
        # *   **Default**: the default mode. In this mode, cloud resources to be associated are set as default origin servers.
        # *   **Normal**: the standard mode. In this mode, cloud resources to be associated are set as standard origin servers.
        self.association_mode = association_mode
        # The ID of the cloud resource with which you want to associate the Anycast EIP.
        # 
        # This parameter is required.
        self.bind_instance_id = bind_instance_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # >  If you do not set this parameter, the system automatically uses **RequestId** as **ClientToken**. **RequestId** may be different for each API request.
        self.client_token = client_token
        # Specifies whether to only precheck the request. Valid values:
        # 
        # *   **true**: prechecks the request without updating the association information. The system checks the required parameters, request syntax, and limits. If the request fails to pass the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the API request. If the request passes the precheck, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The access areas and access points to be added.
        self.pop_location_add_list = pop_location_add_list
        # The access areas and access points to be deleted.
        self.pop_location_delete_list = pop_location_delete_list

    def validate(self):
        if self.pop_location_add_list:
            for k in self.pop_location_add_list:
                if k:
                    k.validate()
        if self.pop_location_delete_list:
            for k in self.pop_location_delete_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.association_mode is not None:
            result['AssociationMode'] = self.association_mode
        if self.bind_instance_id is not None:
            result['BindInstanceId'] = self.bind_instance_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        result['PopLocationAddList'] = []
        if self.pop_location_add_list is not None:
            for k in self.pop_location_add_list:
                result['PopLocationAddList'].append(k.to_map() if k else None)
        result['PopLocationDeleteList'] = []
        if self.pop_location_delete_list is not None:
            for k in self.pop_location_delete_list:
                result['PopLocationDeleteList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('AssociationMode') is not None:
            self.association_mode = m.get('AssociationMode')
        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        self.pop_location_add_list = []
        if m.get('PopLocationAddList') is not None:
            for k in m.get('PopLocationAddList'):
                temp_model = UpdateAnycastEipAddressAssociationsRequestPopLocationAddList()
                self.pop_location_add_list.append(temp_model.from_map(k))
        self.pop_location_delete_list = []
        if m.get('PopLocationDeleteList') is not None:
            for k in m.get('PopLocationDeleteList'):
                temp_model = UpdateAnycastEipAddressAssociationsRequestPopLocationDeleteList()
                self.pop_location_delete_list.append(temp_model.from_map(k))
        return self


class UpdateAnycastEipAddressAssociationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class UpdateAnycastEipAddressAssociationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAnycastEipAddressAssociationsResponseBody = None,
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
            temp_model = UpdateAnycastEipAddressAssociationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


