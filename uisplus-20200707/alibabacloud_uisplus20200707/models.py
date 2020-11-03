# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List
except ImportError:
    pass


class DescribeUisRequest(TeaModel):
    def __init__(self, uis_id=None):
        self.uis_id = uis_id            # type: str

    def validate(self):
        self.validate_required(self.uis_id, 'uis_id')

    def to_map(self):
        result = {}
        result['UisId'] = self.uis_id
        return result

    def from_map(self, map={}):
        self.uis_id = map.get('UisId')
        return self


class DescribeUisResponse(TeaModel):
    def __init__(self, request_id=None, uis_id=None, uis_name=None, state=None, region_id=None, internet_ips=None):
        self.request_id = request_id    # type: str
        self.uis_id = uis_id            # type: str
        self.uis_name = uis_name        # type: str
        self.state = state              # type: str
        self.region_id = region_id      # type: str
        self.internet_ips = internet_ips  # type: List[DescribeUisResponseInternetIps]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.uis_id, 'uis_id')
        self.validate_required(self.uis_name, 'uis_name')
        self.validate_required(self.state, 'state')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.internet_ips, 'internet_ips')
        if self.internet_ips:
            for k in self.internet_ips:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['UisId'] = self.uis_id
        result['UisName'] = self.uis_name
        result['State'] = self.state
        result['RegionId'] = self.region_id
        result['InternetIps'] = []
        if self.internet_ips is not None:
            for k in self.internet_ips:
                result['InternetIps'].append(k.to_map() if k else None)
        else:
            result['InternetIps'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.uis_id = map.get('UisId')
        self.uis_name = map.get('UisName')
        self.state = map.get('State')
        self.region_id = map.get('RegionId')
        self.internet_ips = []
        if map.get('InternetIps') is not None:
            for k in map.get('InternetIps'):
                temp_model = DescribeUisResponseInternetIps()
                self.internet_ips.append(temp_model.from_map(k))
        else:
            self.internet_ips = None
        return self


class DescribeUisResponseInternetIps(TeaModel):
    def __init__(self, ip=None, role=None, eip_id=None):
        self.ip = ip                    # type: str
        self.role = role                # type: str
        self.eip_id = eip_id            # type: str

    def validate(self):
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.role, 'role')
        self.validate_required(self.eip_id, 'eip_id')

    def to_map(self):
        result = {}
        result['Ip'] = self.ip
        result['Role'] = self.role
        result['EipId'] = self.eip_id
        return result

    def from_map(self, map={}):
        self.ip = map.get('Ip')
        self.role = map.get('Role')
        self.eip_id = map.get('EipId')
        return self


class ModifyVnetRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, uis_id=None, vnet_id=None, cidrs=None, mbps_quota=None,
                 kpps_quota=None, flow_quota=None, name=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id      # type: str
        self.uis_id = uis_id            # type: str
        self.vnet_id = vnet_id          # type: str
        self.cidrs = cidrs              # type: str
        self.mbps_quota = mbps_quota    # type: int
        self.kpps_quota = kpps_quota    # type: int
        self.flow_quota = flow_quota    # type: int
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.uis_id, 'uis_id')
        self.validate_required(self.vnet_id, 'vnet_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['UisId'] = self.uis_id
        result['VnetId'] = self.vnet_id
        result['Cidrs'] = self.cidrs
        result['MbpsQuota'] = self.mbps_quota
        result['KppsQuota'] = self.kpps_quota
        result['FlowQuota'] = self.flow_quota
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.uis_id = map.get('UisId')
        self.vnet_id = map.get('VnetId')
        self.cidrs = map.get('Cidrs')
        self.mbps_quota = map.get('MbpsQuota')
        self.kpps_quota = map.get('KppsQuota')
        self.flow_quota = map.get('FlowQuota')
        self.name = map.get('Name')
        return self


class ModifyVnetResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeGreConnectionsRequest(TeaModel):
    def __init__(self, uis_id=None, region_id=None, page_number=None, page_size=None):
        self.uis_id = uis_id            # type: str
        self.region_id = region_id      # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.uis_id, 'uis_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['UisId'] = self.uis_id
        result['RegionId'] = self.region_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.uis_id = map.get('UisId')
        self.region_id = map.get('RegionId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeGreConnectionsResponse(TeaModel):
    def __init__(self, request_id=None, uis_id=None, uis_name=None, state=None, page=None, page_size=None,
                 total_count=None, gre_connections=None):
        self.request_id = request_id    # type: str
        self.uis_id = uis_id            # type: str
        self.uis_name = uis_name        # type: str
        self.state = state              # type: str
        self.page = page                # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.gre_connections = gre_connections  # type: List[DescribeGreConnectionsResponseGreConnections]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.uis_id, 'uis_id')
        self.validate_required(self.uis_name, 'uis_name')
        self.validate_required(self.state, 'state')
        self.validate_required(self.page, 'page')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.gre_connections, 'gre_connections')
        if self.gre_connections:
            for k in self.gre_connections:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['UisId'] = self.uis_id
        result['UisName'] = self.uis_name
        result['State'] = self.state
        result['Page'] = self.page
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['GreConnections'] = []
        if self.gre_connections is not None:
            for k in self.gre_connections:
                result['GreConnections'].append(k.to_map() if k else None)
        else:
            result['GreConnections'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.uis_id = map.get('UisId')
        self.uis_name = map.get('UisName')
        self.state = map.get('State')
        self.page = map.get('Page')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.gre_connections = []
        if map.get('GreConnections') is not None:
            for k in map.get('GreConnections'):
                temp_model = DescribeGreConnectionsResponseGreConnections()
                self.gre_connections.append(temp_model.from_map(k))
        else:
            self.gre_connections = None
        return self


class DescribeGreConnectionsResponseGreConnections(TeaModel):
    def __init__(self, gre_connection_id=None, state=None, cidrs=None, local_ip=None, local_tunnel_ip=None,
                 customer_ip=None, customer_tunnel_ip=None, name=None, description=None, create_time=None):
        self.gre_connection_id = gre_connection_id  # type: str
        self.state = state              # type: str
        self.cidrs = cidrs              # type: str
        self.local_ip = local_ip        # type: str
        self.local_tunnel_ip = local_tunnel_ip  # type: str
        self.customer_ip = customer_ip  # type: str
        self.customer_tunnel_ip = customer_tunnel_ip  # type: str
        self.name = name                # type: str
        self.description = description  # type: str
        self.create_time = create_time  # type: int

    def validate(self):
        self.validate_required(self.gre_connection_id, 'gre_connection_id')
        self.validate_required(self.state, 'state')
        self.validate_required(self.cidrs, 'cidrs')
        self.validate_required(self.local_ip, 'local_ip')
        self.validate_required(self.local_tunnel_ip, 'local_tunnel_ip')
        self.validate_required(self.customer_ip, 'customer_ip')
        self.validate_required(self.customer_tunnel_ip, 'customer_tunnel_ip')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.create_time, 'create_time')

    def to_map(self):
        result = {}
        result['GreConnectionId'] = self.gre_connection_id
        result['State'] = self.state
        result['Cidrs'] = self.cidrs
        result['LocalIp'] = self.local_ip
        result['LocalTunnelIp'] = self.local_tunnel_ip
        result['CustomerIp'] = self.customer_ip
        result['CustomerTunnelIp'] = self.customer_tunnel_ip
        result['Name'] = self.name
        result['Description'] = self.description
        result['CreateTime'] = self.create_time
        return result

    def from_map(self, map={}):
        self.gre_connection_id = map.get('GreConnectionId')
        self.state = map.get('State')
        self.cidrs = map.get('Cidrs')
        self.local_ip = map.get('LocalIp')
        self.local_tunnel_ip = map.get('LocalTunnelIp')
        self.customer_ip = map.get('CustomerIp')
        self.customer_tunnel_ip = map.get('CustomerTunnelIp')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.create_time = map.get('CreateTime')
        return self


class DescribeUissRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None):
        self.region_id = region_id      # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeUissResponse(TeaModel):
    def __init__(self, request_id=None, page=None, page_size=None, uiss=None):
        self.request_id = request_id    # type: str
        self.page = page                # type: int
        self.page_size = page_size      # type: int
        self.uiss = uiss                # type: List[DescribeUissResponseUiss]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page, 'page')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.uiss, 'uiss')
        if self.uiss:
            for k in self.uiss:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Page'] = self.page
        result['PageSize'] = self.page_size
        result['Uiss'] = []
        if self.uiss is not None:
            for k in self.uiss:
                result['Uiss'].append(k.to_map() if k else None)
        else:
            result['Uiss'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page = map.get('Page')
        self.page_size = map.get('PageSize')
        self.uiss = []
        if map.get('Uiss') is not None:
            for k in map.get('Uiss'):
                temp_model = DescribeUissResponseUiss()
                self.uiss.append(temp_model.from_map(k))
        else:
            self.uiss = None
        return self


class DescribeUissResponseUiss(TeaModel):
    def __init__(self, uis_id=None, uis_name=None, spec=None, state=None, create_time=None, description=None,
                 resource_group_id=None, region_id=None):
        self.uis_id = uis_id            # type: str
        self.uis_name = uis_name        # type: str
        self.spec = spec                # type: str
        self.state = state              # type: str
        self.create_time = create_time  # type: int
        self.description = description  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.uis_id, 'uis_id')
        self.validate_required(self.uis_name, 'uis_name')
        self.validate_required(self.spec, 'spec')
        self.validate_required(self.state, 'state')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.description, 'description')
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['UisId'] = self.uis_id
        result['UisName'] = self.uis_name
        result['Spec'] = self.spec
        result['State'] = self.state
        result['CreateTime'] = self.create_time
        result['Description'] = self.description
        result['ResourceGroupId'] = self.resource_group_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.uis_id = map.get('UisId')
        self.uis_name = map.get('UisName')
        self.spec = map.get('Spec')
        self.state = map.get('State')
        self.create_time = map.get('CreateTime')
        self.description = map.get('Description')
        self.resource_group_id = map.get('ResourceGroupId')
        self.region_id = map.get('RegionId')
        return self


class DescribeVnetRouteEntryListRequest(TeaModel):
    def __init__(self, uis_id=None, vnet_id=None, region_id=None, page_number=None, page_size=None):
        self.uis_id = uis_id            # type: str
        self.vnet_id = vnet_id          # type: str
        self.region_id = region_id      # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.uis_id, 'uis_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['UisId'] = self.uis_id
        result['VnetId'] = self.vnet_id
        result['RegionId'] = self.region_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.uis_id = map.get('UisId')
        self.vnet_id = map.get('VnetId')
        self.region_id = map.get('RegionId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeVnetRouteEntryListResponse(TeaModel):
    def __init__(self, request_id=None, page_size=None, page_number=None, total_count=None, vnets=None):
        self.request_id = request_id    # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int
        self.total_count = total_count  # type: int
        self.vnets = vnets              # type: List[DescribeVnetRouteEntryListResponseVnets]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.vnets, 'vnets')
        if self.vnets:
            for k in self.vnets:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        result['TotalCount'] = self.total_count
        result['Vnets'] = []
        if self.vnets is not None:
            for k in self.vnets:
                result['Vnets'].append(k.to_map() if k else None)
        else:
            result['Vnets'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        self.total_count = map.get('TotalCount')
        self.vnets = []
        if map.get('Vnets') is not None:
            for k in map.get('Vnets'):
                temp_model = DescribeVnetRouteEntryListResponseVnets()
                self.vnets.append(temp_model.from_map(k))
        else:
            self.vnets = None
        return self


class DescribeVnetRouteEntryListResponseVnets(TeaModel):
    def __init__(self, uis_id=None, vnet_id=None, destination=None, nexthop_type=None, nexthop=None):
        self.uis_id = uis_id            # type: str
        self.vnet_id = vnet_id          # type: str
        self.destination = destination  # type: str
        self.nexthop_type = nexthop_type  # type: str
        self.nexthop = nexthop          # type: str

    def validate(self):
        self.validate_required(self.uis_id, 'uis_id')
        self.validate_required(self.vnet_id, 'vnet_id')
        self.validate_required(self.destination, 'destination')
        self.validate_required(self.nexthop_type, 'nexthop_type')
        self.validate_required(self.nexthop, 'nexthop')

    def to_map(self):
        result = {}
        result['UisId'] = self.uis_id
        result['VnetId'] = self.vnet_id
        result['Destination'] = self.destination
        result['NexthopType'] = self.nexthop_type
        result['Nexthop'] = self.nexthop
        return result

    def from_map(self, map={}):
        self.uis_id = map.get('UisId')
        self.vnet_id = map.get('VnetId')
        self.destination = map.get('Destination')
        self.nexthop_type = map.get('NexthopType')
        self.nexthop = map.get('Nexthop')
        return self


class CreateVnetRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, uis_id=None, cidrs=None, mbps_quota=None, kpps_quota=None,
                 flow_quota=None, name=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id      # type: str
        self.uis_id = uis_id            # type: str
        self.cidrs = cidrs              # type: str
        self.mbps_quota = mbps_quota    # type: int
        self.kpps_quota = kpps_quota    # type: int
        self.flow_quota = flow_quota    # type: int
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.uis_id, 'uis_id')
        self.validate_required(self.cidrs, 'cidrs')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['UisId'] = self.uis_id
        result['Cidrs'] = self.cidrs
        result['MbpsQuota'] = self.mbps_quota
        result['KppsQuota'] = self.kpps_quota
        result['FlowQuota'] = self.flow_quota
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.uis_id = map.get('UisId')
        self.cidrs = map.get('Cidrs')
        self.mbps_quota = map.get('MbpsQuota')
        self.kpps_quota = map.get('KppsQuota')
        self.flow_quota = map.get('FlowQuota')
        self.name = map.get('Name')
        return self


class CreateVnetResponse(TeaModel):
    def __init__(self, request_id=None, vnet_id=None):
        self.request_id = request_id    # type: str
        self.vnet_id = vnet_id          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.vnet_id, 'vnet_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['VnetId'] = self.vnet_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.vnet_id = map.get('VnetId')
        return self


class DeleteVnetRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, uis_id=None, vnet_id=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id      # type: str
        self.uis_id = uis_id            # type: str
        self.vnet_id = vnet_id          # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.uis_id, 'uis_id')
        self.validate_required(self.vnet_id, 'vnet_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['UisId'] = self.uis_id
        result['VnetId'] = self.vnet_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.uis_id = map.get('UisId')
        self.vnet_id = map.get('VnetId')
        return self


class DeleteVnetResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeVnetsRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None, vnet_id=None, uis_id=None):
        self.region_id = region_id      # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.vnet_id = vnet_id          # type: List[str]
        self.uis_id = uis_id            # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.uis_id, 'uis_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['VnetId'] = self.vnet_id
        result['UisId'] = self.uis_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.vnet_id = map.get('VnetId')
        self.uis_id = map.get('UisId')
        return self


class DescribeVnetsResponse(TeaModel):
    def __init__(self, request_id=None, page_size=None, page_number=None, total_count=None, vnets=None):
        self.request_id = request_id    # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int
        self.total_count = total_count  # type: int
        self.vnets = vnets              # type: List[DescribeVnetsResponseVnets]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.vnets, 'vnets')
        if self.vnets:
            for k in self.vnets:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        result['TotalCount'] = self.total_count
        result['Vnets'] = []
        if self.vnets is not None:
            for k in self.vnets:
                result['Vnets'].append(k.to_map() if k else None)
        else:
            result['Vnets'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        self.total_count = map.get('TotalCount')
        self.vnets = []
        if map.get('Vnets') is not None:
            for k in map.get('Vnets'):
                temp_model = DescribeVnetsResponseVnets()
                self.vnets.append(temp_model.from_map(k))
        else:
            self.vnets = None
        return self


class DescribeVnetsResponseVnets(TeaModel):
    def __init__(self, uis_id=None, vnet_id=None, name=None, cidrs=None, mbps_quota=None, kpps_quota=None,
                 flow_quota=None, state=None):
        self.uis_id = uis_id            # type: str
        self.vnet_id = vnet_id          # type: str
        self.name = name                # type: str
        self.cidrs = cidrs              # type: str
        self.mbps_quota = mbps_quota    # type: int
        self.kpps_quota = kpps_quota    # type: int
        self.flow_quota = flow_quota    # type: int
        self.state = state              # type: str

    def validate(self):
        self.validate_required(self.uis_id, 'uis_id')
        self.validate_required(self.vnet_id, 'vnet_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.cidrs, 'cidrs')
        self.validate_required(self.mbps_quota, 'mbps_quota')
        self.validate_required(self.kpps_quota, 'kpps_quota')
        self.validate_required(self.flow_quota, 'flow_quota')
        self.validate_required(self.state, 'state')

    def to_map(self):
        result = {}
        result['UisId'] = self.uis_id
        result['VnetId'] = self.vnet_id
        result['Name'] = self.name
        result['Cidrs'] = self.cidrs
        result['MbpsQuota'] = self.mbps_quota
        result['KppsQuota'] = self.kpps_quota
        result['FlowQuota'] = self.flow_quota
        result['State'] = self.state
        return result

    def from_map(self, map={}):
        self.uis_id = map.get('UisId')
        self.vnet_id = map.get('VnetId')
        self.name = map.get('Name')
        self.cidrs = map.get('Cidrs')
        self.mbps_quota = map.get('MbpsQuota')
        self.kpps_quota = map.get('KppsQuota')
        self.flow_quota = map.get('FlowQuota')
        self.state = map.get('State')
        return self


class DeleteVnetRouteEntryRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, uis_id=None, vnet_id=None, destination=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id      # type: str
        self.uis_id = uis_id            # type: str
        self.vnet_id = vnet_id          # type: str
        self.destination = destination  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.uis_id, 'uis_id')
        self.validate_required(self.vnet_id, 'vnet_id')
        self.validate_required(self.destination, 'destination')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['UisId'] = self.uis_id
        result['VnetId'] = self.vnet_id
        result['Destination'] = self.destination
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.uis_id = map.get('UisId')
        self.vnet_id = map.get('VnetId')
        self.destination = map.get('Destination')
        return self


class DeleteVnetRouteEntryResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AssociateEipRequest(TeaModel):
    def __init__(self, uis_id=None, type=None, instance_id=None, role=None, client_token=None, region_id=None):
        self.uis_id = uis_id            # type: str
        self.type = type                # type: str
        self.instance_id = instance_id  # type: str
        self.role = role                # type: str
        self.client_token = client_token  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.uis_id, 'uis_id')
        self.validate_required(self.type, 'type')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['UisId'] = self.uis_id
        result['Type'] = self.type
        result['InstanceId'] = self.instance_id
        result['Role'] = self.role
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.uis_id = map.get('UisId')
        self.type = map.get('Type')
        self.instance_id = map.get('InstanceId')
        self.role = map.get('Role')
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        return self


class AssociateEipResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyGreConnectionRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, uis_id=None, gre_connection_id=None, cidrs=None, name=None,
                 local_ip=None, customer_ip=None, local_tunnel_ip=None, customer_tunnel_ip=None, description=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id      # type: str
        self.uis_id = uis_id            # type: str
        self.gre_connection_id = gre_connection_id  # type: str
        self.cidrs = cidrs              # type: str
        self.name = name                # type: str
        self.local_ip = local_ip        # type: str
        self.customer_ip = customer_ip  # type: str
        self.local_tunnel_ip = local_tunnel_ip  # type: str
        self.customer_tunnel_ip = customer_tunnel_ip  # type: str
        self.description = description  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.uis_id, 'uis_id')
        self.validate_required(self.gre_connection_id, 'gre_connection_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['UisId'] = self.uis_id
        result['GreConnectionId'] = self.gre_connection_id
        result['Cidrs'] = self.cidrs
        result['Name'] = self.name
        result['LocalIp'] = self.local_ip
        result['CustomerIp'] = self.customer_ip
        result['LocalTunnelIp'] = self.local_tunnel_ip
        result['CustomerTunnelIp'] = self.customer_tunnel_ip
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.uis_id = map.get('UisId')
        self.gre_connection_id = map.get('GreConnectionId')
        self.cidrs = map.get('Cidrs')
        self.name = map.get('Name')
        self.local_ip = map.get('LocalIp')
        self.customer_ip = map.get('CustomerIp')
        self.local_tunnel_ip = map.get('LocalTunnelIp')
        self.customer_tunnel_ip = map.get('CustomerTunnelIp')
        self.description = map.get('Description')
        return self


class ModifyGreConnectionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeVnetRequest(TeaModel):
    def __init__(self, uis_id=None, vnet_id=None, region_id=None):
        self.uis_id = uis_id            # type: str
        self.vnet_id = vnet_id          # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.uis_id, 'uis_id')
        self.validate_required(self.vnet_id, 'vnet_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['UisId'] = self.uis_id
        result['VnetId'] = self.vnet_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.uis_id = map.get('UisId')
        self.vnet_id = map.get('VnetId')
        self.region_id = map.get('RegionId')
        return self


class DescribeVnetResponse(TeaModel):
    def __init__(self, request_id=None, uis_id=None, name=None, state=None, vnet_id=None, cidrs=None, mbps_quota=None,
                 kpps_quota=None, flow_quota=None):
        self.request_id = request_id    # type: str
        self.uis_id = uis_id            # type: str
        self.name = name                # type: str
        self.state = state              # type: str
        self.vnet_id = vnet_id          # type: str
        self.cidrs = cidrs              # type: str
        self.mbps_quota = mbps_quota    # type: str
        self.kpps_quota = kpps_quota    # type: str
        self.flow_quota = flow_quota    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.uis_id, 'uis_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.state, 'state')
        self.validate_required(self.vnet_id, 'vnet_id')
        self.validate_required(self.cidrs, 'cidrs')
        self.validate_required(self.mbps_quota, 'mbps_quota')
        self.validate_required(self.kpps_quota, 'kpps_quota')
        self.validate_required(self.flow_quota, 'flow_quota')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['UisId'] = self.uis_id
        result['Name'] = self.name
        result['State'] = self.state
        result['VnetId'] = self.vnet_id
        result['Cidrs'] = self.cidrs
        result['MbpsQuota'] = self.mbps_quota
        result['KppsQuota'] = self.kpps_quota
        result['FlowQuota'] = self.flow_quota
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.uis_id = map.get('UisId')
        self.name = map.get('Name')
        self.state = map.get('State')
        self.vnet_id = map.get('VnetId')
        self.cidrs = map.get('Cidrs')
        self.mbps_quota = map.get('MbpsQuota')
        self.kpps_quota = map.get('KppsQuota')
        self.flow_quota = map.get('FlowQuota')
        return self


class UnAssociateEipRequest(TeaModel):
    def __init__(self, uis_id=None, type=None, instance_id=None, client_token=None, region_id=None):
        self.uis_id = uis_id            # type: str
        self.type = type                # type: str
        self.instance_id = instance_id  # type: str
        self.client_token = client_token  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.uis_id, 'uis_id')
        self.validate_required(self.type, 'type')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['UisId'] = self.uis_id
        result['Type'] = self.type
        result['InstanceId'] = self.instance_id
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.uis_id = map.get('UisId')
        self.type = map.get('Type')
        self.instance_id = map.get('InstanceId')
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        return self


class UnAssociateEipResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteGreConnectionRequest(TeaModel):
    def __init__(self, uis_id=None, client_token=None, region_id=None, gre_connection_id=None):
        self.uis_id = uis_id            # type: str
        self.client_token = client_token  # type: str
        self.region_id = region_id      # type: str
        self.gre_connection_id = gre_connection_id  # type: str

    def validate(self):
        self.validate_required(self.uis_id, 'uis_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.gre_connection_id, 'gre_connection_id')

    def to_map(self):
        result = {}
        result['UisId'] = self.uis_id
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['GreConnectionId'] = self.gre_connection_id
        return result

    def from_map(self, map={}):
        self.uis_id = map.get('UisId')
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.gre_connection_id = map.get('GreConnectionId')
        return self


class DeleteGreConnectionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateGreConnectionRequest(TeaModel):
    def __init__(self, uis_id=None, name=None, description=None, cidrs=None, local_ip=None, local_tunnel_ip=None,
                 customer_ip=None, customer_tunnel_ip=None, client_token=None, region_id=None):
        self.uis_id = uis_id            # type: str
        self.name = name                # type: str
        self.description = description  # type: str
        self.cidrs = cidrs              # type: str
        self.local_ip = local_ip        # type: str
        self.local_tunnel_ip = local_tunnel_ip  # type: str
        self.customer_ip = customer_ip  # type: str
        self.customer_tunnel_ip = customer_tunnel_ip  # type: str
        self.client_token = client_token  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.uis_id, 'uis_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.cidrs, 'cidrs')
        self.validate_required(self.local_ip, 'local_ip')
        self.validate_required(self.local_tunnel_ip, 'local_tunnel_ip')
        self.validate_required(self.customer_ip, 'customer_ip')
        self.validate_required(self.customer_tunnel_ip, 'customer_tunnel_ip')

    def to_map(self):
        result = {}
        result['UisId'] = self.uis_id
        result['Name'] = self.name
        result['Description'] = self.description
        result['Cidrs'] = self.cidrs
        result['LocalIp'] = self.local_ip
        result['LocalTunnelIp'] = self.local_tunnel_ip
        result['CustomerIp'] = self.customer_ip
        result['CustomerTunnelIp'] = self.customer_tunnel_ip
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.uis_id = map.get('UisId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.cidrs = map.get('Cidrs')
        self.local_ip = map.get('LocalIp')
        self.local_tunnel_ip = map.get('LocalTunnelIp')
        self.customer_ip = map.get('CustomerIp')
        self.customer_tunnel_ip = map.get('CustomerTunnelIp')
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        return self


class CreateGreConnectionResponse(TeaModel):
    def __init__(self, request_id=None, gre_connection_id=None):
        self.request_id = request_id    # type: str
        self.gre_connection_id = gre_connection_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.gre_connection_id, 'gre_connection_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['GreConnectionId'] = self.gre_connection_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.gre_connection_id = map.get('GreConnectionId')
        return self


class CreateUisRequest(TeaModel):
    def __init__(self, uis_name=None, spec=None, description=None, resource_group_id=None, client_token=None,
                 region_id=None):
        self.uis_name = uis_name        # type: str
        self.spec = spec                # type: str
        self.description = description  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.client_token = client_token  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.uis_name, 'uis_name')
        self.validate_required(self.spec, 'spec')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['UisName'] = self.uis_name
        result['Spec'] = self.spec
        result['Description'] = self.description
        result['ResourceGroupId'] = self.resource_group_id
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.uis_name = map.get('UisName')
        self.spec = map.get('Spec')
        self.description = map.get('Description')
        self.resource_group_id = map.get('ResourceGroupId')
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        return self


class CreateUisResponse(TeaModel):
    def __init__(self, request_id=None, uis_id=None):
        self.request_id = request_id    # type: str
        self.uis_id = uis_id            # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.uis_id, 'uis_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['UisId'] = self.uis_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.uis_id = map.get('UisId')
        return self


class CreateVnetRouteEntryRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, uis_id=None, vnet_id=None, destination=None,
                 nexthop_type=None, nexthop=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id      # type: str
        self.uis_id = uis_id            # type: str
        self.vnet_id = vnet_id          # type: str
        self.destination = destination  # type: str
        self.nexthop_type = nexthop_type  # type: str
        self.nexthop = nexthop          # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.uis_id, 'uis_id')
        self.validate_required(self.vnet_id, 'vnet_id')
        self.validate_required(self.destination, 'destination')
        self.validate_required(self.nexthop_type, 'nexthop_type')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['UisId'] = self.uis_id
        result['VnetId'] = self.vnet_id
        result['Destination'] = self.destination
        result['NexthopType'] = self.nexthop_type
        result['Nexthop'] = self.nexthop
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.uis_id = map.get('UisId')
        self.vnet_id = map.get('VnetId')
        self.destination = map.get('Destination')
        self.nexthop_type = map.get('NexthopType')
        self.nexthop = map.get('Nexthop')
        return self


class CreateVnetRouteEntryResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteUisRequest(TeaModel):
    def __init__(self, uis_id=None, client_token=None, region_id=None):
        self.uis_id = uis_id            # type: str
        self.client_token = client_token  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.uis_id, 'uis_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['UisId'] = self.uis_id
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.uis_id = map.get('UisId')
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        return self


class DeleteUisResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeGreConnectionRequest(TeaModel):
    def __init__(self, uis_id=None, gre_connection_id=None, region_id=None):
        self.uis_id = uis_id            # type: str
        self.gre_connection_id = gre_connection_id  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.uis_id, 'uis_id')
        self.validate_required(self.gre_connection_id, 'gre_connection_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['UisId'] = self.uis_id
        result['GreConnectionId'] = self.gre_connection_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.uis_id = map.get('UisId')
        self.gre_connection_id = map.get('GreConnectionId')
        self.region_id = map.get('RegionId')
        return self


class DescribeGreConnectionResponse(TeaModel):
    def __init__(self, request_id=None, uis_id=None, uis_name=None, gre_connection_id=None, state=None, cidrs=None,
                 local_ip=None, local_tunnel_ip=None, customer_ip=None, customer_tunnel_ip=None, name=None, description=None,
                 create_time=None):
        self.request_id = request_id    # type: str
        self.uis_id = uis_id            # type: str
        self.uis_name = uis_name        # type: str
        self.gre_connection_id = gre_connection_id  # type: str
        self.state = state              # type: str
        self.cidrs = cidrs              # type: str
        self.local_ip = local_ip        # type: str
        self.local_tunnel_ip = local_tunnel_ip  # type: str
        self.customer_ip = customer_ip  # type: str
        self.customer_tunnel_ip = customer_tunnel_ip  # type: str
        self.name = name                # type: str
        self.description = description  # type: str
        self.create_time = create_time  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.uis_id, 'uis_id')
        self.validate_required(self.uis_name, 'uis_name')
        self.validate_required(self.gre_connection_id, 'gre_connection_id')
        self.validate_required(self.state, 'state')
        self.validate_required(self.cidrs, 'cidrs')
        self.validate_required(self.local_ip, 'local_ip')
        self.validate_required(self.local_tunnel_ip, 'local_tunnel_ip')
        self.validate_required(self.customer_ip, 'customer_ip')
        self.validate_required(self.customer_tunnel_ip, 'customer_tunnel_ip')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.create_time, 'create_time')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['UisId'] = self.uis_id
        result['UisName'] = self.uis_name
        result['GreConnectionId'] = self.gre_connection_id
        result['State'] = self.state
        result['Cidrs'] = self.cidrs
        result['LocalIp'] = self.local_ip
        result['LocalTunnelIp'] = self.local_tunnel_ip
        result['CustomerIp'] = self.customer_ip
        result['CustomerTunnelIp'] = self.customer_tunnel_ip
        result['Name'] = self.name
        result['Description'] = self.description
        result['CreateTime'] = self.create_time
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.uis_id = map.get('UisId')
        self.uis_name = map.get('UisName')
        self.gre_connection_id = map.get('GreConnectionId')
        self.state = map.get('State')
        self.cidrs = map.get('Cidrs')
        self.local_ip = map.get('LocalIp')
        self.local_tunnel_ip = map.get('LocalTunnelIp')
        self.customer_ip = map.get('CustomerIp')
        self.customer_tunnel_ip = map.get('CustomerTunnelIp')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.create_time = map.get('CreateTime')
        return self
