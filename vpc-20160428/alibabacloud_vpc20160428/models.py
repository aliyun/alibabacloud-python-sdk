# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ListPhysicalConnectionFeaturesRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, physical_connection_id=None):
        self.region_id = region_id
        self.client_token = client_token
        self.physical_connection_id = physical_connection_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.physical_connection_id, 'physical_connection_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['PhysicalConnectionId'] = self.physical_connection_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.physical_connection_id = map.get('PhysicalConnectionId')
        return self


class ListPhysicalConnectionFeaturesResponse(TeaModel):
    def __init__(self, request_id=None, physical_connection_features=None):
        self.request_id = request_id
        self.physical_connection_features = physical_connection_features

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.physical_connection_features, 'physical_connection_features')
        if self.physical_connection_features:
            for k in self.physical_connection_features:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PhysicalConnectionFeatures'] = []
        if self.physical_connection_features is not None:
            for k in self.physical_connection_features:
                result['PhysicalConnectionFeatures'].append(k.to_map() if k else None)
        else:
            result['PhysicalConnectionFeatures'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.physical_connection_features = []
        if map.get('PhysicalConnectionFeatures') is not None:
            for k in map.get('PhysicalConnectionFeatures'):
                temp_model = ListPhysicalConnectionFeaturesResponsePhysicalConnectionFeatures()
                self.physical_connection_features.append(temp_model.from_map(k))
        else:
            self.physical_connection_features = None
        return self


class ListPhysicalConnectionFeaturesResponsePhysicalConnectionFeatures(TeaModel):
    def __init__(self, feature_key=None, feature_value=None):
        self.feature_key = feature_key
        self.feature_value = feature_value

    def validate(self):
        self.validate_required(self.feature_key, 'feature_key')
        self.validate_required(self.feature_value, 'feature_value')

    def to_map(self):
        result = {}
        result['FeatureKey'] = self.feature_key
        result['FeatureValue'] = self.feature_value
        return result

    def from_map(self, map={}):
        self.feature_key = map.get('FeatureKey')
        self.feature_value = map.get('FeatureValue')
        return self


class ListNatGatewayEcsMetricRequest(TeaModel):
    def __init__(self, region_id=None, dry_run=None, nat_gateway_id=None, time_point=None, order_key=None,
                 order_type=None, private_ip_address=None, next_token=None, max_results=None):
        self.region_id = region_id
        self.dry_run = dry_run
        self.nat_gateway_id = nat_gateway_id
        self.time_point = time_point
        self.order_key = order_key
        self.order_type = order_type
        self.private_ip_address = private_ip_address
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.nat_gateway_id, 'nat_gateway_id')
        self.validate_required(self.time_point, 'time_point')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DryRun'] = self.dry_run
        result['NatGatewayId'] = self.nat_gateway_id
        result['TimePoint'] = self.time_point
        result['OrderKey'] = self.order_key
        result['OrderType'] = self.order_type
        result['PrivateIpAddress'] = self.private_ip_address
        result['NextToken'] = self.next_token
        result['MaxResults'] = self.max_results
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dry_run = map.get('DryRun')
        self.nat_gateway_id = map.get('NatGatewayId')
        self.time_point = map.get('TimePoint')
        self.order_key = map.get('OrderKey')
        self.order_type = map.get('OrderType')
        self.private_ip_address = map.get('PrivateIpAddress')
        self.next_token = map.get('NextToken')
        self.max_results = map.get('MaxResults')
        return self


class ListNatGatewayEcsMetricResponse(TeaModel):
    def __init__(self, request_id=None, next_token=None, max_results=None, metric_data_list=None):
        self.request_id = request_id
        self.next_token = next_token
        self.max_results = max_results
        self.metric_data_list = metric_data_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.max_results, 'max_results')
        self.validate_required(self.metric_data_list, 'metric_data_list')
        if self.metric_data_list:
            for k in self.metric_data_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['NextToken'] = self.next_token
        result['MaxResults'] = self.max_results
        result['MetricDataList'] = []
        if self.metric_data_list is not None:
            for k in self.metric_data_list:
                result['MetricDataList'].append(k.to_map() if k else None)
        else:
            result['MetricDataList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.next_token = map.get('NextToken')
        self.max_results = map.get('MaxResults')
        self.metric_data_list = []
        if map.get('MetricDataList') is not None:
            for k in map.get('MetricDataList'):
                temp_model = ListNatGatewayEcsMetricResponseMetricDataList()
                self.metric_data_list.append(temp_model.from_map(k))
        else:
            self.metric_data_list = None
        return self


class ListNatGatewayEcsMetricResponseMetricDataList(TeaModel):
    def __init__(self, nat_gateway_id=None, private_ip_address=None, timestamp=None, active_session_num=None,
                 new_session_rate=None, rx_bps=None, tx_bps=None, rx_pps=None, tx_pps=None):
        self.nat_gateway_id = nat_gateway_id
        self.private_ip_address = private_ip_address
        self.timestamp = timestamp
        self.active_session_num = active_session_num
        self.new_session_rate = new_session_rate
        self.rx_bps = rx_bps
        self.tx_bps = tx_bps
        self.rx_pps = rx_pps
        self.tx_pps = tx_pps

    def validate(self):
        self.validate_required(self.nat_gateway_id, 'nat_gateway_id')
        self.validate_required(self.private_ip_address, 'private_ip_address')
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.active_session_num, 'active_session_num')
        self.validate_required(self.new_session_rate, 'new_session_rate')
        self.validate_required(self.rx_bps, 'rx_bps')
        self.validate_required(self.tx_bps, 'tx_bps')
        self.validate_required(self.rx_pps, 'rx_pps')
        self.validate_required(self.tx_pps, 'tx_pps')

    def to_map(self):
        result = {}
        result['NatGatewayId'] = self.nat_gateway_id
        result['PrivateIpAddress'] = self.private_ip_address
        result['Timestamp'] = self.timestamp
        result['ActiveSessionNum'] = self.active_session_num
        result['NewSessionRate'] = self.new_session_rate
        result['RxBps'] = self.rx_bps
        result['TxBps'] = self.tx_bps
        result['RxPps'] = self.rx_pps
        result['TxPps'] = self.tx_pps
        return result

    def from_map(self, map={}):
        self.nat_gateway_id = map.get('NatGatewayId')
        self.private_ip_address = map.get('PrivateIpAddress')
        self.timestamp = map.get('Timestamp')
        self.active_session_num = map.get('ActiveSessionNum')
        self.new_session_rate = map.get('NewSessionRate')
        self.rx_bps = map.get('RxBps')
        self.tx_bps = map.get('TxBps')
        self.rx_pps = map.get('RxPps')
        self.tx_pps = map.get('TxPps')
        return self


class DisableNatGatewayEcsMetricRequest(TeaModel):
    def __init__(self, region_id=None, dry_run=None, nat_gateway_id=None):
        self.region_id = region_id
        self.dry_run = dry_run
        self.nat_gateway_id = nat_gateway_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.nat_gateway_id, 'nat_gateway_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DryRun'] = self.dry_run
        result['NatGatewayId'] = self.nat_gateway_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dry_run = map.get('DryRun')
        self.nat_gateway_id = map.get('NatGatewayId')
        return self


class DisableNatGatewayEcsMetricResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class EnableNatGatewayEcsMetricRequest(TeaModel):
    def __init__(self, region_id=None, dry_run=None, nat_gateway_id=None):
        self.region_id = region_id
        self.dry_run = dry_run
        self.nat_gateway_id = nat_gateway_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.nat_gateway_id, 'nat_gateway_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DryRun'] = self.dry_run
        result['NatGatewayId'] = self.nat_gateway_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dry_run = map.get('DryRun')
        self.nat_gateway_id = map.get('NatGatewayId')
        return self


class EnableNatGatewayEcsMetricResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateDhcpOptionsSetRequest(TeaModel):
    def __init__(self, region_id=None, domain_name_servers=None, dhcp_options_set_name=None,
                 dhcp_options_set_description=None, domain_name=None, client_token=None, dry_run=None):
        self.region_id = region_id
        self.domain_name_servers = domain_name_servers
        self.dhcp_options_set_name = dhcp_options_set_name
        self.dhcp_options_set_description = dhcp_options_set_description
        self.domain_name = domain_name
        self.client_token = client_token
        self.dry_run = dry_run

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DomainNameServers'] = self.domain_name_servers
        result['DhcpOptionsSetName'] = self.dhcp_options_set_name
        result['DhcpOptionsSetDescription'] = self.dhcp_options_set_description
        result['DomainName'] = self.domain_name
        result['ClientToken'] = self.client_token
        result['DryRun'] = self.dry_run
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.domain_name_servers = map.get('DomainNameServers')
        self.dhcp_options_set_name = map.get('DhcpOptionsSetName')
        self.dhcp_options_set_description = map.get('DhcpOptionsSetDescription')
        self.domain_name = map.get('DomainName')
        self.client_token = map.get('ClientToken')
        self.dry_run = map.get('DryRun')
        return self


class CreateDhcpOptionsSetResponse(TeaModel):
    def __init__(self, request_id=None, dhcp_options_set_id=None):
        self.request_id = request_id
        self.dhcp_options_set_id = dhcp_options_set_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dhcp_options_set_id, 'dhcp_options_set_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DhcpOptionsSetId'] = self.dhcp_options_set_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dhcp_options_set_id = map.get('DhcpOptionsSetId')
        return self


class ReplaceVpcDhcpOptionsSetRequest(TeaModel):
    def __init__(self, region_id=None, dhcp_options_set_id=None, vpc_id=None, client_token=None, dry_run=None):
        self.region_id = region_id
        self.dhcp_options_set_id = dhcp_options_set_id
        self.vpc_id = vpc_id
        self.client_token = client_token
        self.dry_run = dry_run

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.dhcp_options_set_id, 'dhcp_options_set_id')
        self.validate_required(self.vpc_id, 'vpc_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DhcpOptionsSetId'] = self.dhcp_options_set_id
        result['VpcId'] = self.vpc_id
        result['ClientToken'] = self.client_token
        result['DryRun'] = self.dry_run
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dhcp_options_set_id = map.get('DhcpOptionsSetId')
        self.vpc_id = map.get('VpcId')
        self.client_token = map.get('ClientToken')
        self.dry_run = map.get('DryRun')
        return self


class ReplaceVpcDhcpOptionsSetResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class UpdateDhcpOptionsSetAttributeRequest(TeaModel):
    def __init__(self, region_id=None, dhcp_options_set_id=None, domain_name_servers=None, domain_name=None,
                 dhcp_options_set_name=None, dhcp_options_set_description=None, client_token=None, dry_run=None):
        self.region_id = region_id
        self.dhcp_options_set_id = dhcp_options_set_id
        self.domain_name_servers = domain_name_servers
        self.domain_name = domain_name
        self.dhcp_options_set_name = dhcp_options_set_name
        self.dhcp_options_set_description = dhcp_options_set_description
        self.client_token = client_token
        self.dry_run = dry_run

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.dhcp_options_set_id, 'dhcp_options_set_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DhcpOptionsSetId'] = self.dhcp_options_set_id
        result['DomainNameServers'] = self.domain_name_servers
        result['DomainName'] = self.domain_name
        result['DhcpOptionsSetName'] = self.dhcp_options_set_name
        result['DhcpOptionsSetDescription'] = self.dhcp_options_set_description
        result['ClientToken'] = self.client_token
        result['DryRun'] = self.dry_run
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dhcp_options_set_id = map.get('DhcpOptionsSetId')
        self.domain_name_servers = map.get('DomainNameServers')
        self.domain_name = map.get('DomainName')
        self.dhcp_options_set_name = map.get('DhcpOptionsSetName')
        self.dhcp_options_set_description = map.get('DhcpOptionsSetDescription')
        self.client_token = map.get('ClientToken')
        self.dry_run = map.get('DryRun')
        return self


class UpdateDhcpOptionsSetAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class GetDhcpOptionsSetRequest(TeaModel):
    def __init__(self, region_id=None, dhcp_options_set_id=None):
        self.region_id = region_id
        self.dhcp_options_set_id = dhcp_options_set_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.dhcp_options_set_id, 'dhcp_options_set_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DhcpOptionsSetId'] = self.dhcp_options_set_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dhcp_options_set_id = map.get('DhcpOptionsSetId')
        return self


class GetDhcpOptionsSetResponse(TeaModel):
    def __init__(self, request_id=None, dhcp_options_set_name=None, dhcp_options_set_description=None,
                 dhcp_options_set_id=None, owner_id=None, status=None, associate_vpcs=None, dhcp_options=None):
        self.request_id = request_id
        self.dhcp_options_set_name = dhcp_options_set_name
        self.dhcp_options_set_description = dhcp_options_set_description
        self.dhcp_options_set_id = dhcp_options_set_id
        self.owner_id = owner_id
        self.status = status
        self.associate_vpcs = associate_vpcs
        self.dhcp_options = dhcp_options  # type: GetDhcpOptionsSetResponseDhcpOptions

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dhcp_options_set_name, 'dhcp_options_set_name')
        self.validate_required(self.dhcp_options_set_description, 'dhcp_options_set_description')
        self.validate_required(self.dhcp_options_set_id, 'dhcp_options_set_id')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.associate_vpcs, 'associate_vpcs')
        if self.associate_vpcs:
            for k in self.associate_vpcs:
                if k:
                    k.validate()
        self.validate_required(self.dhcp_options, 'dhcp_options')
        if self.dhcp_options:
            self.dhcp_options.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DhcpOptionsSetName'] = self.dhcp_options_set_name
        result['DhcpOptionsSetDescription'] = self.dhcp_options_set_description
        result['DhcpOptionsSetId'] = self.dhcp_options_set_id
        result['OwnerId'] = self.owner_id
        result['Status'] = self.status
        result['AssociateVpcs'] = []
        if self.associate_vpcs is not None:
            for k in self.associate_vpcs:
                result['AssociateVpcs'].append(k.to_map() if k else None)
        else:
            result['AssociateVpcs'] = None
        if self.dhcp_options is not None:
            result['DhcpOptions'] = self.dhcp_options.to_map()
        else:
            result['DhcpOptions'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dhcp_options_set_name = map.get('DhcpOptionsSetName')
        self.dhcp_options_set_description = map.get('DhcpOptionsSetDescription')
        self.dhcp_options_set_id = map.get('DhcpOptionsSetId')
        self.owner_id = map.get('OwnerId')
        self.status = map.get('Status')
        self.associate_vpcs = []
        if map.get('AssociateVpcs') is not None:
            for k in map.get('AssociateVpcs'):
                temp_model = GetDhcpOptionsSetResponseAssociateVpcs()
                self.associate_vpcs.append(temp_model.from_map(k))
        else:
            self.associate_vpcs = None
        if map.get('DhcpOptions') is not None:
            temp_model = GetDhcpOptionsSetResponseDhcpOptions()
            self.dhcp_options = temp_model.from_map(map['DhcpOptions'])
        else:
            self.dhcp_options = None
        return self


class GetDhcpOptionsSetResponseAssociateVpcs(TeaModel):
    def __init__(self, vpc_id=None, associate_status=None):
        self.vpc_id = vpc_id
        self.associate_status = associate_status

    def validate(self):
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.associate_status, 'associate_status')

    def to_map(self):
        result = {}
        result['VpcId'] = self.vpc_id
        result['AssociateStatus'] = self.associate_status
        return result

    def from_map(self, map={}):
        self.vpc_id = map.get('VpcId')
        self.associate_status = map.get('AssociateStatus')
        return self


class GetDhcpOptionsSetResponseDhcpOptions(TeaModel):
    def __init__(self, domain_name_servers=None, domain_name=None):
        self.domain_name_servers = domain_name_servers
        self.domain_name = domain_name

    def validate(self):
        self.validate_required(self.domain_name_servers, 'domain_name_servers')
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainNameServers'] = self.domain_name_servers
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.domain_name_servers = map.get('DomainNameServers')
        self.domain_name = map.get('DomainName')
        return self


class ListDhcpOptionsSetsRequest(TeaModel):
    def __init__(self, region_id=None, next_token=None, max_results=None, domain_name=None,
                 dhcp_options_set_id=None, dhcp_options_set_name=None):
        self.region_id = region_id
        self.next_token = next_token
        self.max_results = max_results
        self.domain_name = domain_name
        self.dhcp_options_set_id = dhcp_options_set_id
        self.dhcp_options_set_name = dhcp_options_set_name

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['NextToken'] = self.next_token
        result['MaxResults'] = self.max_results
        result['DomainName'] = self.domain_name
        result['DhcpOptionsSetId'] = self.dhcp_options_set_id
        result['DhcpOptionsSetName'] = self.dhcp_options_set_name
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.next_token = map.get('NextToken')
        self.max_results = map.get('MaxResults')
        self.domain_name = map.get('DomainName')
        self.dhcp_options_set_id = map.get('DhcpOptionsSetId')
        self.dhcp_options_set_name = map.get('DhcpOptionsSetName')
        return self


class ListDhcpOptionsSetsResponse(TeaModel):
    def __init__(self, request_id=None, next_token=None, dhcp_options_sets=None):
        self.request_id = request_id
        self.next_token = next_token
        self.dhcp_options_sets = dhcp_options_sets

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.dhcp_options_sets, 'dhcp_options_sets')
        if self.dhcp_options_sets:
            for k in self.dhcp_options_sets:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['NextToken'] = self.next_token
        result['DhcpOptionsSets'] = []
        if self.dhcp_options_sets is not None:
            for k in self.dhcp_options_sets:
                result['DhcpOptionsSets'].append(k.to_map() if k else None)
        else:
            result['DhcpOptionsSets'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.next_token = map.get('NextToken')
        self.dhcp_options_sets = []
        if map.get('DhcpOptionsSets') is not None:
            for k in map.get('DhcpOptionsSets'):
                temp_model = ListDhcpOptionsSetsResponseDhcpOptionsSets()
                self.dhcp_options_sets.append(temp_model.from_map(k))
        else:
            self.dhcp_options_sets = None
        return self


class ListDhcpOptionsSetsResponseDhcpOptionsSetsDhcpOptions(TeaModel):
    def __init__(self, domain_name_servers=None, domain_name=None):
        self.domain_name_servers = domain_name_servers
        self.domain_name = domain_name

    def validate(self):
        self.validate_required(self.domain_name_servers, 'domain_name_servers')
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainNameServers'] = self.domain_name_servers
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.domain_name_servers = map.get('DomainNameServers')
        self.domain_name = map.get('DomainName')
        return self


class ListDhcpOptionsSetsResponseDhcpOptionsSets(TeaModel):
    def __init__(self, dhcp_options_set_name=None, dhcp_options_set_description=None, owner_id=None, status=None,
                 dhcp_options_set_id=None, associate_vpc_count=None, dhcp_options=None):
        self.dhcp_options_set_name = dhcp_options_set_name
        self.dhcp_options_set_description = dhcp_options_set_description
        self.owner_id = owner_id
        self.status = status
        self.dhcp_options_set_id = dhcp_options_set_id
        self.associate_vpc_count = associate_vpc_count
        self.dhcp_options = dhcp_options  # type: ListDhcpOptionsSetsResponseDhcpOptionsSetsDhcpOptions

    def validate(self):
        self.validate_required(self.dhcp_options_set_name, 'dhcp_options_set_name')
        self.validate_required(self.dhcp_options_set_description, 'dhcp_options_set_description')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.dhcp_options_set_id, 'dhcp_options_set_id')
        self.validate_required(self.associate_vpc_count, 'associate_vpc_count')
        self.validate_required(self.dhcp_options, 'dhcp_options')
        if self.dhcp_options:
            self.dhcp_options.validate()

    def to_map(self):
        result = {}
        result['DhcpOptionsSetName'] = self.dhcp_options_set_name
        result['DhcpOptionsSetDescription'] = self.dhcp_options_set_description
        result['OwnerId'] = self.owner_id
        result['Status'] = self.status
        result['DhcpOptionsSetId'] = self.dhcp_options_set_id
        result['AssociateVpcCount'] = self.associate_vpc_count
        if self.dhcp_options is not None:
            result['DhcpOptions'] = self.dhcp_options.to_map()
        else:
            result['DhcpOptions'] = None
        return result

    def from_map(self, map={}):
        self.dhcp_options_set_name = map.get('DhcpOptionsSetName')
        self.dhcp_options_set_description = map.get('DhcpOptionsSetDescription')
        self.owner_id = map.get('OwnerId')
        self.status = map.get('Status')
        self.dhcp_options_set_id = map.get('DhcpOptionsSetId')
        self.associate_vpc_count = map.get('AssociateVpcCount')
        if map.get('DhcpOptions') is not None:
            temp_model = ListDhcpOptionsSetsResponseDhcpOptionsSetsDhcpOptions()
            self.dhcp_options = temp_model.from_map(map['DhcpOptions'])
        else:
            self.dhcp_options = None
        return self


class DetachDhcpOptionsSetFromVpcRequest(TeaModel):
    def __init__(self, region_id=None, dhcp_options_set_id=None, vpc_id=None, client_token=None, dry_run=None):
        self.region_id = region_id
        self.dhcp_options_set_id = dhcp_options_set_id
        self.vpc_id = vpc_id
        self.client_token = client_token
        self.dry_run = dry_run

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.dhcp_options_set_id, 'dhcp_options_set_id')
        self.validate_required(self.vpc_id, 'vpc_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DhcpOptionsSetId'] = self.dhcp_options_set_id
        result['VpcId'] = self.vpc_id
        result['ClientToken'] = self.client_token
        result['DryRun'] = self.dry_run
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dhcp_options_set_id = map.get('DhcpOptionsSetId')
        self.vpc_id = map.get('VpcId')
        self.client_token = map.get('ClientToken')
        self.dry_run = map.get('DryRun')
        return self


class DetachDhcpOptionsSetFromVpcResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AttachDhcpOptionsSetToVpcRequest(TeaModel):
    def __init__(self, region_id=None, dhcp_options_set_id=None, vpc_id=None, client_token=None, dry_run=None):
        self.region_id = region_id
        self.dhcp_options_set_id = dhcp_options_set_id
        self.vpc_id = vpc_id
        self.client_token = client_token
        self.dry_run = dry_run

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.dhcp_options_set_id, 'dhcp_options_set_id')
        self.validate_required(self.vpc_id, 'vpc_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DhcpOptionsSetId'] = self.dhcp_options_set_id
        result['VpcId'] = self.vpc_id
        result['ClientToken'] = self.client_token
        result['DryRun'] = self.dry_run
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dhcp_options_set_id = map.get('DhcpOptionsSetId')
        self.vpc_id = map.get('VpcId')
        self.client_token = map.get('ClientToken')
        self.dry_run = map.get('DryRun')
        return self


class AttachDhcpOptionsSetToVpcResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteDhcpOptionsSetRequest(TeaModel):
    def __init__(self, region_id=None, dhcp_options_set_id=None, client_token=None, dry_run=None):
        self.region_id = region_id
        self.dhcp_options_set_id = dhcp_options_set_id
        self.client_token = client_token
        self.dry_run = dry_run

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.dhcp_options_set_id, 'dhcp_options_set_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DhcpOptionsSetId'] = self.dhcp_options_set_id
        result['ClientToken'] = self.client_token
        result['DryRun'] = self.dry_run
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dhcp_options_set_id = map.get('DhcpOptionsSetId')
        self.client_token = map.get('ClientToken')
        self.dry_run = map.get('DryRun')
        return self


class DeleteDhcpOptionsSetResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, pricing_cycle=None, duration=None, instance_type=None):
        self.region_id = region_id
        self.instance_id = instance_id
        self.pricing_cycle = pricing_cycle
        self.duration = duration
        self.instance_type = instance_type

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.pricing_cycle, 'pricing_cycle')
        self.validate_required(self.duration, 'duration')
        self.validate_required(self.instance_type, 'instance_type')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['InstanceId'] = self.instance_id
        result['PricingCycle'] = self.pricing_cycle
        result['Duration'] = self.duration
        result['InstanceType'] = self.instance_type
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.instance_id = map.get('InstanceId')
        self.pricing_cycle = map.get('PricingCycle')
        self.duration = map.get('Duration')
        self.instance_type = map.get('InstanceType')
        return self


class RenewInstanceResponse(TeaModel):
    def __init__(self, request_id=None, order_id=None):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['OrderId'] = self.order_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.order_id = map.get('OrderId')
        return self


class DescribeInstanceAutoRenewAttributeRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, instance_type=None, renewal_status=None, page_size=None,
                 page_number=None):
        self.region_id = region_id
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.renewal_status = renewal_status
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.instance_type, 'instance_type')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['InstanceId'] = self.instance_id
        result['InstanceType'] = self.instance_type
        result['RenewalStatus'] = self.renewal_status
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.instance_id = map.get('InstanceId')
        self.instance_type = map.get('InstanceType')
        self.renewal_status = map.get('RenewalStatus')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescribeInstanceAutoRenewAttributeResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_size=None, page_number=None,
                 instance_renew_attributes=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_size = page_size
        self.page_number = page_number
        self.instance_renew_attributes = instance_renew_attributes  # type: DescribeInstanceAutoRenewAttributeResponseInstanceRenewAttributes

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.instance_renew_attributes, 'instance_renew_attributes')
        if self.instance_renew_attributes:
            self.instance_renew_attributes.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        if self.instance_renew_attributes is not None:
            result['InstanceRenewAttributes'] = self.instance_renew_attributes.to_map()
        else:
            result['InstanceRenewAttributes'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        if map.get('InstanceRenewAttributes') is not None:
            temp_model = DescribeInstanceAutoRenewAttributeResponseInstanceRenewAttributes()
            self.instance_renew_attributes = temp_model.from_map(map['InstanceRenewAttributes'])
        else:
            self.instance_renew_attributes = None
        return self


class DescribeInstanceAutoRenewAttributeResponseInstanceRenewAttributesInstanceRenewAttribute(TeaModel):
    def __init__(self, instance_id=None, renewal_status=None, duration=None, pricing_cycle=None):
        self.instance_id = instance_id
        self.renewal_status = renewal_status
        self.duration = duration
        self.pricing_cycle = pricing_cycle

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.renewal_status, 'renewal_status')
        self.validate_required(self.duration, 'duration')
        self.validate_required(self.pricing_cycle, 'pricing_cycle')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['RenewalStatus'] = self.renewal_status
        result['Duration'] = self.duration
        result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.renewal_status = map.get('RenewalStatus')
        self.duration = map.get('Duration')
        self.pricing_cycle = map.get('PricingCycle')
        return self


class DescribeInstanceAutoRenewAttributeResponseInstanceRenewAttributes(TeaModel):
    def __init__(self, instance_renew_attribute=None):
        self.instance_renew_attribute = instance_renew_attribute

    def validate(self):
        self.validate_required(self.instance_renew_attribute, 'instance_renew_attribute')
        if self.instance_renew_attribute:
            for k in self.instance_renew_attribute:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['InstanceRenewAttribute'] = []
        if self.instance_renew_attribute is not None:
            for k in self.instance_renew_attribute:
                result['InstanceRenewAttribute'].append(k.to_map() if k else None)
        else:
            result['InstanceRenewAttribute'] = None
        return result

    def from_map(self, map={}):
        self.instance_renew_attribute = []
        if map.get('InstanceRenewAttribute') is not None:
            for k in map.get('InstanceRenewAttribute'):
                temp_model = DescribeInstanceAutoRenewAttributeResponseInstanceRenewAttributesInstanceRenewAttribute()
                self.instance_renew_attribute.append(temp_model.from_map(k))
        else:
            self.instance_renew_attribute = None
        return self


class ModifyInstanceAutoRenewalAttributeRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, pricing_cycle=None, duration=None, instance_type=None,
                 client_token=None, renewal_status=None):
        self.region_id = region_id
        self.instance_id = instance_id
        self.pricing_cycle = pricing_cycle
        self.duration = duration
        self.instance_type = instance_type
        self.client_token = client_token
        self.renewal_status = renewal_status

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.pricing_cycle, 'pricing_cycle')
        self.validate_required(self.duration, 'duration')
        self.validate_required(self.instance_type, 'instance_type')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['InstanceId'] = self.instance_id
        result['PricingCycle'] = self.pricing_cycle
        result['Duration'] = self.duration
        result['InstanceType'] = self.instance_type
        result['ClientToken'] = self.client_token
        result['RenewalStatus'] = self.renewal_status
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.instance_id = map.get('InstanceId')
        self.pricing_cycle = map.get('PricingCycle')
        self.duration = map.get('Duration')
        self.instance_type = map.get('InstanceType')
        self.client_token = map.get('ClientToken')
        self.renewal_status = map.get('RenewalStatus')
        return self


class ModifyInstanceAutoRenewalAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ReleaseEipSegmentAddressRequest(TeaModel):
    def __init__(self, region_id=None, segment_instance_id=None, client_token=None):
        self.region_id = region_id
        self.segment_instance_id = segment_instance_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.segment_instance_id, 'segment_instance_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['SegmentInstanceId'] = self.segment_instance_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.segment_instance_id = map.get('SegmentInstanceId')
        self.client_token = map.get('ClientToken')
        return self


class ReleaseEipSegmentAddressResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeEipSegmentRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, segment_instance_id=None, page_number=None,
                 page_size=None):
        self.client_token = client_token
        self.region_id = region_id
        self.segment_instance_id = segment_instance_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['SegmentInstanceId'] = self.segment_instance_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.segment_instance_id = map.get('SegmentInstanceId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeEipSegmentResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, eip_segments=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.eip_segments = eip_segments  # type: DescribeEipSegmentResponseEipSegments

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.eip_segments, 'eip_segments')
        if self.eip_segments:
            self.eip_segments.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.eip_segments is not None:
            result['EipSegments'] = self.eip_segments.to_map()
        else:
            result['EipSegments'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('EipSegments') is not None:
            temp_model = DescribeEipSegmentResponseEipSegments()
            self.eip_segments = temp_model.from_map(map['EipSegments'])
        else:
            self.eip_segments = None
        return self


class DescribeEipSegmentResponseEipSegmentsEipSegment(TeaModel):
    def __init__(self, instance_id=None, segment=None, status=None, region_id=None, ip_count=None, name=None,
                 descritpion=None, creation_time=None):
        self.instance_id = instance_id
        self.segment = segment
        self.status = status
        self.region_id = region_id
        self.ip_count = ip_count
        self.name = name
        self.descritpion = descritpion
        self.creation_time = creation_time

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.segment, 'segment')
        self.validate_required(self.status, 'status')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ip_count, 'ip_count')
        self.validate_required(self.name, 'name')
        self.validate_required(self.descritpion, 'descritpion')
        self.validate_required(self.creation_time, 'creation_time')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['Segment'] = self.segment
        result['Status'] = self.status
        result['RegionId'] = self.region_id
        result['IpCount'] = self.ip_count
        result['Name'] = self.name
        result['Descritpion'] = self.descritpion
        result['CreationTime'] = self.creation_time
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.segment = map.get('Segment')
        self.status = map.get('Status')
        self.region_id = map.get('RegionId')
        self.ip_count = map.get('IpCount')
        self.name = map.get('Name')
        self.descritpion = map.get('Descritpion')
        self.creation_time = map.get('CreationTime')
        return self


class DescribeEipSegmentResponseEipSegments(TeaModel):
    def __init__(self, eip_segment=None):
        self.eip_segment = eip_segment

    def validate(self):
        self.validate_required(self.eip_segment, 'eip_segment')
        if self.eip_segment:
            for k in self.eip_segment:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EipSegment'] = []
        if self.eip_segment is not None:
            for k in self.eip_segment:
                result['EipSegment'].append(k.to_map() if k else None)
        else:
            result['EipSegment'] = None
        return result

    def from_map(self, map={}):
        self.eip_segment = []
        if map.get('EipSegment') is not None:
            for k in map.get('EipSegment'):
                temp_model = DescribeEipSegmentResponseEipSegmentsEipSegment()
                self.eip_segment.append(temp_model.from_map(k))
        else:
            self.eip_segment = None
        return self


class AllocateEipSegmentAddressRequest(TeaModel):
    def __init__(self, client_token=None, bandwidth=None, region_id=None, eip_mask=None, netmode=None,
                 internet_charge_type=None, resource_group_id=None, isp=None):
        self.client_token = client_token
        self.bandwidth = bandwidth
        self.region_id = region_id
        self.eip_mask = eip_mask
        self.netmode = netmode
        self.internet_charge_type = internet_charge_type
        self.resource_group_id = resource_group_id
        self.isp = isp

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.eip_mask, 'eip_mask')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['Bandwidth'] = self.bandwidth
        result['RegionId'] = self.region_id
        result['EipMask'] = self.eip_mask
        result['Netmode'] = self.netmode
        result['InternetChargeType'] = self.internet_charge_type
        result['ResourceGroupId'] = self.resource_group_id
        result['Isp'] = self.isp
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.bandwidth = map.get('Bandwidth')
        self.region_id = map.get('RegionId')
        self.eip_mask = map.get('EipMask')
        self.netmode = map.get('Netmode')
        self.internet_charge_type = map.get('InternetChargeType')
        self.resource_group_id = map.get('ResourceGroupId')
        self.isp = map.get('Isp')
        return self


class AllocateEipSegmentAddressResponse(TeaModel):
    def __init__(self, request_id=None, eip_segment_instance_id=None, order_id=None):
        self.request_id = request_id
        self.eip_segment_instance_id = eip_segment_instance_id
        self.order_id = order_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.eip_segment_instance_id, 'eip_segment_instance_id')
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['EipSegmentInstanceId'] = self.eip_segment_instance_id
        result['OrderId'] = self.order_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.eip_segment_instance_id = map.get('EipSegmentInstanceId')
        self.order_id = map.get('OrderId')
        return self


class UnassociateVpcCidrBlockRequest(TeaModel):
    def __init__(self, region_id=None, vpc_id=None, secondary_cidr_block=None):
        self.region_id = region_id
        self.vpc_id = vpc_id
        self.secondary_cidr_block = secondary_cidr_block

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpc_id, 'vpc_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VpcId'] = self.vpc_id
        result['SecondaryCidrBlock'] = self.secondary_cidr_block
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vpc_id = map.get('VpcId')
        self.secondary_cidr_block = map.get('SecondaryCidrBlock')
        return self


class UnassociateVpcCidrBlockResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AssociateVpcCidrBlockRequest(TeaModel):
    def __init__(self, region_id=None, vpc_id=None, secondary_cidr_block=None):
        self.region_id = region_id
        self.vpc_id = vpc_id
        self.secondary_cidr_block = secondary_cidr_block

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpc_id, 'vpc_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VpcId'] = self.vpc_id
        result['SecondaryCidrBlock'] = self.secondary_cidr_block
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vpc_id = map.get('VpcId')
        self.secondary_cidr_block = map.get('SecondaryCidrBlock')
        return self


class AssociateVpcCidrBlockResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeRouterInterfaceAttributeRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None):
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.instance_id = map.get('InstanceId')
        return self


class DescribeRouterInterfaceAttributeResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, success=None, router_interface_id=None,
                 opposite_region_id=None, role=None, spec=None, name=None, description=None, router_id=None, router_type=None,
                 creation_time=None, gmt_modified=None, end_time=None, charge_type=None, status=None, business_status=None,
                 connected_time=None, opposite_interface_id=None, opposite_interface_spec=None, opposite_interface_status=None,
                 opposite_interface_business_status=None, opposite_router_id=None, opposite_router_type=None, opposite_interface_owner_id=None,
                 access_point_id=None, opposite_access_point_id=None, health_check_source_ip=None, health_check_target_ip=None,
                 opposite_vpc_instance_id=None, bandwidth=None, vpc_instance_id=None, opposite_bandwidth=None, has_reservation_data=None,
                 reservation_bandwidth=None, reservation_internet_charge_type=None, reservation_active_time=None,
                 reservation_order_type=None, cross_border=None, hc_threshold=None, hc_rate=None, health_check_status=None):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.success = success
        self.router_interface_id = router_interface_id
        self.opposite_region_id = opposite_region_id
        self.role = role
        self.spec = spec
        self.name = name
        self.description = description
        self.router_id = router_id
        self.router_type = router_type
        self.creation_time = creation_time
        self.gmt_modified = gmt_modified
        self.end_time = end_time
        self.charge_type = charge_type
        self.status = status
        self.business_status = business_status
        self.connected_time = connected_time
        self.opposite_interface_id = opposite_interface_id
        self.opposite_interface_spec = opposite_interface_spec
        self.opposite_interface_status = opposite_interface_status
        self.opposite_interface_business_status = opposite_interface_business_status
        self.opposite_router_id = opposite_router_id
        self.opposite_router_type = opposite_router_type
        self.opposite_interface_owner_id = opposite_interface_owner_id
        self.access_point_id = access_point_id
        self.opposite_access_point_id = opposite_access_point_id
        self.health_check_source_ip = health_check_source_ip
        self.health_check_target_ip = health_check_target_ip
        self.opposite_vpc_instance_id = opposite_vpc_instance_id
        self.bandwidth = bandwidth
        self.vpc_instance_id = vpc_instance_id
        self.opposite_bandwidth = opposite_bandwidth
        self.has_reservation_data = has_reservation_data
        self.reservation_bandwidth = reservation_bandwidth
        self.reservation_internet_charge_type = reservation_internet_charge_type
        self.reservation_active_time = reservation_active_time
        self.reservation_order_type = reservation_order_type
        self.cross_border = cross_border
        self.hc_threshold = hc_threshold
        self.hc_rate = hc_rate
        self.health_check_status = health_check_status

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.success, 'success')
        self.validate_required(self.router_interface_id, 'router_interface_id')
        self.validate_required(self.opposite_region_id, 'opposite_region_id')
        self.validate_required(self.role, 'role')
        self.validate_required(self.spec, 'spec')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.router_id, 'router_id')
        self.validate_required(self.router_type, 'router_type')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.gmt_modified, 'gmt_modified')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.charge_type, 'charge_type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.business_status, 'business_status')
        self.validate_required(self.connected_time, 'connected_time')
        self.validate_required(self.opposite_interface_id, 'opposite_interface_id')
        self.validate_required(self.opposite_interface_spec, 'opposite_interface_spec')
        self.validate_required(self.opposite_interface_status, 'opposite_interface_status')
        self.validate_required(self.opposite_interface_business_status, 'opposite_interface_business_status')
        self.validate_required(self.opposite_router_id, 'opposite_router_id')
        self.validate_required(self.opposite_router_type, 'opposite_router_type')
        self.validate_required(self.opposite_interface_owner_id, 'opposite_interface_owner_id')
        self.validate_required(self.access_point_id, 'access_point_id')
        self.validate_required(self.opposite_access_point_id, 'opposite_access_point_id')
        self.validate_required(self.health_check_source_ip, 'health_check_source_ip')
        self.validate_required(self.health_check_target_ip, 'health_check_target_ip')
        self.validate_required(self.opposite_vpc_instance_id, 'opposite_vpc_instance_id')
        self.validate_required(self.bandwidth, 'bandwidth')
        self.validate_required(self.vpc_instance_id, 'vpc_instance_id')
        self.validate_required(self.opposite_bandwidth, 'opposite_bandwidth')
        self.validate_required(self.has_reservation_data, 'has_reservation_data')
        self.validate_required(self.reservation_bandwidth, 'reservation_bandwidth')
        self.validate_required(self.reservation_internet_charge_type, 'reservation_internet_charge_type')
        self.validate_required(self.reservation_active_time, 'reservation_active_time')
        self.validate_required(self.reservation_order_type, 'reservation_order_type')
        self.validate_required(self.cross_border, 'cross_border')
        self.validate_required(self.hc_threshold, 'hc_threshold')
        self.validate_required(self.hc_rate, 'hc_rate')
        self.validate_required(self.health_check_status, 'health_check_status')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        result['Success'] = self.success
        result['RouterInterfaceId'] = self.router_interface_id
        result['OppositeRegionId'] = self.opposite_region_id
        result['Role'] = self.role
        result['Spec'] = self.spec
        result['Name'] = self.name
        result['Description'] = self.description
        result['RouterId'] = self.router_id
        result['RouterType'] = self.router_type
        result['CreationTime'] = self.creation_time
        result['GmtModified'] = self.gmt_modified
        result['EndTime'] = self.end_time
        result['ChargeType'] = self.charge_type
        result['Status'] = self.status
        result['BusinessStatus'] = self.business_status
        result['ConnectedTime'] = self.connected_time
        result['OppositeInterfaceId'] = self.opposite_interface_id
        result['OppositeInterfaceSpec'] = self.opposite_interface_spec
        result['OppositeInterfaceStatus'] = self.opposite_interface_status
        result['OppositeInterfaceBusinessStatus'] = self.opposite_interface_business_status
        result['OppositeRouterId'] = self.opposite_router_id
        result['OppositeRouterType'] = self.opposite_router_type
        result['OppositeInterfaceOwnerId'] = self.opposite_interface_owner_id
        result['AccessPointId'] = self.access_point_id
        result['OppositeAccessPointId'] = self.opposite_access_point_id
        result['HealthCheckSourceIp'] = self.health_check_source_ip
        result['HealthCheckTargetIp'] = self.health_check_target_ip
        result['OppositeVpcInstanceId'] = self.opposite_vpc_instance_id
        result['Bandwidth'] = self.bandwidth
        result['VpcInstanceId'] = self.vpc_instance_id
        result['OppositeBandwidth'] = self.opposite_bandwidth
        result['HasReservationData'] = self.has_reservation_data
        result['ReservationBandwidth'] = self.reservation_bandwidth
        result['ReservationInternetChargeType'] = self.reservation_internet_charge_type
        result['ReservationActiveTime'] = self.reservation_active_time
        result['ReservationOrderType'] = self.reservation_order_type
        result['CrossBorder'] = self.cross_border
        result['HcThreshold'] = self.hc_threshold
        result['HcRate'] = self.hc_rate
        result['HealthCheckStatus'] = self.health_check_status
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.success = map.get('Success')
        self.router_interface_id = map.get('RouterInterfaceId')
        self.opposite_region_id = map.get('OppositeRegionId')
        self.role = map.get('Role')
        self.spec = map.get('Spec')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.router_id = map.get('RouterId')
        self.router_type = map.get('RouterType')
        self.creation_time = map.get('CreationTime')
        self.gmt_modified = map.get('GmtModified')
        self.end_time = map.get('EndTime')
        self.charge_type = map.get('ChargeType')
        self.status = map.get('Status')
        self.business_status = map.get('BusinessStatus')
        self.connected_time = map.get('ConnectedTime')
        self.opposite_interface_id = map.get('OppositeInterfaceId')
        self.opposite_interface_spec = map.get('OppositeInterfaceSpec')
        self.opposite_interface_status = map.get('OppositeInterfaceStatus')
        self.opposite_interface_business_status = map.get('OppositeInterfaceBusinessStatus')
        self.opposite_router_id = map.get('OppositeRouterId')
        self.opposite_router_type = map.get('OppositeRouterType')
        self.opposite_interface_owner_id = map.get('OppositeInterfaceOwnerId')
        self.access_point_id = map.get('AccessPointId')
        self.opposite_access_point_id = map.get('OppositeAccessPointId')
        self.health_check_source_ip = map.get('HealthCheckSourceIp')
        self.health_check_target_ip = map.get('HealthCheckTargetIp')
        self.opposite_vpc_instance_id = map.get('OppositeVpcInstanceId')
        self.bandwidth = map.get('Bandwidth')
        self.vpc_instance_id = map.get('VpcInstanceId')
        self.opposite_bandwidth = map.get('OppositeBandwidth')
        self.has_reservation_data = map.get('HasReservationData')
        self.reservation_bandwidth = map.get('ReservationBandwidth')
        self.reservation_internet_charge_type = map.get('ReservationInternetChargeType')
        self.reservation_active_time = map.get('ReservationActiveTime')
        self.reservation_order_type = map.get('ReservationOrderType')
        self.cross_border = map.get('CrossBorder')
        self.hc_threshold = map.get('HcThreshold')
        self.hc_rate = map.get('HcRate')
        self.health_check_status = map.get('HealthCheckStatus')
        return self


class DeleteExpressCloudConnectionRequest(TeaModel):
    def __init__(self, region_id=None, ecc_id=None):
        self.region_id = region_id
        self.ecc_id = ecc_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ecc_id, 'ecc_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['EccId'] = self.ecc_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ecc_id = map.get('EccId')
        return self


class DeleteExpressCloudConnectionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CancelExpressCloudConnectionRequest(TeaModel):
    def __init__(self, region_id=None, ecc_id=None):
        self.region_id = region_id
        self.ecc_id = ecc_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ecc_id, 'ecc_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['EccId'] = self.ecc_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ecc_id = map.get('EccId')
        return self


class CancelExpressCloudConnectionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeletionProtectionRequest(TeaModel):
    def __init__(self, protection_enable=None, type=None, instance_id=None, client_token=None, region_id=None):
        self.protection_enable = protection_enable
        self.type = type
        self.instance_id = instance_id
        self.client_token = client_token
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.protection_enable, 'protection_enable')
        self.validate_required(self.type, 'type')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['ProtectionEnable'] = self.protection_enable
        result['Type'] = self.type
        result['InstanceId'] = self.instance_id
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.protection_enable = map.get('ProtectionEnable')
        self.type = map.get('Type')
        self.instance_id = map.get('InstanceId')
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        return self


class DeletionProtectionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeEipGatewayInfoRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.region_id = map.get('RegionId')
        return self


class DescribeEipGatewayInfoResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, eip_infos=None):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.eip_infos = eip_infos  # type: DescribeEipGatewayInfoResponseEipInfos

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.eip_infos, 'eip_infos')
        if self.eip_infos:
            self.eip_infos.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        if self.eip_infos is not None:
            result['EipInfos'] = self.eip_infos.to_map()
        else:
            result['EipInfos'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('EipInfos') is not None:
            temp_model = DescribeEipGatewayInfoResponseEipInfos()
            self.eip_infos = temp_model.from_map(map['EipInfos'])
        else:
            self.eip_infos = None
        return self


class DescribeEipGatewayInfoResponseEipInfosEipInfo(TeaModel):
    def __init__(self, ip=None, ip_gw=None, ip_mask=None):
        self.ip = ip
        self.ip_gw = ip_gw
        self.ip_mask = ip_mask

    def validate(self):
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.ip_gw, 'ip_gw')
        self.validate_required(self.ip_mask, 'ip_mask')

    def to_map(self):
        result = {}
        result['Ip'] = self.ip
        result['IpGw'] = self.ip_gw
        result['IpMask'] = self.ip_mask
        return result

    def from_map(self, map={}):
        self.ip = map.get('Ip')
        self.ip_gw = map.get('IpGw')
        self.ip_mask = map.get('IpMask')
        return self


class DescribeEipGatewayInfoResponseEipInfos(TeaModel):
    def __init__(self, eip_info=None):
        self.eip_info = eip_info

    def validate(self):
        self.validate_required(self.eip_info, 'eip_info')
        if self.eip_info:
            for k in self.eip_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EipInfo'] = []
        if self.eip_info is not None:
            for k in self.eip_info:
                result['EipInfo'].append(k.to_map() if k else None)
        else:
            result['EipInfo'] = None
        return result

    def from_map(self, map={}):
        self.eip_info = []
        if map.get('EipInfo') is not None:
            for k in map.get('EipInfo'):
                temp_model = DescribeEipGatewayInfoResponseEipInfosEipInfo()
                self.eip_info.append(temp_model.from_map(k))
        else:
            self.eip_info = None
        return self


class ModifyBgpPeerAttributeRequest(TeaModel):
    def __init__(self, region_id=None, bgp_peer_id=None, bgp_group_id=None, peer_ip_address=None, enable_bfd=None,
                 client_token=None, bfd_multi_hop=None):
        self.region_id = region_id
        self.bgp_peer_id = bgp_peer_id
        self.bgp_group_id = bgp_group_id
        self.peer_ip_address = peer_ip_address
        self.enable_bfd = enable_bfd
        self.client_token = client_token
        self.bfd_multi_hop = bfd_multi_hop

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bgp_peer_id, 'bgp_peer_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['BgpPeerId'] = self.bgp_peer_id
        result['BgpGroupId'] = self.bgp_group_id
        result['PeerIpAddress'] = self.peer_ip_address
        result['EnableBfd'] = self.enable_bfd
        result['ClientToken'] = self.client_token
        result['BfdMultiHop'] = self.bfd_multi_hop
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.bgp_peer_id = map.get('BgpPeerId')
        self.bgp_group_id = map.get('BgpGroupId')
        self.peer_ip_address = map.get('PeerIpAddress')
        self.enable_bfd = map.get('EnableBfd')
        self.client_token = map.get('ClientToken')
        self.bfd_multi_hop = map.get('BfdMultiHop')
        return self


class ModifyBgpPeerAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeVpnSslServerLogsRequest(TeaModel):
    def __init__(self, region_id=None, vpn_ssl_server_id=None, ssl_vpn_client_cert_id=None, from_=None, to=None,
                 minute_period=None, page_number=None, page_size=None):
        self.region_id = region_id
        self.vpn_ssl_server_id = vpn_ssl_server_id
        self.ssl_vpn_client_cert_id = ssl_vpn_client_cert_id
        self.from_ = from_
        self.to = to
        self.minute_period = minute_period
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpn_ssl_server_id, 'vpn_ssl_server_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VpnSslServerId'] = self.vpn_ssl_server_id
        result['SslVpnClientCertId'] = self.ssl_vpn_client_cert_id
        result['From'] = self.from_
        result['To'] = self.to
        result['MinutePeriod'] = self.minute_period
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vpn_ssl_server_id = map.get('VpnSslServerId')
        self.ssl_vpn_client_cert_id = map.get('SslVpnClientCertId')
        self.from_ = map.get('From')
        self.to = map.get('To')
        self.minute_period = map.get('MinutePeriod')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeVpnSslServerLogsResponse(TeaModel):
    def __init__(self, request_id=None, count=None, is_completed=None, page_number=None, page_size=None, data=None):
        self.request_id = request_id
        self.count = count
        self.is_completed = is_completed
        self.page_number = page_number
        self.page_size = page_size
        self.data = data  # type: DescribeVpnSslServerLogsResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.count, 'count')
        self.validate_required(self.is_completed, 'is_completed')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Count'] = self.count
        result['IsCompleted'] = self.is_completed
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.count = map.get('Count')
        self.is_completed = map.get('IsCompleted')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('Data') is not None:
            temp_model = DescribeVpnSslServerLogsResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class DescribeVpnSslServerLogsResponseData(TeaModel):
    def __init__(self, logs=None):
        self.logs = logs

    def validate(self):
        self.validate_required(self.logs, 'logs')

    def to_map(self):
        result = {}
        result['Logs'] = self.logs
        return result

    def from_map(self, map={}):
        self.logs = map.get('Logs')
        return self


class ModifyExpressCloudConnectionBandwidthRequest(TeaModel):
    def __init__(self, region_id=None, bandwidth=None, ecc_id=None):
        self.region_id = region_id
        self.bandwidth = bandwidth
        self.ecc_id = ecc_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ecc_id, 'ecc_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Bandwidth'] = self.bandwidth
        result['EccId'] = self.ecc_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.bandwidth = map.get('Bandwidth')
        self.ecc_id = map.get('EccId')
        return self


class ModifyExpressCloudConnectionBandwidthResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyExpressCloudConnectionAttributeRequest(TeaModel):
    def __init__(self, description=None, region_id=None, name=None, ecc_id=None, bgp_as=None, pe_ip=None, ce_ip=None):
        self.description = description
        self.region_id = region_id
        self.name = name
        self.ecc_id = ecc_id
        self.bgp_as = bgp_as
        self.pe_ip = pe_ip
        self.ce_ip = ce_ip

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ecc_id, 'ecc_id')

    def to_map(self):
        result = {}
        result['Description'] = self.description
        result['RegionId'] = self.region_id
        result['Name'] = self.name
        result['EccId'] = self.ecc_id
        result['BgpAs'] = self.bgp_as
        result['PeIp'] = self.pe_ip
        result['CeIp'] = self.ce_ip
        return result

    def from_map(self, map={}):
        self.description = map.get('Description')
        self.region_id = map.get('RegionId')
        self.name = map.get('Name')
        self.ecc_id = map.get('EccId')
        self.bgp_as = map.get('BgpAs')
        self.pe_ip = map.get('PeIp')
        self.ce_ip = map.get('CeIp')
        return self


class ModifyExpressCloudConnectionAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeExpressCloudConnectionsRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None, filter=None):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.filter = filter

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        else:
            result['Filter'] = None
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.filter = []
        if map.get('Filter') is not None:
            for k in map.get('Filter'):
                temp_model = DescribeExpressCloudConnectionsRequestFilter()
                self.filter.append(temp_model.from_map(k))
        else:
            self.filter = None
        return self


class DescribeExpressCloudConnectionsRequestFilter(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class DescribeExpressCloudConnectionsResponse(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None,
                 express_cloud_connection_set=None):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.express_cloud_connection_set = express_cloud_connection_set  # type: DescribeExpressCloudConnectionsResponseExpressCloudConnectionSet

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.express_cloud_connection_set, 'express_cloud_connection_set')
        if self.express_cloud_connection_set:
            self.express_cloud_connection_set.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        if self.express_cloud_connection_set is not None:
            result['ExpressCloudConnectionSet'] = self.express_cloud_connection_set.to_map()
        else:
            result['ExpressCloudConnectionSet'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        if map.get('ExpressCloudConnectionSet') is not None:
            temp_model = DescribeExpressCloudConnectionsResponseExpressCloudConnectionSet()
            self.express_cloud_connection_set = temp_model.from_map(map['ExpressCloudConnectionSet'])
        else:
            self.express_cloud_connection_set = None
        return self


class DescribeExpressCloudConnectionsResponseExpressCloudConnectionSetExpressCloudConnectionTypeVirtualBorderRouterModelsVirtualBorderRouterModel(TeaModel):
    def __init__(self, instance_id=None, access_point_id=None, physical_connection_id=None):
        self.instance_id = instance_id
        self.access_point_id = access_point_id
        self.physical_connection_id = physical_connection_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.access_point_id, 'access_point_id')
        self.validate_required(self.physical_connection_id, 'physical_connection_id')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['AccessPointId'] = self.access_point_id
        result['PhysicalConnectionId'] = self.physical_connection_id
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.access_point_id = map.get('AccessPointId')
        self.physical_connection_id = map.get('PhysicalConnectionId')
        return self


class DescribeExpressCloudConnectionsResponseExpressCloudConnectionSetExpressCloudConnectionTypeVirtualBorderRouterModels(TeaModel):
    def __init__(self, virtual_border_router_model=None):
        self.virtual_border_router_model = virtual_border_router_model

    def validate(self):
        self.validate_required(self.virtual_border_router_model, 'virtual_border_router_model')
        if self.virtual_border_router_model:
            for k in self.virtual_border_router_model:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['VirtualBorderRouterModel'] = []
        if self.virtual_border_router_model is not None:
            for k in self.virtual_border_router_model:
                result['VirtualBorderRouterModel'].append(k.to_map() if k else None)
        else:
            result['VirtualBorderRouterModel'] = None
        return result

    def from_map(self, map={}):
        self.virtual_border_router_model = []
        if map.get('VirtualBorderRouterModel') is not None:
            for k in map.get('VirtualBorderRouterModel'):
                temp_model = DescribeExpressCloudConnectionsResponseExpressCloudConnectionSetExpressCloudConnectionTypeVirtualBorderRouterModelsVirtualBorderRouterModel()
                self.virtual_border_router_model.append(temp_model.from_map(k))
        else:
            self.virtual_border_router_model = None
        return self


class DescribeExpressCloudConnectionsResponseExpressCloudConnectionSetExpressCloudConnectionType(TeaModel):
    def __init__(self, instance_id=None, status=None, name=None, description=None, gmt_create=None, gmt_modify=None,
                 peer_city=None, peer_location=None, port_type=None, bandwidth=None, distance=None, redundant_ecc_id=None,
                 circuit_code=None, isp=None, type=None, idc_sp=None, business_status=None, has_reservation_data=None,
                 reservation_bandwidth=None, reservation_internet_charge_type=None, reservation_active_time=None,
                 reservation_order_type=None, application_type=None, application_id=None, application_status=None,
                 application_bandwidth=None, end_time=None, charge_type=None, contact_tel=None, contact_mail=None, idcard_no=None,
                 estimated_time=None, bgp_as=None, pe_ip=None, ce_ip=None, construction_period=None,
                 virtual_border_router_models=None):
        self.instance_id = instance_id
        self.status = status
        self.name = name
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modify = gmt_modify
        self.peer_city = peer_city
        self.peer_location = peer_location
        self.port_type = port_type
        self.bandwidth = bandwidth
        self.distance = distance
        self.redundant_ecc_id = redundant_ecc_id
        self.circuit_code = circuit_code
        self.isp = isp
        self.type = type
        self.idc_sp = idc_sp
        self.business_status = business_status
        self.has_reservation_data = has_reservation_data
        self.reservation_bandwidth = reservation_bandwidth
        self.reservation_internet_charge_type = reservation_internet_charge_type
        self.reservation_active_time = reservation_active_time
        self.reservation_order_type = reservation_order_type
        self.application_type = application_type
        self.application_id = application_id
        self.application_status = application_status
        self.application_bandwidth = application_bandwidth
        self.end_time = end_time
        self.charge_type = charge_type
        self.contact_tel = contact_tel
        self.contact_mail = contact_mail
        self.idcard_no = idcard_no
        self.estimated_time = estimated_time
        self.bgp_as = bgp_as
        self.pe_ip = pe_ip
        self.ce_ip = ce_ip
        self.construction_period = construction_period
        self.virtual_border_router_models = virtual_border_router_models  # type: DescribeExpressCloudConnectionsResponseExpressCloudConnectionSetExpressCloudConnectionTypeVirtualBorderRouterModels

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.gmt_create, 'gmt_create')
        self.validate_required(self.gmt_modify, 'gmt_modify')
        self.validate_required(self.peer_city, 'peer_city')
        self.validate_required(self.peer_location, 'peer_location')
        self.validate_required(self.port_type, 'port_type')
        self.validate_required(self.bandwidth, 'bandwidth')
        self.validate_required(self.distance, 'distance')
        self.validate_required(self.redundant_ecc_id, 'redundant_ecc_id')
        self.validate_required(self.circuit_code, 'circuit_code')
        self.validate_required(self.isp, 'isp')
        self.validate_required(self.type, 'type')
        self.validate_required(self.idc_sp, 'idc_sp')
        self.validate_required(self.business_status, 'business_status')
        self.validate_required(self.has_reservation_data, 'has_reservation_data')
        self.validate_required(self.reservation_bandwidth, 'reservation_bandwidth')
        self.validate_required(self.reservation_internet_charge_type, 'reservation_internet_charge_type')
        self.validate_required(self.reservation_active_time, 'reservation_active_time')
        self.validate_required(self.reservation_order_type, 'reservation_order_type')
        self.validate_required(self.application_type, 'application_type')
        self.validate_required(self.application_id, 'application_id')
        self.validate_required(self.application_status, 'application_status')
        self.validate_required(self.application_bandwidth, 'application_bandwidth')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.charge_type, 'charge_type')
        self.validate_required(self.contact_tel, 'contact_tel')
        self.validate_required(self.contact_mail, 'contact_mail')
        self.validate_required(self.idcard_no, 'idcard_no')
        self.validate_required(self.estimated_time, 'estimated_time')
        self.validate_required(self.bgp_as, 'bgp_as')
        self.validate_required(self.pe_ip, 'pe_ip')
        self.validate_required(self.ce_ip, 'ce_ip')
        self.validate_required(self.construction_period, 'construction_period')
        self.validate_required(self.virtual_border_router_models, 'virtual_border_router_models')
        if self.virtual_border_router_models:
            self.virtual_border_router_models.validate()

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['Status'] = self.status
        result['Name'] = self.name
        result['Description'] = self.description
        result['GmtCreate'] = self.gmt_create
        result['GmtModify'] = self.gmt_modify
        result['PeerCity'] = self.peer_city
        result['PeerLocation'] = self.peer_location
        result['PortType'] = self.port_type
        result['Bandwidth'] = self.bandwidth
        result['Distance'] = self.distance
        result['RedundantEccId'] = self.redundant_ecc_id
        result['CircuitCode'] = self.circuit_code
        result['Isp'] = self.isp
        result['Type'] = self.type
        result['IdcSP'] = self.idc_sp
        result['BusinessStatus'] = self.business_status
        result['HasReservationData'] = self.has_reservation_data
        result['ReservationBandwidth'] = self.reservation_bandwidth
        result['ReservationInternetChargeType'] = self.reservation_internet_charge_type
        result['ReservationActiveTime'] = self.reservation_active_time
        result['ReservationOrderType'] = self.reservation_order_type
        result['ApplicationType'] = self.application_type
        result['ApplicationId'] = self.application_id
        result['ApplicationStatus'] = self.application_status
        result['ApplicationBandwidth'] = self.application_bandwidth
        result['EndTime'] = self.end_time
        result['ChargeType'] = self.charge_type
        result['ContactTel'] = self.contact_tel
        result['ContactMail'] = self.contact_mail
        result['IDCardNo'] = self.idcard_no
        result['EstimatedTime'] = self.estimated_time
        result['BgpAs'] = self.bgp_as
        result['PeIp'] = self.pe_ip
        result['CeIp'] = self.ce_ip
        result['ConstructionPeriod'] = self.construction_period
        if self.virtual_border_router_models is not None:
            result['VirtualBorderRouterModels'] = self.virtual_border_router_models.to_map()
        else:
            result['VirtualBorderRouterModels'] = None
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.status = map.get('Status')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.gmt_create = map.get('GmtCreate')
        self.gmt_modify = map.get('GmtModify')
        self.peer_city = map.get('PeerCity')
        self.peer_location = map.get('PeerLocation')
        self.port_type = map.get('PortType')
        self.bandwidth = map.get('Bandwidth')
        self.distance = map.get('Distance')
        self.redundant_ecc_id = map.get('RedundantEccId')
        self.circuit_code = map.get('CircuitCode')
        self.isp = map.get('Isp')
        self.type = map.get('Type')
        self.idc_sp = map.get('IdcSP')
        self.business_status = map.get('BusinessStatus')
        self.has_reservation_data = map.get('HasReservationData')
        self.reservation_bandwidth = map.get('ReservationBandwidth')
        self.reservation_internet_charge_type = map.get('ReservationInternetChargeType')
        self.reservation_active_time = map.get('ReservationActiveTime')
        self.reservation_order_type = map.get('ReservationOrderType')
        self.application_type = map.get('ApplicationType')
        self.application_id = map.get('ApplicationId')
        self.application_status = map.get('ApplicationStatus')
        self.application_bandwidth = map.get('ApplicationBandwidth')
        self.end_time = map.get('EndTime')
        self.charge_type = map.get('ChargeType')
        self.contact_tel = map.get('ContactTel')
        self.contact_mail = map.get('ContactMail')
        self.idcard_no = map.get('IDCardNo')
        self.estimated_time = map.get('EstimatedTime')
        self.bgp_as = map.get('BgpAs')
        self.pe_ip = map.get('PeIp')
        self.ce_ip = map.get('CeIp')
        self.construction_period = map.get('ConstructionPeriod')
        if map.get('VirtualBorderRouterModels') is not None:
            temp_model = DescribeExpressCloudConnectionsResponseExpressCloudConnectionSetExpressCloudConnectionTypeVirtualBorderRouterModels()
            self.virtual_border_router_models = temp_model.from_map(map['VirtualBorderRouterModels'])
        else:
            self.virtual_border_router_models = None
        return self


class DescribeExpressCloudConnectionsResponseExpressCloudConnectionSet(TeaModel):
    def __init__(self, express_cloud_connection_type=None):
        self.express_cloud_connection_type = express_cloud_connection_type

    def validate(self):
        self.validate_required(self.express_cloud_connection_type, 'express_cloud_connection_type')
        if self.express_cloud_connection_type:
            for k in self.express_cloud_connection_type:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ExpressCloudConnectionType'] = []
        if self.express_cloud_connection_type is not None:
            for k in self.express_cloud_connection_type:
                result['ExpressCloudConnectionType'].append(k.to_map() if k else None)
        else:
            result['ExpressCloudConnectionType'] = None
        return result

    def from_map(self, map={}):
        self.express_cloud_connection_type = []
        if map.get('ExpressCloudConnectionType') is not None:
            for k in map.get('ExpressCloudConnectionType'):
                temp_model = DescribeExpressCloudConnectionsResponseExpressCloudConnectionSetExpressCloudConnectionType()
                self.express_cloud_connection_type.append(temp_model.from_map(k))
        else:
            self.express_cloud_connection_type = None
        return self


class CreateExpressCloudConnectionRequest(TeaModel):
    def __init__(self, region_id=None, name=None, description=None, peer_city=None, peer_location=None, idc_sp=None,
                 port_type=None, bandwidth=None, contact_tel=None, contact_mail=None, idcard_no=None, redundant_ecc_id=None):
        self.region_id = region_id
        self.name = name
        self.description = description
        self.peer_city = peer_city
        self.peer_location = peer_location
        self.idc_sp = idc_sp
        self.port_type = port_type
        self.bandwidth = bandwidth
        self.contact_tel = contact_tel
        self.contact_mail = contact_mail
        self.idcard_no = idcard_no
        self.redundant_ecc_id = redundant_ecc_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.peer_location, 'peer_location')
        self.validate_required(self.idc_sp, 'idc_sp')
        self.validate_required(self.bandwidth, 'bandwidth')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Name'] = self.name
        result['Description'] = self.description
        result['PeerCity'] = self.peer_city
        result['PeerLocation'] = self.peer_location
        result['IdcSP'] = self.idc_sp
        result['PortType'] = self.port_type
        result['Bandwidth'] = self.bandwidth
        result['ContactTel'] = self.contact_tel
        result['ContactMail'] = self.contact_mail
        result['IDCardNo'] = self.idcard_no
        result['RedundantEccId'] = self.redundant_ecc_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.peer_city = map.get('PeerCity')
        self.peer_location = map.get('PeerLocation')
        self.idc_sp = map.get('IdcSP')
        self.port_type = map.get('PortType')
        self.bandwidth = map.get('Bandwidth')
        self.contact_tel = map.get('ContactTel')
        self.contact_mail = map.get('ContactMail')
        self.idcard_no = map.get('IDCardNo')
        self.redundant_ecc_id = map.get('RedundantEccId')
        return self


class CreateExpressCloudConnectionResponse(TeaModel):
    def __init__(self, request_id=None, ecc_id=None):
        self.request_id = request_id
        self.ecc_id = ecc_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.ecc_id, 'ecc_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['EccId'] = self.ecc_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.ecc_id = map.get('EccId')
        return self


class UpdateNetworkAclEntriesRequest(TeaModel):
    def __init__(self, ingress_acl_entries=None, egress_acl_entries=None, update_ingress_acl_entries=None,
                 update_egress_acl_entries=None, network_acl_id=None, region_id=None, client_token=None):
        self.ingress_acl_entries = ingress_acl_entries
        self.egress_acl_entries = egress_acl_entries
        self.update_ingress_acl_entries = update_ingress_acl_entries
        self.update_egress_acl_entries = update_egress_acl_entries
        self.network_acl_id = network_acl_id
        self.region_id = region_id
        self.client_token = client_token

    def validate(self):
        if self.ingress_acl_entries:
            for k in self.ingress_acl_entries:
                if k:
                    k.validate()
        if self.egress_acl_entries:
            for k in self.egress_acl_entries:
                if k:
                    k.validate()
        self.validate_required(self.network_acl_id, 'network_acl_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['IngressAclEntries'] = []
        if self.ingress_acl_entries is not None:
            for k in self.ingress_acl_entries:
                result['IngressAclEntries'].append(k.to_map() if k else None)
        else:
            result['IngressAclEntries'] = None
        result['EgressAclEntries'] = []
        if self.egress_acl_entries is not None:
            for k in self.egress_acl_entries:
                result['EgressAclEntries'].append(k.to_map() if k else None)
        else:
            result['EgressAclEntries'] = None
        result['UpdateIngressAclEntries'] = self.update_ingress_acl_entries
        result['UpdateEgressAclEntries'] = self.update_egress_acl_entries
        result['NetworkAclId'] = self.network_acl_id
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.ingress_acl_entries = []
        if map.get('IngressAclEntries') is not None:
            for k in map.get('IngressAclEntries'):
                temp_model = UpdateNetworkAclEntriesRequestIngressAclEntries()
                self.ingress_acl_entries.append(temp_model.from_map(k))
        else:
            self.ingress_acl_entries = None
        self.egress_acl_entries = []
        if map.get('EgressAclEntries') is not None:
            for k in map.get('EgressAclEntries'):
                temp_model = UpdateNetworkAclEntriesRequestEgressAclEntries()
                self.egress_acl_entries.append(temp_model.from_map(k))
        else:
            self.egress_acl_entries = None
        self.update_ingress_acl_entries = map.get('UpdateIngressAclEntries')
        self.update_egress_acl_entries = map.get('UpdateEgressAclEntries')
        self.network_acl_id = map.get('NetworkAclId')
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        return self


class UpdateNetworkAclEntriesRequestIngressAclEntries(TeaModel):
    def __init__(self, network_acl_entry_name=None, network_acl_entry_id=None, policy=None, protocol=None,
                 source_cidr_ip=None, port=None, entry_type=None, description=None):
        self.network_acl_entry_name = network_acl_entry_name
        self.network_acl_entry_id = network_acl_entry_id
        self.policy = policy
        self.protocol = protocol
        self.source_cidr_ip = source_cidr_ip
        self.port = port
        self.entry_type = entry_type
        self.description = description

    def validate(self):
        self.validate_required(self.network_acl_entry_name, 'network_acl_entry_name')
        self.validate_required(self.network_acl_entry_id, 'network_acl_entry_id')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.source_cidr_ip, 'source_cidr_ip')
        self.validate_required(self.port, 'port')
        self.validate_required(self.entry_type, 'entry_type')
        self.validate_required(self.description, 'description')

    def to_map(self):
        result = {}
        result['NetworkAclEntryName'] = self.network_acl_entry_name
        result['NetworkAclEntryId'] = self.network_acl_entry_id
        result['Policy'] = self.policy
        result['Protocol'] = self.protocol
        result['SourceCidrIp'] = self.source_cidr_ip
        result['Port'] = self.port
        result['EntryType'] = self.entry_type
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.network_acl_entry_name = map.get('NetworkAclEntryName')
        self.network_acl_entry_id = map.get('NetworkAclEntryId')
        self.policy = map.get('Policy')
        self.protocol = map.get('Protocol')
        self.source_cidr_ip = map.get('SourceCidrIp')
        self.port = map.get('Port')
        self.entry_type = map.get('EntryType')
        self.description = map.get('Description')
        return self


class UpdateNetworkAclEntriesRequestEgressAclEntries(TeaModel):
    def __init__(self, network_acl_entry_name=None, network_acl_entry_id=None, policy=None, protocol=None,
                 destination_cidr_ip=None, port=None, entry_type=None, description=None):
        self.network_acl_entry_name = network_acl_entry_name
        self.network_acl_entry_id = network_acl_entry_id
        self.policy = policy
        self.protocol = protocol
        self.destination_cidr_ip = destination_cidr_ip
        self.port = port
        self.entry_type = entry_type
        self.description = description

    def validate(self):
        self.validate_required(self.network_acl_entry_name, 'network_acl_entry_name')
        self.validate_required(self.network_acl_entry_id, 'network_acl_entry_id')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.destination_cidr_ip, 'destination_cidr_ip')
        self.validate_required(self.port, 'port')
        self.validate_required(self.entry_type, 'entry_type')
        self.validate_required(self.description, 'description')

    def to_map(self):
        result = {}
        result['NetworkAclEntryName'] = self.network_acl_entry_name
        result['NetworkAclEntryId'] = self.network_acl_entry_id
        result['Policy'] = self.policy
        result['Protocol'] = self.protocol
        result['DestinationCidrIp'] = self.destination_cidr_ip
        result['Port'] = self.port
        result['EntryType'] = self.entry_type
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.network_acl_entry_name = map.get('NetworkAclEntryName')
        self.network_acl_entry_id = map.get('NetworkAclEntryId')
        self.policy = map.get('Policy')
        self.protocol = map.get('Protocol')
        self.destination_cidr_ip = map.get('DestinationCidrIp')
        self.port = map.get('Port')
        self.entry_type = map.get('EntryType')
        self.description = map.get('Description')
        return self


class UpdateNetworkAclEntriesResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class UnassociateNetworkAclRequest(TeaModel):
    def __init__(self, resource=None, network_acl_id=None, region_id=None, client_token=None):
        self.resource = resource
        self.network_acl_id = network_acl_id
        self.region_id = region_id
        self.client_token = client_token

    def validate(self):
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()
        self.validate_required(self.network_acl_id, 'network_acl_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        else:
            result['Resource'] = None
        result['NetworkAclId'] = self.network_acl_id
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.resource = []
        if map.get('Resource') is not None:
            for k in map.get('Resource'):
                temp_model = UnassociateNetworkAclRequestResource()
                self.resource.append(temp_model.from_map(k))
        else:
            self.resource = None
        self.network_acl_id = map.get('NetworkAclId')
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        return self


class UnassociateNetworkAclRequestResource(TeaModel):
    def __init__(self, resource_type=None, resource_id=None):
        self.resource_type = resource_type
        self.resource_id = resource_id

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['ResourceType'] = self.resource_type
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.resource_type = map.get('ResourceType')
        self.resource_id = map.get('ResourceId')
        return self


class UnassociateNetworkAclResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyNetworkAclAttributesRequest(TeaModel):
    def __init__(self, network_acl_id=None, network_acl_name=None, description=None, region_id=None,
                 client_token=None):
        self.network_acl_id = network_acl_id
        self.network_acl_name = network_acl_name
        self.description = description
        self.region_id = region_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.network_acl_id, 'network_acl_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['NetworkAclId'] = self.network_acl_id
        result['NetworkAclName'] = self.network_acl_name
        result['Description'] = self.description
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.network_acl_id = map.get('NetworkAclId')
        self.network_acl_name = map.get('NetworkAclName')
        self.description = map.get('Description')
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        return self


class ModifyNetworkAclAttributesResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeNetworkAclsRequest(TeaModel):
    def __init__(self, network_acl_id=None, network_acl_name=None, vpc_id=None, resource_type=None,
                 resource_id=None, page_number=None, page_size=None, region_id=None, client_token=None):
        self.network_acl_id = network_acl_id
        self.network_acl_name = network_acl_name
        self.vpc_id = vpc_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['NetworkAclId'] = self.network_acl_id
        result['NetworkAclName'] = self.network_acl_name
        result['VpcId'] = self.vpc_id
        result['ResourceType'] = self.resource_type
        result['ResourceId'] = self.resource_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.network_acl_id = map.get('NetworkAclId')
        self.network_acl_name = map.get('NetworkAclName')
        self.vpc_id = map.get('VpcId')
        self.resource_type = map.get('ResourceType')
        self.resource_id = map.get('ResourceId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        return self


class DescribeNetworkAclsResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, network_acls=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.network_acls = network_acls  # type: DescribeNetworkAclsResponseNetworkAcls

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.network_acls, 'network_acls')
        if self.network_acls:
            self.network_acls.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.network_acls is not None:
            result['NetworkAcls'] = self.network_acls.to_map()
        else:
            result['NetworkAcls'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('NetworkAcls') is not None:
            temp_model = DescribeNetworkAclsResponseNetworkAcls()
            self.network_acls = temp_model.from_map(map['NetworkAcls'])
        else:
            self.network_acls = None
        return self


class DescribeNetworkAclsResponseNetworkAclsNetworkAclIngressAclEntriesIngressAclEntry(TeaModel):
    def __init__(self, network_acl_entry_id=None, policy=None, protocol=None, source_cidr_ip=None, port=None,
                 entry_type=None, network_acl_entry_name=None, description=None):
        self.network_acl_entry_id = network_acl_entry_id
        self.policy = policy
        self.protocol = protocol
        self.source_cidr_ip = source_cidr_ip
        self.port = port
        self.entry_type = entry_type
        self.network_acl_entry_name = network_acl_entry_name
        self.description = description

    def validate(self):
        self.validate_required(self.network_acl_entry_id, 'network_acl_entry_id')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.source_cidr_ip, 'source_cidr_ip')
        self.validate_required(self.port, 'port')
        self.validate_required(self.entry_type, 'entry_type')
        self.validate_required(self.network_acl_entry_name, 'network_acl_entry_name')
        self.validate_required(self.description, 'description')

    def to_map(self):
        result = {}
        result['NetworkAclEntryId'] = self.network_acl_entry_id
        result['Policy'] = self.policy
        result['Protocol'] = self.protocol
        result['SourceCidrIp'] = self.source_cidr_ip
        result['Port'] = self.port
        result['EntryType'] = self.entry_type
        result['NetworkAclEntryName'] = self.network_acl_entry_name
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.network_acl_entry_id = map.get('NetworkAclEntryId')
        self.policy = map.get('Policy')
        self.protocol = map.get('Protocol')
        self.source_cidr_ip = map.get('SourceCidrIp')
        self.port = map.get('Port')
        self.entry_type = map.get('EntryType')
        self.network_acl_entry_name = map.get('NetworkAclEntryName')
        self.description = map.get('Description')
        return self


class DescribeNetworkAclsResponseNetworkAclsNetworkAclIngressAclEntries(TeaModel):
    def __init__(self, ingress_acl_entry=None):
        self.ingress_acl_entry = ingress_acl_entry

    def validate(self):
        self.validate_required(self.ingress_acl_entry, 'ingress_acl_entry')
        if self.ingress_acl_entry:
            for k in self.ingress_acl_entry:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['IngressAclEntry'] = []
        if self.ingress_acl_entry is not None:
            for k in self.ingress_acl_entry:
                result['IngressAclEntry'].append(k.to_map() if k else None)
        else:
            result['IngressAclEntry'] = None
        return result

    def from_map(self, map={}):
        self.ingress_acl_entry = []
        if map.get('IngressAclEntry') is not None:
            for k in map.get('IngressAclEntry'):
                temp_model = DescribeNetworkAclsResponseNetworkAclsNetworkAclIngressAclEntriesIngressAclEntry()
                self.ingress_acl_entry.append(temp_model.from_map(k))
        else:
            self.ingress_acl_entry = None
        return self


class DescribeNetworkAclsResponseNetworkAclsNetworkAclEgressAclEntriesEgressAclEntry(TeaModel):
    def __init__(self, network_acl_entry_id=None, policy=None, protocol=None, destination_cidr_ip=None, port=None,
                 entry_type=None, description=None, network_acl_entry_name=None):
        self.network_acl_entry_id = network_acl_entry_id
        self.policy = policy
        self.protocol = protocol
        self.destination_cidr_ip = destination_cidr_ip
        self.port = port
        self.entry_type = entry_type
        self.description = description
        self.network_acl_entry_name = network_acl_entry_name

    def validate(self):
        self.validate_required(self.network_acl_entry_id, 'network_acl_entry_id')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.destination_cidr_ip, 'destination_cidr_ip')
        self.validate_required(self.port, 'port')
        self.validate_required(self.entry_type, 'entry_type')
        self.validate_required(self.description, 'description')
        self.validate_required(self.network_acl_entry_name, 'network_acl_entry_name')

    def to_map(self):
        result = {}
        result['NetworkAclEntryId'] = self.network_acl_entry_id
        result['Policy'] = self.policy
        result['Protocol'] = self.protocol
        result['DestinationCidrIp'] = self.destination_cidr_ip
        result['Port'] = self.port
        result['EntryType'] = self.entry_type
        result['Description'] = self.description
        result['NetworkAclEntryName'] = self.network_acl_entry_name
        return result

    def from_map(self, map={}):
        self.network_acl_entry_id = map.get('NetworkAclEntryId')
        self.policy = map.get('Policy')
        self.protocol = map.get('Protocol')
        self.destination_cidr_ip = map.get('DestinationCidrIp')
        self.port = map.get('Port')
        self.entry_type = map.get('EntryType')
        self.description = map.get('Description')
        self.network_acl_entry_name = map.get('NetworkAclEntryName')
        return self


class DescribeNetworkAclsResponseNetworkAclsNetworkAclEgressAclEntries(TeaModel):
    def __init__(self, egress_acl_entry=None):
        self.egress_acl_entry = egress_acl_entry

    def validate(self):
        self.validate_required(self.egress_acl_entry, 'egress_acl_entry')
        if self.egress_acl_entry:
            for k in self.egress_acl_entry:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EgressAclEntry'] = []
        if self.egress_acl_entry is not None:
            for k in self.egress_acl_entry:
                result['EgressAclEntry'].append(k.to_map() if k else None)
        else:
            result['EgressAclEntry'] = None
        return result

    def from_map(self, map={}):
        self.egress_acl_entry = []
        if map.get('EgressAclEntry') is not None:
            for k in map.get('EgressAclEntry'):
                temp_model = DescribeNetworkAclsResponseNetworkAclsNetworkAclEgressAclEntriesEgressAclEntry()
                self.egress_acl_entry.append(temp_model.from_map(k))
        else:
            self.egress_acl_entry = None
        return self


class DescribeNetworkAclsResponseNetworkAclsNetworkAclResourcesResource(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, status=None):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.status = status

    def validate(self):
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['ResourceId'] = self.resource_id
        result['ResourceType'] = self.resource_type
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.resource_id = map.get('ResourceId')
        self.resource_type = map.get('ResourceType')
        self.status = map.get('Status')
        return self


class DescribeNetworkAclsResponseNetworkAclsNetworkAclResources(TeaModel):
    def __init__(self, resource=None):
        self.resource = resource

    def validate(self):
        self.validate_required(self.resource, 'resource')
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        else:
            result['Resource'] = None
        return result

    def from_map(self, map={}):
        self.resource = []
        if map.get('Resource') is not None:
            for k in map.get('Resource'):
                temp_model = DescribeNetworkAclsResponseNetworkAclsNetworkAclResourcesResource()
                self.resource.append(temp_model.from_map(k))
        else:
            self.resource = None
        return self


class DescribeNetworkAclsResponseNetworkAclsNetworkAcl(TeaModel):
    def __init__(self, network_acl_id=None, region_id=None, network_acl_name=None, description=None, vpc_id=None,
                 creation_time=None, status=None, owner_id=None, ingress_acl_entries=None, egress_acl_entries=None,
                 resources=None):
        self.network_acl_id = network_acl_id
        self.region_id = region_id
        self.network_acl_name = network_acl_name
        self.description = description
        self.vpc_id = vpc_id
        self.creation_time = creation_time
        self.status = status
        self.owner_id = owner_id
        self.ingress_acl_entries = ingress_acl_entries  # type: DescribeNetworkAclsResponseNetworkAclsNetworkAclIngressAclEntries
        self.egress_acl_entries = egress_acl_entries  # type: DescribeNetworkAclsResponseNetworkAclsNetworkAclEgressAclEntries
        self.resources = resources  # type: DescribeNetworkAclsResponseNetworkAclsNetworkAclResources

    def validate(self):
        self.validate_required(self.network_acl_id, 'network_acl_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.network_acl_name, 'network_acl_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.ingress_acl_entries, 'ingress_acl_entries')
        if self.ingress_acl_entries:
            self.ingress_acl_entries.validate()
        self.validate_required(self.egress_acl_entries, 'egress_acl_entries')
        if self.egress_acl_entries:
            self.egress_acl_entries.validate()
        self.validate_required(self.resources, 'resources')
        if self.resources:
            self.resources.validate()

    def to_map(self):
        result = {}
        result['NetworkAclId'] = self.network_acl_id
        result['RegionId'] = self.region_id
        result['NetworkAclName'] = self.network_acl_name
        result['Description'] = self.description
        result['VpcId'] = self.vpc_id
        result['CreationTime'] = self.creation_time
        result['Status'] = self.status
        result['OwnerId'] = self.owner_id
        if self.ingress_acl_entries is not None:
            result['IngressAclEntries'] = self.ingress_acl_entries.to_map()
        else:
            result['IngressAclEntries'] = None
        if self.egress_acl_entries is not None:
            result['EgressAclEntries'] = self.egress_acl_entries.to_map()
        else:
            result['EgressAclEntries'] = None
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        else:
            result['Resources'] = None
        return result

    def from_map(self, map={}):
        self.network_acl_id = map.get('NetworkAclId')
        self.region_id = map.get('RegionId')
        self.network_acl_name = map.get('NetworkAclName')
        self.description = map.get('Description')
        self.vpc_id = map.get('VpcId')
        self.creation_time = map.get('CreationTime')
        self.status = map.get('Status')
        self.owner_id = map.get('OwnerId')
        if map.get('IngressAclEntries') is not None:
            temp_model = DescribeNetworkAclsResponseNetworkAclsNetworkAclIngressAclEntries()
            self.ingress_acl_entries = temp_model.from_map(map['IngressAclEntries'])
        else:
            self.ingress_acl_entries = None
        if map.get('EgressAclEntries') is not None:
            temp_model = DescribeNetworkAclsResponseNetworkAclsNetworkAclEgressAclEntries()
            self.egress_acl_entries = temp_model.from_map(map['EgressAclEntries'])
        else:
            self.egress_acl_entries = None
        if map.get('Resources') is not None:
            temp_model = DescribeNetworkAclsResponseNetworkAclsNetworkAclResources()
            self.resources = temp_model.from_map(map['Resources'])
        else:
            self.resources = None
        return self


class DescribeNetworkAclsResponseNetworkAcls(TeaModel):
    def __init__(self, network_acl=None):
        self.network_acl = network_acl

    def validate(self):
        self.validate_required(self.network_acl, 'network_acl')
        if self.network_acl:
            for k in self.network_acl:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['NetworkAcl'] = []
        if self.network_acl is not None:
            for k in self.network_acl:
                result['NetworkAcl'].append(k.to_map() if k else None)
        else:
            result['NetworkAcl'] = None
        return result

    def from_map(self, map={}):
        self.network_acl = []
        if map.get('NetworkAcl') is not None:
            for k in map.get('NetworkAcl'):
                temp_model = DescribeNetworkAclsResponseNetworkAclsNetworkAcl()
                self.network_acl.append(temp_model.from_map(k))
        else:
            self.network_acl = None
        return self


class DescribeNetworkAclAttributesRequest(TeaModel):
    def __init__(self, network_acl_id=None, region_id=None, client_token=None):
        self.network_acl_id = network_acl_id
        self.region_id = region_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.network_acl_id, 'network_acl_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['NetworkAclId'] = self.network_acl_id
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.network_acl_id = map.get('NetworkAclId')
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        return self


class DescribeNetworkAclAttributesResponse(TeaModel):
    def __init__(self, request_id=None, network_acl_attribute=None):
        self.request_id = request_id
        self.network_acl_attribute = network_acl_attribute  # type: DescribeNetworkAclAttributesResponseNetworkAclAttribute

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.network_acl_attribute, 'network_acl_attribute')
        if self.network_acl_attribute:
            self.network_acl_attribute.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.network_acl_attribute is not None:
            result['NetworkAclAttribute'] = self.network_acl_attribute.to_map()
        else:
            result['NetworkAclAttribute'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('NetworkAclAttribute') is not None:
            temp_model = DescribeNetworkAclAttributesResponseNetworkAclAttribute()
            self.network_acl_attribute = temp_model.from_map(map['NetworkAclAttribute'])
        else:
            self.network_acl_attribute = None
        return self


class DescribeNetworkAclAttributesResponseNetworkAclAttributeIngressAclEntriesIngressAclEntry(TeaModel):
    def __init__(self, network_acl_entry_id=None, policy=None, protocol=None, source_cidr_ip=None, port=None,
                 entry_type=None, network_acl_entry_name=None, description=None):
        self.network_acl_entry_id = network_acl_entry_id
        self.policy = policy
        self.protocol = protocol
        self.source_cidr_ip = source_cidr_ip
        self.port = port
        self.entry_type = entry_type
        self.network_acl_entry_name = network_acl_entry_name
        self.description = description

    def validate(self):
        self.validate_required(self.network_acl_entry_id, 'network_acl_entry_id')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.source_cidr_ip, 'source_cidr_ip')
        self.validate_required(self.port, 'port')
        self.validate_required(self.entry_type, 'entry_type')
        self.validate_required(self.network_acl_entry_name, 'network_acl_entry_name')
        self.validate_required(self.description, 'description')

    def to_map(self):
        result = {}
        result['NetworkAclEntryId'] = self.network_acl_entry_id
        result['Policy'] = self.policy
        result['Protocol'] = self.protocol
        result['SourceCidrIp'] = self.source_cidr_ip
        result['Port'] = self.port
        result['EntryType'] = self.entry_type
        result['NetworkAclEntryName'] = self.network_acl_entry_name
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.network_acl_entry_id = map.get('NetworkAclEntryId')
        self.policy = map.get('Policy')
        self.protocol = map.get('Protocol')
        self.source_cidr_ip = map.get('SourceCidrIp')
        self.port = map.get('Port')
        self.entry_type = map.get('EntryType')
        self.network_acl_entry_name = map.get('NetworkAclEntryName')
        self.description = map.get('Description')
        return self


class DescribeNetworkAclAttributesResponseNetworkAclAttributeIngressAclEntries(TeaModel):
    def __init__(self, ingress_acl_entry=None):
        self.ingress_acl_entry = ingress_acl_entry

    def validate(self):
        self.validate_required(self.ingress_acl_entry, 'ingress_acl_entry')
        if self.ingress_acl_entry:
            for k in self.ingress_acl_entry:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['IngressAclEntry'] = []
        if self.ingress_acl_entry is not None:
            for k in self.ingress_acl_entry:
                result['IngressAclEntry'].append(k.to_map() if k else None)
        else:
            result['IngressAclEntry'] = None
        return result

    def from_map(self, map={}):
        self.ingress_acl_entry = []
        if map.get('IngressAclEntry') is not None:
            for k in map.get('IngressAclEntry'):
                temp_model = DescribeNetworkAclAttributesResponseNetworkAclAttributeIngressAclEntriesIngressAclEntry()
                self.ingress_acl_entry.append(temp_model.from_map(k))
        else:
            self.ingress_acl_entry = None
        return self


class DescribeNetworkAclAttributesResponseNetworkAclAttributeEgressAclEntriesEgressAclEntry(TeaModel):
    def __init__(self, network_acl_entry_id=None, policy=None, protocol=None, destination_cidr_ip=None, port=None,
                 entry_type=None, description=None, network_acl_entry_name=None):
        self.network_acl_entry_id = network_acl_entry_id
        self.policy = policy
        self.protocol = protocol
        self.destination_cidr_ip = destination_cidr_ip
        self.port = port
        self.entry_type = entry_type
        self.description = description
        self.network_acl_entry_name = network_acl_entry_name

    def validate(self):
        self.validate_required(self.network_acl_entry_id, 'network_acl_entry_id')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.destination_cidr_ip, 'destination_cidr_ip')
        self.validate_required(self.port, 'port')
        self.validate_required(self.entry_type, 'entry_type')
        self.validate_required(self.description, 'description')
        self.validate_required(self.network_acl_entry_name, 'network_acl_entry_name')

    def to_map(self):
        result = {}
        result['NetworkAclEntryId'] = self.network_acl_entry_id
        result['Policy'] = self.policy
        result['Protocol'] = self.protocol
        result['DestinationCidrIp'] = self.destination_cidr_ip
        result['Port'] = self.port
        result['EntryType'] = self.entry_type
        result['Description'] = self.description
        result['NetworkAclEntryName'] = self.network_acl_entry_name
        return result

    def from_map(self, map={}):
        self.network_acl_entry_id = map.get('NetworkAclEntryId')
        self.policy = map.get('Policy')
        self.protocol = map.get('Protocol')
        self.destination_cidr_ip = map.get('DestinationCidrIp')
        self.port = map.get('Port')
        self.entry_type = map.get('EntryType')
        self.description = map.get('Description')
        self.network_acl_entry_name = map.get('NetworkAclEntryName')
        return self


class DescribeNetworkAclAttributesResponseNetworkAclAttributeEgressAclEntries(TeaModel):
    def __init__(self, egress_acl_entry=None):
        self.egress_acl_entry = egress_acl_entry

    def validate(self):
        self.validate_required(self.egress_acl_entry, 'egress_acl_entry')
        if self.egress_acl_entry:
            for k in self.egress_acl_entry:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EgressAclEntry'] = []
        if self.egress_acl_entry is not None:
            for k in self.egress_acl_entry:
                result['EgressAclEntry'].append(k.to_map() if k else None)
        else:
            result['EgressAclEntry'] = None
        return result

    def from_map(self, map={}):
        self.egress_acl_entry = []
        if map.get('EgressAclEntry') is not None:
            for k in map.get('EgressAclEntry'):
                temp_model = DescribeNetworkAclAttributesResponseNetworkAclAttributeEgressAclEntriesEgressAclEntry()
                self.egress_acl_entry.append(temp_model.from_map(k))
        else:
            self.egress_acl_entry = None
        return self


class DescribeNetworkAclAttributesResponseNetworkAclAttributeResourcesResource(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, status=None):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.status = status

    def validate(self):
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['ResourceId'] = self.resource_id
        result['ResourceType'] = self.resource_type
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.resource_id = map.get('ResourceId')
        self.resource_type = map.get('ResourceType')
        self.status = map.get('Status')
        return self


class DescribeNetworkAclAttributesResponseNetworkAclAttributeResources(TeaModel):
    def __init__(self, resource=None):
        self.resource = resource

    def validate(self):
        self.validate_required(self.resource, 'resource')
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        else:
            result['Resource'] = None
        return result

    def from_map(self, map={}):
        self.resource = []
        if map.get('Resource') is not None:
            for k in map.get('Resource'):
                temp_model = DescribeNetworkAclAttributesResponseNetworkAclAttributeResourcesResource()
                self.resource.append(temp_model.from_map(k))
        else:
            self.resource = None
        return self


class DescribeNetworkAclAttributesResponseNetworkAclAttribute(TeaModel):
    def __init__(self, network_acl_id=None, region_id=None, network_acl_name=None, description=None, vpc_id=None,
                 creation_time=None, status=None, owner_id=None, ingress_acl_entries=None, egress_acl_entries=None,
                 resources=None):
        self.network_acl_id = network_acl_id
        self.region_id = region_id
        self.network_acl_name = network_acl_name
        self.description = description
        self.vpc_id = vpc_id
        self.creation_time = creation_time
        self.status = status
        self.owner_id = owner_id
        self.ingress_acl_entries = ingress_acl_entries  # type: DescribeNetworkAclAttributesResponseNetworkAclAttributeIngressAclEntries
        self.egress_acl_entries = egress_acl_entries  # type: DescribeNetworkAclAttributesResponseNetworkAclAttributeEgressAclEntries
        self.resources = resources  # type: DescribeNetworkAclAttributesResponseNetworkAclAttributeResources

    def validate(self):
        self.validate_required(self.network_acl_id, 'network_acl_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.network_acl_name, 'network_acl_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.ingress_acl_entries, 'ingress_acl_entries')
        if self.ingress_acl_entries:
            self.ingress_acl_entries.validate()
        self.validate_required(self.egress_acl_entries, 'egress_acl_entries')
        if self.egress_acl_entries:
            self.egress_acl_entries.validate()
        self.validate_required(self.resources, 'resources')
        if self.resources:
            self.resources.validate()

    def to_map(self):
        result = {}
        result['NetworkAclId'] = self.network_acl_id
        result['RegionId'] = self.region_id
        result['NetworkAclName'] = self.network_acl_name
        result['Description'] = self.description
        result['VpcId'] = self.vpc_id
        result['CreationTime'] = self.creation_time
        result['Status'] = self.status
        result['OwnerId'] = self.owner_id
        if self.ingress_acl_entries is not None:
            result['IngressAclEntries'] = self.ingress_acl_entries.to_map()
        else:
            result['IngressAclEntries'] = None
        if self.egress_acl_entries is not None:
            result['EgressAclEntries'] = self.egress_acl_entries.to_map()
        else:
            result['EgressAclEntries'] = None
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        else:
            result['Resources'] = None
        return result

    def from_map(self, map={}):
        self.network_acl_id = map.get('NetworkAclId')
        self.region_id = map.get('RegionId')
        self.network_acl_name = map.get('NetworkAclName')
        self.description = map.get('Description')
        self.vpc_id = map.get('VpcId')
        self.creation_time = map.get('CreationTime')
        self.status = map.get('Status')
        self.owner_id = map.get('OwnerId')
        if map.get('IngressAclEntries') is not None:
            temp_model = DescribeNetworkAclAttributesResponseNetworkAclAttributeIngressAclEntries()
            self.ingress_acl_entries = temp_model.from_map(map['IngressAclEntries'])
        else:
            self.ingress_acl_entries = None
        if map.get('EgressAclEntries') is not None:
            temp_model = DescribeNetworkAclAttributesResponseNetworkAclAttributeEgressAclEntries()
            self.egress_acl_entries = temp_model.from_map(map['EgressAclEntries'])
        else:
            self.egress_acl_entries = None
        if map.get('Resources') is not None:
            temp_model = DescribeNetworkAclAttributesResponseNetworkAclAttributeResources()
            self.resources = temp_model.from_map(map['Resources'])
        else:
            self.resources = None
        return self


class DeleteNetworkAclRequest(TeaModel):
    def __init__(self, network_acl_id=None, region_id=None, client_token=None):
        self.network_acl_id = network_acl_id
        self.region_id = region_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.network_acl_id, 'network_acl_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['NetworkAclId'] = self.network_acl_id
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.network_acl_id = map.get('NetworkAclId')
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        return self


class DeleteNetworkAclResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateNetworkAclRequest(TeaModel):
    def __init__(self, vpc_id=None, network_acl_name=None, description=None, region_id=None, client_token=None):
        self.vpc_id = vpc_id
        self.network_acl_name = network_acl_name
        self.description = description
        self.region_id = region_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['VpcId'] = self.vpc_id
        result['NetworkAclName'] = self.network_acl_name
        result['Description'] = self.description
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.vpc_id = map.get('VpcId')
        self.network_acl_name = map.get('NetworkAclName')
        self.description = map.get('Description')
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        return self


class CreateNetworkAclResponse(TeaModel):
    def __init__(self, request_id=None, network_acl_id=None, network_acl_attribute=None):
        self.request_id = request_id
        self.network_acl_id = network_acl_id
        self.network_acl_attribute = network_acl_attribute  # type: CreateNetworkAclResponseNetworkAclAttribute

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.network_acl_id, 'network_acl_id')
        self.validate_required(self.network_acl_attribute, 'network_acl_attribute')
        if self.network_acl_attribute:
            self.network_acl_attribute.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['NetworkAclId'] = self.network_acl_id
        if self.network_acl_attribute is not None:
            result['NetworkAclAttribute'] = self.network_acl_attribute.to_map()
        else:
            result['NetworkAclAttribute'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.network_acl_id = map.get('NetworkAclId')
        if map.get('NetworkAclAttribute') is not None:
            temp_model = CreateNetworkAclResponseNetworkAclAttribute()
            self.network_acl_attribute = temp_model.from_map(map['NetworkAclAttribute'])
        else:
            self.network_acl_attribute = None
        return self


class CreateNetworkAclResponseNetworkAclAttributeIngressAclEntriesIngressAclEntry(TeaModel):
    def __init__(self, network_acl_entry_id=None, policy=None, protocol=None, source_cidr_ip=None, port=None,
                 entry_type=None, network_acl_entry_name=None, description=None):
        self.network_acl_entry_id = network_acl_entry_id
        self.policy = policy
        self.protocol = protocol
        self.source_cidr_ip = source_cidr_ip
        self.port = port
        self.entry_type = entry_type
        self.network_acl_entry_name = network_acl_entry_name
        self.description = description

    def validate(self):
        self.validate_required(self.network_acl_entry_id, 'network_acl_entry_id')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.source_cidr_ip, 'source_cidr_ip')
        self.validate_required(self.port, 'port')
        self.validate_required(self.entry_type, 'entry_type')
        self.validate_required(self.network_acl_entry_name, 'network_acl_entry_name')
        self.validate_required(self.description, 'description')

    def to_map(self):
        result = {}
        result['NetworkAclEntryId'] = self.network_acl_entry_id
        result['Policy'] = self.policy
        result['Protocol'] = self.protocol
        result['SourceCidrIp'] = self.source_cidr_ip
        result['Port'] = self.port
        result['EntryType'] = self.entry_type
        result['NetworkAclEntryName'] = self.network_acl_entry_name
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.network_acl_entry_id = map.get('NetworkAclEntryId')
        self.policy = map.get('Policy')
        self.protocol = map.get('Protocol')
        self.source_cidr_ip = map.get('SourceCidrIp')
        self.port = map.get('Port')
        self.entry_type = map.get('EntryType')
        self.network_acl_entry_name = map.get('NetworkAclEntryName')
        self.description = map.get('Description')
        return self


class CreateNetworkAclResponseNetworkAclAttributeIngressAclEntries(TeaModel):
    def __init__(self, ingress_acl_entry=None):
        self.ingress_acl_entry = ingress_acl_entry

    def validate(self):
        self.validate_required(self.ingress_acl_entry, 'ingress_acl_entry')
        if self.ingress_acl_entry:
            for k in self.ingress_acl_entry:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['IngressAclEntry'] = []
        if self.ingress_acl_entry is not None:
            for k in self.ingress_acl_entry:
                result['IngressAclEntry'].append(k.to_map() if k else None)
        else:
            result['IngressAclEntry'] = None
        return result

    def from_map(self, map={}):
        self.ingress_acl_entry = []
        if map.get('IngressAclEntry') is not None:
            for k in map.get('IngressAclEntry'):
                temp_model = CreateNetworkAclResponseNetworkAclAttributeIngressAclEntriesIngressAclEntry()
                self.ingress_acl_entry.append(temp_model.from_map(k))
        else:
            self.ingress_acl_entry = None
        return self


class CreateNetworkAclResponseNetworkAclAttributeEgressAclEntriesEgressAclEntry(TeaModel):
    def __init__(self, network_acl_entry_id=None, policy=None, protocol=None, destination_cidr_ip=None, port=None,
                 entry_type=None, description=None, network_acl_entry_name=None):
        self.network_acl_entry_id = network_acl_entry_id
        self.policy = policy
        self.protocol = protocol
        self.destination_cidr_ip = destination_cidr_ip
        self.port = port
        self.entry_type = entry_type
        self.description = description
        self.network_acl_entry_name = network_acl_entry_name

    def validate(self):
        self.validate_required(self.network_acl_entry_id, 'network_acl_entry_id')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.destination_cidr_ip, 'destination_cidr_ip')
        self.validate_required(self.port, 'port')
        self.validate_required(self.entry_type, 'entry_type')
        self.validate_required(self.description, 'description')
        self.validate_required(self.network_acl_entry_name, 'network_acl_entry_name')

    def to_map(self):
        result = {}
        result['NetworkAclEntryId'] = self.network_acl_entry_id
        result['Policy'] = self.policy
        result['Protocol'] = self.protocol
        result['DestinationCidrIp'] = self.destination_cidr_ip
        result['Port'] = self.port
        result['EntryType'] = self.entry_type
        result['Description'] = self.description
        result['NetworkAclEntryName'] = self.network_acl_entry_name
        return result

    def from_map(self, map={}):
        self.network_acl_entry_id = map.get('NetworkAclEntryId')
        self.policy = map.get('Policy')
        self.protocol = map.get('Protocol')
        self.destination_cidr_ip = map.get('DestinationCidrIp')
        self.port = map.get('Port')
        self.entry_type = map.get('EntryType')
        self.description = map.get('Description')
        self.network_acl_entry_name = map.get('NetworkAclEntryName')
        return self


class CreateNetworkAclResponseNetworkAclAttributeEgressAclEntries(TeaModel):
    def __init__(self, egress_acl_entry=None):
        self.egress_acl_entry = egress_acl_entry

    def validate(self):
        self.validate_required(self.egress_acl_entry, 'egress_acl_entry')
        if self.egress_acl_entry:
            for k in self.egress_acl_entry:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EgressAclEntry'] = []
        if self.egress_acl_entry is not None:
            for k in self.egress_acl_entry:
                result['EgressAclEntry'].append(k.to_map() if k else None)
        else:
            result['EgressAclEntry'] = None
        return result

    def from_map(self, map={}):
        self.egress_acl_entry = []
        if map.get('EgressAclEntry') is not None:
            for k in map.get('EgressAclEntry'):
                temp_model = CreateNetworkAclResponseNetworkAclAttributeEgressAclEntriesEgressAclEntry()
                self.egress_acl_entry.append(temp_model.from_map(k))
        else:
            self.egress_acl_entry = None
        return self


class CreateNetworkAclResponseNetworkAclAttributeResourcesResource(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, status=None):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.status = status

    def validate(self):
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['ResourceId'] = self.resource_id
        result['ResourceType'] = self.resource_type
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.resource_id = map.get('ResourceId')
        self.resource_type = map.get('ResourceType')
        self.status = map.get('Status')
        return self


class CreateNetworkAclResponseNetworkAclAttributeResources(TeaModel):
    def __init__(self, resource=None):
        self.resource = resource

    def validate(self):
        self.validate_required(self.resource, 'resource')
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        else:
            result['Resource'] = None
        return result

    def from_map(self, map={}):
        self.resource = []
        if map.get('Resource') is not None:
            for k in map.get('Resource'):
                temp_model = CreateNetworkAclResponseNetworkAclAttributeResourcesResource()
                self.resource.append(temp_model.from_map(k))
        else:
            self.resource = None
        return self


class CreateNetworkAclResponseNetworkAclAttribute(TeaModel):
    def __init__(self, network_acl_id=None, region_id=None, network_acl_name=None, description=None, vpc_id=None,
                 creation_time=None, status=None, ingress_acl_entries=None, egress_acl_entries=None, resources=None):
        self.network_acl_id = network_acl_id
        self.region_id = region_id
        self.network_acl_name = network_acl_name
        self.description = description
        self.vpc_id = vpc_id
        self.creation_time = creation_time
        self.status = status
        self.ingress_acl_entries = ingress_acl_entries  # type: CreateNetworkAclResponseNetworkAclAttributeIngressAclEntries
        self.egress_acl_entries = egress_acl_entries  # type: CreateNetworkAclResponseNetworkAclAttributeEgressAclEntries
        self.resources = resources  # type: CreateNetworkAclResponseNetworkAclAttributeResources

    def validate(self):
        self.validate_required(self.network_acl_id, 'network_acl_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.network_acl_name, 'network_acl_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.ingress_acl_entries, 'ingress_acl_entries')
        if self.ingress_acl_entries:
            self.ingress_acl_entries.validate()
        self.validate_required(self.egress_acl_entries, 'egress_acl_entries')
        if self.egress_acl_entries:
            self.egress_acl_entries.validate()
        self.validate_required(self.resources, 'resources')
        if self.resources:
            self.resources.validate()

    def to_map(self):
        result = {}
        result['NetworkAclId'] = self.network_acl_id
        result['RegionId'] = self.region_id
        result['NetworkAclName'] = self.network_acl_name
        result['Description'] = self.description
        result['VpcId'] = self.vpc_id
        result['CreationTime'] = self.creation_time
        result['Status'] = self.status
        if self.ingress_acl_entries is not None:
            result['IngressAclEntries'] = self.ingress_acl_entries.to_map()
        else:
            result['IngressAclEntries'] = None
        if self.egress_acl_entries is not None:
            result['EgressAclEntries'] = self.egress_acl_entries.to_map()
        else:
            result['EgressAclEntries'] = None
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        else:
            result['Resources'] = None
        return result

    def from_map(self, map={}):
        self.network_acl_id = map.get('NetworkAclId')
        self.region_id = map.get('RegionId')
        self.network_acl_name = map.get('NetworkAclName')
        self.description = map.get('Description')
        self.vpc_id = map.get('VpcId')
        self.creation_time = map.get('CreationTime')
        self.status = map.get('Status')
        if map.get('IngressAclEntries') is not None:
            temp_model = CreateNetworkAclResponseNetworkAclAttributeIngressAclEntries()
            self.ingress_acl_entries = temp_model.from_map(map['IngressAclEntries'])
        else:
            self.ingress_acl_entries = None
        if map.get('EgressAclEntries') is not None:
            temp_model = CreateNetworkAclResponseNetworkAclAttributeEgressAclEntries()
            self.egress_acl_entries = temp_model.from_map(map['EgressAclEntries'])
        else:
            self.egress_acl_entries = None
        if map.get('Resources') is not None:
            temp_model = CreateNetworkAclResponseNetworkAclAttributeResources()
            self.resources = temp_model.from_map(map['Resources'])
        else:
            self.resources = None
        return self


class CopyNetworkAclEntriesRequest(TeaModel):
    def __init__(self, region_id=None, network_acl_id=None, source_network_acl_id=None, client_token=None):
        self.region_id = region_id
        self.network_acl_id = network_acl_id
        self.source_network_acl_id = source_network_acl_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.network_acl_id, 'network_acl_id')
        self.validate_required(self.source_network_acl_id, 'source_network_acl_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['NetworkAclId'] = self.network_acl_id
        result['SourceNetworkAclId'] = self.source_network_acl_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.network_acl_id = map.get('NetworkAclId')
        self.source_network_acl_id = map.get('SourceNetworkAclId')
        self.client_token = map.get('ClientToken')
        return self


class CopyNetworkAclEntriesResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AssociateNetworkAclRequest(TeaModel):
    def __init__(self, resource=None, network_acl_id=None, region_id=None, client_token=None):
        self.resource = resource
        self.network_acl_id = network_acl_id
        self.region_id = region_id
        self.client_token = client_token

    def validate(self):
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()
        self.validate_required(self.network_acl_id, 'network_acl_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        else:
            result['Resource'] = None
        result['NetworkAclId'] = self.network_acl_id
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.resource = []
        if map.get('Resource') is not None:
            for k in map.get('Resource'):
                temp_model = AssociateNetworkAclRequestResource()
                self.resource.append(temp_model.from_map(k))
        else:
            self.resource = None
        self.network_acl_id = map.get('NetworkAclId')
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        return self


class AssociateNetworkAclRequestResource(TeaModel):
    def __init__(self, resource_type=None, resource_id=None):
        self.resource_type = resource_type
        self.resource_id = resource_id

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['ResourceType'] = self.resource_type
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.resource_type = map.get('ResourceType')
        self.resource_id = map.get('ResourceId')
        return self


class AssociateNetworkAclResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyCommonBandwidthPackageIpBandwidthRequest(TeaModel):
    def __init__(self, region_id=None, bandwidth_package_id=None, eip_id=None, bandwidth=None):
        self.region_id = region_id
        self.bandwidth_package_id = bandwidth_package_id
        self.eip_id = eip_id
        self.bandwidth = bandwidth

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bandwidth_package_id, 'bandwidth_package_id')
        self.validate_required(self.eip_id, 'eip_id')
        self.validate_required(self.bandwidth, 'bandwidth')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['BandwidthPackageId'] = self.bandwidth_package_id
        result['EipId'] = self.eip_id
        result['Bandwidth'] = self.bandwidth
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        self.eip_id = map.get('EipId')
        self.bandwidth = map.get('Bandwidth')
        return self


class ModifyCommonBandwidthPackageIpBandwidthResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CancelCommonBandwidthPackageIpBandwidthRequest(TeaModel):
    def __init__(self, region_id=None, bandwidth_package_id=None, eip_id=None):
        self.region_id = region_id
        self.bandwidth_package_id = bandwidth_package_id
        self.eip_id = eip_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bandwidth_package_id, 'bandwidth_package_id')
        self.validate_required(self.eip_id, 'eip_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['BandwidthPackageId'] = self.bandwidth_package_id
        result['EipId'] = self.eip_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        self.eip_id = map.get('EipId')
        return self


class CancelCommonBandwidthPackageIpBandwidthResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateVpnPbrRouteEntryRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, vpn_gateway_id=None, route_source=None, route_dest=None,
                 next_hop=None, weight=None, publish_vpc=None, description=None, overlay_mode=None):
        self.region_id = region_id
        self.client_token = client_token
        self.vpn_gateway_id = vpn_gateway_id
        self.route_source = route_source
        self.route_dest = route_dest
        self.next_hop = next_hop
        self.weight = weight
        self.publish_vpc = publish_vpc
        self.description = description
        self.overlay_mode = overlay_mode

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')
        self.validate_required(self.route_source, 'route_source')
        self.validate_required(self.route_dest, 'route_dest')
        self.validate_required(self.next_hop, 'next_hop')
        self.validate_required(self.weight, 'weight')
        self.validate_required(self.publish_vpc, 'publish_vpc')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['RouteSource'] = self.route_source
        result['RouteDest'] = self.route_dest
        result['NextHop'] = self.next_hop
        result['Weight'] = self.weight
        result['PublishVpc'] = self.publish_vpc
        result['Description'] = self.description
        result['OverlayMode'] = self.overlay_mode
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.route_source = map.get('RouteSource')
        self.route_dest = map.get('RouteDest')
        self.next_hop = map.get('NextHop')
        self.weight = map.get('Weight')
        self.publish_vpc = map.get('PublishVpc')
        self.description = map.get('Description')
        self.overlay_mode = map.get('OverlayMode')
        return self


class CreateVpnPbrRouteEntryResponse(TeaModel):
    def __init__(self, request_id=None, vpn_instance_id=None, route_source=None, route_dest=None, next_hop=None,
                 weight=None, overlay_mode=None, description=None, state=None, create_time=None):
        self.request_id = request_id
        self.vpn_instance_id = vpn_instance_id
        self.route_source = route_source
        self.route_dest = route_dest
        self.next_hop = next_hop
        self.weight = weight
        self.overlay_mode = overlay_mode
        self.description = description
        self.state = state
        self.create_time = create_time

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.vpn_instance_id, 'vpn_instance_id')
        self.validate_required(self.route_source, 'route_source')
        self.validate_required(self.route_dest, 'route_dest')
        self.validate_required(self.next_hop, 'next_hop')
        self.validate_required(self.weight, 'weight')
        self.validate_required(self.overlay_mode, 'overlay_mode')
        self.validate_required(self.description, 'description')
        self.validate_required(self.state, 'state')
        self.validate_required(self.create_time, 'create_time')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['VpnInstanceId'] = self.vpn_instance_id
        result['RouteSource'] = self.route_source
        result['RouteDest'] = self.route_dest
        result['NextHop'] = self.next_hop
        result['Weight'] = self.weight
        result['OverlayMode'] = self.overlay_mode
        result['Description'] = self.description
        result['State'] = self.state
        result['CreateTime'] = self.create_time
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.vpn_instance_id = map.get('VpnInstanceId')
        self.route_source = map.get('RouteSource')
        self.route_dest = map.get('RouteDest')
        self.next_hop = map.get('NextHop')
        self.weight = map.get('Weight')
        self.overlay_mode = map.get('OverlayMode')
        self.description = map.get('Description')
        self.state = map.get('State')
        self.create_time = map.get('CreateTime')
        return self


class CreateVpnRouteEntryRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, vpn_gateway_id=None, route_dest=None, next_hop=None,
                 weight=None, publish_vpc=None, description=None, overlay_mode=None):
        self.region_id = region_id
        self.client_token = client_token
        self.vpn_gateway_id = vpn_gateway_id
        self.route_dest = route_dest
        self.next_hop = next_hop
        self.weight = weight
        self.publish_vpc = publish_vpc
        self.description = description
        self.overlay_mode = overlay_mode

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')
        self.validate_required(self.route_dest, 'route_dest')
        self.validate_required(self.next_hop, 'next_hop')
        self.validate_required(self.weight, 'weight')
        self.validate_required(self.publish_vpc, 'publish_vpc')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['RouteDest'] = self.route_dest
        result['NextHop'] = self.next_hop
        result['Weight'] = self.weight
        result['PublishVpc'] = self.publish_vpc
        result['Description'] = self.description
        result['OverlayMode'] = self.overlay_mode
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.route_dest = map.get('RouteDest')
        self.next_hop = map.get('NextHop')
        self.weight = map.get('Weight')
        self.publish_vpc = map.get('PublishVpc')
        self.description = map.get('Description')
        self.overlay_mode = map.get('OverlayMode')
        return self


class CreateVpnRouteEntryResponse(TeaModel):
    def __init__(self, request_id=None, vpn_instance_id=None, route_dest=None, next_hop=None, weight=None,
                 overlay_mode=None, description=None, state=None, create_time=None):
        self.request_id = request_id
        self.vpn_instance_id = vpn_instance_id
        self.route_dest = route_dest
        self.next_hop = next_hop
        self.weight = weight
        self.overlay_mode = overlay_mode
        self.description = description
        self.state = state
        self.create_time = create_time

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.vpn_instance_id, 'vpn_instance_id')
        self.validate_required(self.route_dest, 'route_dest')
        self.validate_required(self.next_hop, 'next_hop')
        self.validate_required(self.weight, 'weight')
        self.validate_required(self.overlay_mode, 'overlay_mode')
        self.validate_required(self.description, 'description')
        self.validate_required(self.state, 'state')
        self.validate_required(self.create_time, 'create_time')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['VpnInstanceId'] = self.vpn_instance_id
        result['RouteDest'] = self.route_dest
        result['NextHop'] = self.next_hop
        result['Weight'] = self.weight
        result['OverlayMode'] = self.overlay_mode
        result['Description'] = self.description
        result['State'] = self.state
        result['CreateTime'] = self.create_time
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.vpn_instance_id = map.get('VpnInstanceId')
        self.route_dest = map.get('RouteDest')
        self.next_hop = map.get('NextHop')
        self.weight = map.get('Weight')
        self.overlay_mode = map.get('OverlayMode')
        self.description = map.get('Description')
        self.state = map.get('State')
        self.create_time = map.get('CreateTime')
        return self


class DeleteVpnPbrRouteEntryRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, vpn_gateway_id=None, route_source=None, route_dest=None,
                 next_hop=None, weight=None, overlay_mode=None):
        self.region_id = region_id
        self.client_token = client_token
        self.vpn_gateway_id = vpn_gateway_id
        self.route_source = route_source
        self.route_dest = route_dest
        self.next_hop = next_hop
        self.weight = weight
        self.overlay_mode = overlay_mode

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')
        self.validate_required(self.route_source, 'route_source')
        self.validate_required(self.route_dest, 'route_dest')
        self.validate_required(self.next_hop, 'next_hop')
        self.validate_required(self.weight, 'weight')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['RouteSource'] = self.route_source
        result['RouteDest'] = self.route_dest
        result['NextHop'] = self.next_hop
        result['Weight'] = self.weight
        result['OverlayMode'] = self.overlay_mode
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.route_source = map.get('RouteSource')
        self.route_dest = map.get('RouteDest')
        self.next_hop = map.get('NextHop')
        self.weight = map.get('Weight')
        self.overlay_mode = map.get('OverlayMode')
        return self


class DeleteVpnPbrRouteEntryResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteVpnRouteEntryRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, vpn_gateway_id=None, route_dest=None, next_hop=None,
                 weight=None, overlay_mode=None):
        self.region_id = region_id
        self.client_token = client_token
        self.vpn_gateway_id = vpn_gateway_id
        self.route_dest = route_dest
        self.next_hop = next_hop
        self.weight = weight
        self.overlay_mode = overlay_mode

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')
        self.validate_required(self.route_dest, 'route_dest')
        self.validate_required(self.next_hop, 'next_hop')
        self.validate_required(self.weight, 'weight')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['RouteDest'] = self.route_dest
        result['NextHop'] = self.next_hop
        result['Weight'] = self.weight
        result['OverlayMode'] = self.overlay_mode
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.route_dest = map.get('RouteDest')
        self.next_hop = map.get('NextHop')
        self.weight = map.get('Weight')
        self.overlay_mode = map.get('OverlayMode')
        return self


class DeleteVpnRouteEntryResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeVpnRouteEntriesRequest(TeaModel):
    def __init__(self, region_id=None, vpn_gateway_id=None, page_number=None, page_size=None, route_entry_type=None):
        self.region_id = region_id
        self.vpn_gateway_id = vpn_gateway_id
        self.page_number = page_number
        self.page_size = page_size
        self.route_entry_type = route_entry_type

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['RouteEntryType'] = self.route_entry_type
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.route_entry_type = map.get('RouteEntryType')
        return self


class DescribeVpnRouteEntriesResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, vpn_route_entries=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.vpn_route_entries = vpn_route_entries  # type: DescribeVpnRouteEntriesResponseVpnRouteEntries

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.vpn_route_entries, 'vpn_route_entries')
        if self.vpn_route_entries:
            self.vpn_route_entries.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.vpn_route_entries is not None:
            result['VpnRouteEntries'] = self.vpn_route_entries.to_map()
        else:
            result['VpnRouteEntries'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('VpnRouteEntries') is not None:
            temp_model = DescribeVpnRouteEntriesResponseVpnRouteEntries()
            self.vpn_route_entries = temp_model.from_map(map['VpnRouteEntries'])
        else:
            self.vpn_route_entries = None
        return self


class DescribeVpnRouteEntriesResponseVpnRouteEntriesVpnRouteEntry(TeaModel):
    def __init__(self, vpn_instance_id=None, route_dest=None, next_hop=None, weight=None, create_time=None,
                 state=None, as_path=None, community=None, source=None, route_entry_type=None):
        self.vpn_instance_id = vpn_instance_id
        self.route_dest = route_dest
        self.next_hop = next_hop
        self.weight = weight
        self.create_time = create_time
        self.state = state
        self.as_path = as_path
        self.community = community
        self.source = source
        self.route_entry_type = route_entry_type

    def validate(self):
        self.validate_required(self.vpn_instance_id, 'vpn_instance_id')
        self.validate_required(self.route_dest, 'route_dest')
        self.validate_required(self.next_hop, 'next_hop')
        self.validate_required(self.weight, 'weight')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.state, 'state')
        self.validate_required(self.as_path, 'as_path')
        self.validate_required(self.community, 'community')
        self.validate_required(self.source, 'source')
        self.validate_required(self.route_entry_type, 'route_entry_type')

    def to_map(self):
        result = {}
        result['VpnInstanceId'] = self.vpn_instance_id
        result['RouteDest'] = self.route_dest
        result['NextHop'] = self.next_hop
        result['Weight'] = self.weight
        result['CreateTime'] = self.create_time
        result['State'] = self.state
        result['AsPath'] = self.as_path
        result['Community'] = self.community
        result['Source'] = self.source
        result['RouteEntryType'] = self.route_entry_type
        return result

    def from_map(self, map={}):
        self.vpn_instance_id = map.get('VpnInstanceId')
        self.route_dest = map.get('RouteDest')
        self.next_hop = map.get('NextHop')
        self.weight = map.get('Weight')
        self.create_time = map.get('CreateTime')
        self.state = map.get('State')
        self.as_path = map.get('AsPath')
        self.community = map.get('Community')
        self.source = map.get('Source')
        self.route_entry_type = map.get('RouteEntryType')
        return self


class DescribeVpnRouteEntriesResponseVpnRouteEntries(TeaModel):
    def __init__(self, vpn_route_entry=None):
        self.vpn_route_entry = vpn_route_entry

    def validate(self):
        self.validate_required(self.vpn_route_entry, 'vpn_route_entry')
        if self.vpn_route_entry:
            for k in self.vpn_route_entry:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['VpnRouteEntry'] = []
        if self.vpn_route_entry is not None:
            for k in self.vpn_route_entry:
                result['VpnRouteEntry'].append(k.to_map() if k else None)
        else:
            result['VpnRouteEntry'] = None
        return result

    def from_map(self, map={}):
        self.vpn_route_entry = []
        if map.get('VpnRouteEntry') is not None:
            for k in map.get('VpnRouteEntry'):
                temp_model = DescribeVpnRouteEntriesResponseVpnRouteEntriesVpnRouteEntry()
                self.vpn_route_entry.append(temp_model.from_map(k))
        else:
            self.vpn_route_entry = None
        return self


class DescribeVpnPbrRouteEntriesRequest(TeaModel):
    def __init__(self, region_id=None, vpn_gateway_id=None, page_number=None, page_size=None):
        self.region_id = region_id
        self.vpn_gateway_id = vpn_gateway_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeVpnPbrRouteEntriesResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None,
                 vpn_pbr_route_entries=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.vpn_pbr_route_entries = vpn_pbr_route_entries  # type: DescribeVpnPbrRouteEntriesResponseVpnPbrRouteEntries

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.vpn_pbr_route_entries, 'vpn_pbr_route_entries')
        if self.vpn_pbr_route_entries:
            self.vpn_pbr_route_entries.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.vpn_pbr_route_entries is not None:
            result['VpnPbrRouteEntries'] = self.vpn_pbr_route_entries.to_map()
        else:
            result['VpnPbrRouteEntries'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('VpnPbrRouteEntries') is not None:
            temp_model = DescribeVpnPbrRouteEntriesResponseVpnPbrRouteEntries()
            self.vpn_pbr_route_entries = temp_model.from_map(map['VpnPbrRouteEntries'])
        else:
            self.vpn_pbr_route_entries = None
        return self


class DescribeVpnPbrRouteEntriesResponseVpnPbrRouteEntriesVpnPbrRouteEntry(TeaModel):
    def __init__(self, vpn_instance_id=None, route_source=None, route_dest=None, next_hop=None, weight=None,
                 create_time=None, state=None):
        self.vpn_instance_id = vpn_instance_id
        self.route_source = route_source
        self.route_dest = route_dest
        self.next_hop = next_hop
        self.weight = weight
        self.create_time = create_time
        self.state = state

    def validate(self):
        self.validate_required(self.vpn_instance_id, 'vpn_instance_id')
        self.validate_required(self.route_source, 'route_source')
        self.validate_required(self.route_dest, 'route_dest')
        self.validate_required(self.next_hop, 'next_hop')
        self.validate_required(self.weight, 'weight')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.state, 'state')

    def to_map(self):
        result = {}
        result['VpnInstanceId'] = self.vpn_instance_id
        result['RouteSource'] = self.route_source
        result['RouteDest'] = self.route_dest
        result['NextHop'] = self.next_hop
        result['Weight'] = self.weight
        result['CreateTime'] = self.create_time
        result['State'] = self.state
        return result

    def from_map(self, map={}):
        self.vpn_instance_id = map.get('VpnInstanceId')
        self.route_source = map.get('RouteSource')
        self.route_dest = map.get('RouteDest')
        self.next_hop = map.get('NextHop')
        self.weight = map.get('Weight')
        self.create_time = map.get('CreateTime')
        self.state = map.get('State')
        return self


class DescribeVpnPbrRouteEntriesResponseVpnPbrRouteEntries(TeaModel):
    def __init__(self, vpn_pbr_route_entry=None):
        self.vpn_pbr_route_entry = vpn_pbr_route_entry

    def validate(self):
        self.validate_required(self.vpn_pbr_route_entry, 'vpn_pbr_route_entry')
        if self.vpn_pbr_route_entry:
            for k in self.vpn_pbr_route_entry:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['VpnPbrRouteEntry'] = []
        if self.vpn_pbr_route_entry is not None:
            for k in self.vpn_pbr_route_entry:
                result['VpnPbrRouteEntry'].append(k.to_map() if k else None)
        else:
            result['VpnPbrRouteEntry'] = None
        return result

    def from_map(self, map={}):
        self.vpn_pbr_route_entry = []
        if map.get('VpnPbrRouteEntry') is not None:
            for k in map.get('VpnPbrRouteEntry'):
                temp_model = DescribeVpnPbrRouteEntriesResponseVpnPbrRouteEntriesVpnPbrRouteEntry()
                self.vpn_pbr_route_entry.append(temp_model.from_map(k))
        else:
            self.vpn_pbr_route_entry = None
        return self


class PublishVpnRouteEntryRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, vpn_gateway_id=None, route_dest=None, next_hop=None,
                 route_type=None, publish_vpc=None):
        self.region_id = region_id
        self.client_token = client_token
        self.vpn_gateway_id = vpn_gateway_id
        self.route_dest = route_dest
        self.next_hop = next_hop
        self.route_type = route_type
        self.publish_vpc = publish_vpc

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')
        self.validate_required(self.route_dest, 'route_dest')
        self.validate_required(self.next_hop, 'next_hop')
        self.validate_required(self.route_type, 'route_type')
        self.validate_required(self.publish_vpc, 'publish_vpc')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['RouteDest'] = self.route_dest
        result['NextHop'] = self.next_hop
        result['RouteType'] = self.route_type
        result['PublishVpc'] = self.publish_vpc
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.route_dest = map.get('RouteDest')
        self.next_hop = map.get('NextHop')
        self.route_type = map.get('RouteType')
        self.publish_vpc = map.get('PublishVpc')
        return self


class PublishVpnRouteEntryResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyVpnRouteEntryWeightRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, vpn_gateway_id=None, route_dest=None, next_hop=None,
                 weight=None, new_weight=None, overlay_mode=None):
        self.region_id = region_id
        self.client_token = client_token
        self.vpn_gateway_id = vpn_gateway_id
        self.route_dest = route_dest
        self.next_hop = next_hop
        self.weight = weight
        self.new_weight = new_weight
        self.overlay_mode = overlay_mode

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')
        self.validate_required(self.route_dest, 'route_dest')
        self.validate_required(self.next_hop, 'next_hop')
        self.validate_required(self.weight, 'weight')
        self.validate_required(self.new_weight, 'new_weight')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['RouteDest'] = self.route_dest
        result['NextHop'] = self.next_hop
        result['Weight'] = self.weight
        result['NewWeight'] = self.new_weight
        result['OverlayMode'] = self.overlay_mode
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.route_dest = map.get('RouteDest')
        self.next_hop = map.get('NextHop')
        self.weight = map.get('Weight')
        self.new_weight = map.get('NewWeight')
        self.overlay_mode = map.get('OverlayMode')
        return self


class ModifyVpnRouteEntryWeightResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyVpnPbrRouteEntryWeightRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, vpn_gateway_id=None, route_source=None, route_dest=None,
                 next_hop=None, weight=None, new_weight=None, overlay_mode=None):
        self.region_id = region_id
        self.client_token = client_token
        self.vpn_gateway_id = vpn_gateway_id
        self.route_source = route_source
        self.route_dest = route_dest
        self.next_hop = next_hop
        self.weight = weight
        self.new_weight = new_weight
        self.overlay_mode = overlay_mode

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')
        self.validate_required(self.route_source, 'route_source')
        self.validate_required(self.route_dest, 'route_dest')
        self.validate_required(self.next_hop, 'next_hop')
        self.validate_required(self.weight, 'weight')
        self.validate_required(self.new_weight, 'new_weight')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['RouteSource'] = self.route_source
        result['RouteDest'] = self.route_dest
        result['NextHop'] = self.next_hop
        result['Weight'] = self.weight
        result['NewWeight'] = self.new_weight
        result['OverlayMode'] = self.overlay_mode
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.route_source = map.get('RouteSource')
        self.route_dest = map.get('RouteDest')
        self.next_hop = map.get('NextHop')
        self.weight = map.get('Weight')
        self.new_weight = map.get('NewWeight')
        self.overlay_mode = map.get('OverlayMode')
        return self


class ModifyVpnPbrRouteEntryWeightResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribePhysicalConnectionLOARequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, instance_id=None):
        # description: The ID of the region where the leased line is deployed. ; 
        self.region_id = region_id
        # description: Optional. The token used for client authentication. ; 
        self.client_token = client_token
        # description: The instance ID of the physical connection interface. ; 
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.instance_id = map.get('InstanceId')
        return self


class DescribePhysicalConnectionLOAResponse(TeaModel):
    def __init__(self, request_id=None, physical_connection_loatype=None):
        # description: The ID of the request. ; 
        self.request_id = request_id
        # description: The LOA information of the physical connection. 
        self.physical_connection_loatype = physical_connection_loatype  # type: DescribePhysicalConnectionLOAResponsePhysicalConnectionLOAType

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.physical_connection_loatype, 'physical_connection_loatype')
        if self.physical_connection_loatype:
            self.physical_connection_loatype.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.physical_connection_loatype is not None:
            result['PhysicalConnectionLOAType'] = self.physical_connection_loatype.to_map()
        else:
            result['PhysicalConnectionLOAType'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('PhysicalConnectionLOAType') is not None:
            temp_model = DescribePhysicalConnectionLOAResponsePhysicalConnectionLOAType()
            self.physical_connection_loatype = temp_model.from_map(map['PhysicalConnectionLOAType'])
        else:
            self.physical_connection_loatype = None
        return self


class DescribePhysicalConnectionLOAResponsePhysicalConnectionLOATypePMInfoPMInfo(TeaModel):
    def __init__(self, pmname=None, pmcontact_info=None, pmcertificate_type=None, pmcertificate_no=None,
                 pmgender=None):
        # description: The name of the data center cable installation technician or representative. ; 
        self.pmname = pmname
        # description: The contact information of the data center cable installation technician or representative. ; 
        self.pmcontact_info = pmcontact_info
        # description: The type of certificate or licence held by the data center cable installation technician or representative. ; 
        self.pmcertificate_type = pmcertificate_type
        # description: The certificate or licence number of the data center cable installation technician or representative.; 
        self.pmcertificate_no = pmcertificate_no
        # description: The gender of the data center cable installation technician or representative.; 
        self.pmgender = pmgender

    def validate(self):
        self.validate_required(self.pmname, 'pmname')
        self.validate_required(self.pmcontact_info, 'pmcontact_info')
        self.validate_required(self.pmcertificate_type, 'pmcertificate_type')
        self.validate_required(self.pmcertificate_no, 'pmcertificate_no')
        self.validate_required(self.pmgender, 'pmgender')

    def to_map(self):
        result = {}
        result['PMName'] = self.pmname
        result['PMContactInfo'] = self.pmcontact_info
        result['PMCertificateType'] = self.pmcertificate_type
        result['PMCertificateNo'] = self.pmcertificate_no
        result['PMGender'] = self.pmgender
        return result

    def from_map(self, map={}):
        self.pmname = map.get('PMName')
        self.pmcontact_info = map.get('PMContactInfo')
        self.pmcertificate_type = map.get('PMCertificateType')
        self.pmcertificate_no = map.get('PMCertificateNo')
        self.pmgender = map.get('PMGender')
        return self


class DescribePhysicalConnectionLOAResponsePhysicalConnectionLOATypePMInfo(TeaModel):
    def __init__(self, pminfo=None):
        self.pminfo = pminfo

    def validate(self):
        self.validate_required(self.pminfo, 'pminfo')
        if self.pminfo:
            for k in self.pminfo:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PMInfo'] = []
        if self.pminfo is not None:
            for k in self.pminfo:
                result['PMInfo'].append(k.to_map() if k else None)
        else:
            result['PMInfo'] = None
        return result

    def from_map(self, map={}):
        self.pminfo = []
        if map.get('PMInfo') is not None:
            for k in map.get('PMInfo'):
                temp_model = DescribePhysicalConnectionLOAResponsePhysicalConnectionLOATypePMInfoPMInfo()
                self.pminfo.append(temp_model.from_map(k))
        else:
            self.pminfo = None
        return self


class DescribePhysicalConnectionLOAResponsePhysicalConnectionLOAType(TeaModel):
    def __init__(self, instance_id=None, company_name=None, company_localized_name=None, line_type=None,
                 line_code=None, line_label=None, construction_time=None, status=None, loa_url=None, si=None, pminfo=None):
        # description: The instance ID of the physical connection interface. ; 
        self.instance_id = instance_id
        # description: The name of the company that requires the leased line. ; 
        self.company_name = company_name
        # description: The company name that you set when you registered your account.; 
        self.company_localized_name = company_localized_name
        # description: The type of the physical connection.Valid values:* MSTP* Other * SDH* MPLSVPN * FIBRE; 
        self.line_type = line_type
        # description: The number of leased line.; 
        self.line_code = line_code
        # description: The label numbers of the cables at the installation site.; 
        self.line_label = line_label
        # description: The time when the the data center cable installation technician or representative will go to the installation site.; 
        self.construction_time = construction_time
        # description: The status of the physical connection interface. ; 
        self.status = status
        # description: The URL to use to download the LOA file.; 
        self.loa_url = loa_url
        # description: The name of the data center cable installation company. ; 
        self.si = si
        # description: The information about the data center cable installation technician or representative.
        self.pminfo = pminfo  # type: DescribePhysicalConnectionLOAResponsePhysicalConnectionLOATypePMInfo

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.company_name, 'company_name')
        self.validate_required(self.company_localized_name, 'company_localized_name')
        self.validate_required(self.line_type, 'line_type')
        self.validate_required(self.line_code, 'line_code')
        self.validate_required(self.line_label, 'line_label')
        self.validate_required(self.construction_time, 'construction_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.loa_url, 'loa_url')
        self.validate_required(self.si, 'si')
        self.validate_required(self.pminfo, 'pminfo')
        if self.pminfo:
            self.pminfo.validate()

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['CompanyName'] = self.company_name
        result['CompanyLocalizedName'] = self.company_localized_name
        result['LineType'] = self.line_type
        result['LineCode'] = self.line_code
        result['LineLabel'] = self.line_label
        result['ConstructionTime'] = self.construction_time
        result['Status'] = self.status
        result['LoaUrl'] = self.loa_url
        result['SI'] = self.si
        if self.pminfo is not None:
            result['PMInfo'] = self.pminfo.to_map()
        else:
            result['PMInfo'] = None
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.company_name = map.get('CompanyName')
        self.company_localized_name = map.get('CompanyLocalizedName')
        self.line_type = map.get('LineType')
        self.line_code = map.get('LineCode')
        self.line_label = map.get('LineLabel')
        self.construction_time = map.get('ConstructionTime')
        self.status = map.get('Status')
        self.loa_url = map.get('LoaUrl')
        self.si = map.get('SI')
        if map.get('PMInfo') is not None:
            temp_model = DescribePhysicalConnectionLOAResponsePhysicalConnectionLOATypePMInfo()
            self.pminfo = temp_model.from_map(map['PMInfo'])
        else:
            self.pminfo = None
        return self


class CreatePhysicalConnectionSetupOrderRequest(TeaModel):
    def __init__(self, region_id=None, access_point_id=None, line_operator=None, port_type=None,
                 redundant_physical_connection_id=None, auto_pay=None, client_token=None):
        # description: The ID of the region where the leased line is deployed. You can get the region ID by calling the DescribeRegions API.; 
        self.region_id = region_id
        # description: The ID of the access point.; 
        self.access_point_id = access_point_id
        # description: The service provider that provides the leased line. Valid values:* CT: China Telecom* CU: China Unicom* CM: China Mobile* CO: Other Chinese service providers* Equinix: Equinix* Other: Other service providers outside Mainland China; 
        self.line_operator = line_operator
        # description: Optional. The type of the leased line connection port. Valid values:* **100Base-T**: 100M electrical ports* **1000Base-T **(default value): Gigabit electrical ports* **1000Base-LX**: 1000M single-mode optical ports (10 km)* **10GBase-T**: 10GE electrical ports* **10GBase-LR**: 10GE single-mode optical ports (10km) ; 
        self.port_type = port_type
        # description: The ID of the redundant physical connection. Its status must be **Allocated**,**Confirmed**or** Enabled**. ; 
        self.redundant_physical_connection_id = redundant_physical_connection_id
        # description: Optional. Indicates whether to pay the fee automatically.Valid values: **true | false**; 
        self.auto_pay = auto_pay
        # description: Optional. The token used for client authentication.; 
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.access_point_id, 'access_point_id')
        self.validate_required(self.line_operator, 'line_operator')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['AccessPointId'] = self.access_point_id
        result['LineOperator'] = self.line_operator
        result['PortType'] = self.port_type
        result['RedundantPhysicalConnectionId'] = self.redundant_physical_connection_id
        result['AutoPay'] = self.auto_pay
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.access_point_id = map.get('AccessPointId')
        self.line_operator = map.get('LineOperator')
        self.port_type = map.get('PortType')
        self.redundant_physical_connection_id = map.get('RedundantPhysicalConnectionId')
        self.auto_pay = map.get('AutoPay')
        self.client_token = map.get('ClientToken')
        return self


class CreatePhysicalConnectionSetupOrderResponse(TeaModel):
    def __init__(self, request_id=None, order_id=None, physical_connection_id=None):
        # description: ; 
        self.request_id = request_id
        # description: The ID of the order.; 
        self.order_id = order_id
        self.physical_connection_id = physical_connection_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.physical_connection_id, 'physical_connection_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['OrderId'] = self.order_id
        result['PhysicalConnectionId'] = self.physical_connection_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.order_id = map.get('OrderId')
        self.physical_connection_id = map.get('PhysicalConnectionId')
        return self


class CreatePhysicalConnectionOccupancyOrderRequest(TeaModel):
    def __init__(self, region_id=None, physical_connection_id=None, period=None, instance_charge_type=None,
                 auto_pay=None, pricing_cycle=None, client_token=None):
        # description: The ID of the region where the leased line is deployed.; 
        self.region_id = region_id
        # description: The instance ID of the physical connection interface.; 
        self.physical_connection_id = physical_connection_id
        # description: Optional. The validity period of a Subscription.; 
        self.period = period
        # description: Optional. The billing method of the instance. Valid values:* PrePaid: Subscription. If you select this value, you must make sure that your account has enough available funds.* PostPaid (default value): Pay-As-You-Go; 
        self.instance_charge_type = instance_charge_type
        # description: Optional. Indicates whether to pay automatically. Valid values:* true (default value): Pay automatically. If you select this value, you must ensure that your account has enough available funds. Otherwise, the order that is generated is invalid.* false: Generates the order only. No fee is deducted from your account.; 
        self.auto_pay = auto_pay
        # description: Optional. The Subscription cycle. Valid values:* Month* Year; 
        self.pricing_cycle = pricing_cycle
        # description: Optional. The token used for client authentication.; 
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.physical_connection_id, 'physical_connection_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['PhysicalConnectionId'] = self.physical_connection_id
        result['Period'] = self.period
        result['InstanceChargeType'] = self.instance_charge_type
        result['AutoPay'] = self.auto_pay
        result['PricingCycle'] = self.pricing_cycle
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.physical_connection_id = map.get('PhysicalConnectionId')
        self.period = map.get('Period')
        self.instance_charge_type = map.get('InstanceChargeType')
        self.auto_pay = map.get('AutoPay')
        self.pricing_cycle = map.get('PricingCycle')
        self.client_token = map.get('ClientToken')
        return self


class CreatePhysicalConnectionOccupancyOrderResponse(TeaModel):
    def __init__(self, request_id=None):
        # description: The ID of the request.; 
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CompletePhysicalConnectionLOARequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, instance_id=None, line_code=None, line_label=None):
        # description: Optional. The token used for client authentication.; 
        self.client_token = client_token
        # description: The ID of the region where the leased line is deployed.; 
        self.region_id = region_id
        # description: The instance ID of the physical connection interface.; 
        self.instance_id = instance_id
        # description: The number of the leased line.; 
        self.line_code = line_code
        # description: The label numbers of cables at the installation site.; 
        self.line_label = line_label

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.line_code, 'line_code')
        self.validate_required(self.line_label, 'line_label')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['InstanceId'] = self.instance_id
        result['LineCode'] = self.line_code
        result['LineLabel'] = self.line_label
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.instance_id = map.get('InstanceId')
        self.line_code = map.get('LineCode')
        self.line_label = map.get('LineLabel')
        return self


class CompletePhysicalConnectionLOAResponse(TeaModel):
    def __init__(self, request_id=None):
        # description: The ID of the request.; 
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ApplyPhysicalConnectionLOARequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, bandwidth=None, peer_location=None, instance_id=None,
                 company_name=None, line_type=None, si=None, construction_time=None, pminfo=None):
        # description: Optional. The token used for client authentication.; 
        self.client_token = client_token
        # description: The ID of the region to which the physical connection interface belongs.; 
        self.region_id = region_id
        # description: Optional. The bandwidth value of the physical connection.; 
        self.bandwidth = bandwidth
        # description: The location where the leased line is deployed.; 
        self.peer_location = peer_location
        # description: The instance ID of the physical connection interface.; 
        self.instance_id = instance_id
        # description: The name of the company that requires the physical connection.; 
        self.company_name = company_name
        # description: The type of leased line. ; 
        self.line_type = line_type
        # description: The name of the installation company.; 
        self.si = si
        # description: The date and time when the data cable installation technician or representative will go to the installation site.; 
        self.construction_time = construction_time
        self.pminfo = pminfo

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.company_name, 'company_name')
        self.validate_required(self.line_type, 'line_type')
        self.validate_required(self.si, 'si')
        self.validate_required(self.construction_time, 'construction_time')
        if self.pminfo:
            for k in self.pminfo:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['Bandwidth'] = self.bandwidth
        result['PeerLocation'] = self.peer_location
        result['InstanceId'] = self.instance_id
        result['CompanyName'] = self.company_name
        result['LineType'] = self.line_type
        result['Si'] = self.si
        result['ConstructionTime'] = self.construction_time
        result['PMInfo'] = []
        if self.pminfo is not None:
            for k in self.pminfo:
                result['PMInfo'].append(k.to_map() if k else None)
        else:
            result['PMInfo'] = None
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.bandwidth = map.get('Bandwidth')
        self.peer_location = map.get('PeerLocation')
        self.instance_id = map.get('InstanceId')
        self.company_name = map.get('CompanyName')
        self.line_type = map.get('LineType')
        self.si = map.get('Si')
        self.construction_time = map.get('ConstructionTime')
        self.pminfo = []
        if map.get('PMInfo') is not None:
            for k in map.get('PMInfo'):
                temp_model = ApplyPhysicalConnectionLOARequestPMInfo()
                self.pminfo.append(temp_model.from_map(k))
        else:
            self.pminfo = None
        return self


class ApplyPhysicalConnectionLOARequestPMInfo(TeaModel):
    def __init__(self, pmname=None, pmcontact_info=None, pmcertificate_type=None, pmcertificate_no=None,
                 pmgender=None):
        self.pmname = pmname
        self.pmcontact_info = pmcontact_info
        self.pmcertificate_type = pmcertificate_type
        self.pmcertificate_no = pmcertificate_no
        self.pmgender = pmgender

    def validate(self):
        self.validate_required(self.pmname, 'pmname')
        self.validate_required(self.pmcontact_info, 'pmcontact_info')
        self.validate_required(self.pmcertificate_type, 'pmcertificate_type')
        self.validate_required(self.pmcertificate_no, 'pmcertificate_no')
        self.validate_required(self.pmgender, 'pmgender')

    def to_map(self):
        result = {}
        result['PMName'] = self.pmname
        result['PMContactInfo'] = self.pmcontact_info
        result['PMCertificateType'] = self.pmcertificate_type
        result['PMCertificateNo'] = self.pmcertificate_no
        result['PMGender'] = self.pmgender
        return result

    def from_map(self, map={}):
        self.pmname = map.get('PMName')
        self.pmcontact_info = map.get('PMContactInfo')
        self.pmcertificate_type = map.get('PMCertificateType')
        self.pmcertificate_no = map.get('PMCertificateNo')
        self.pmgender = map.get('PMGender')
        return self


class ApplyPhysicalConnectionLOAResponse(TeaModel):
    def __init__(self, request_id=None):
        # description: The ID of the request.; 
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ConvertBandwidthPackageRequest(TeaModel):
    def __init__(self, bandwidth_package_id=None, region_id=None, client_token=None):
        self.bandwidth_package_id = bandwidth_package_id
        self.region_id = region_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.bandwidth_package_id, 'bandwidth_package_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['BandwidthPackageId'] = self.bandwidth_package_id
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        return self


class ConvertBandwidthPackageResponse(TeaModel):
    def __init__(self, request_id=None, convert_instance_id=None):
        self.request_id = request_id
        self.convert_instance_id = convert_instance_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.convert_instance_id, 'convert_instance_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ConvertInstanceId'] = self.convert_instance_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.convert_instance_id = map.get('ConvertInstanceId')
        return self


class ModifyRouteEntryRequest(TeaModel):
    def __init__(self, region_id=None, route_entry_name=None, route_entry_id=None, description=None):
        self.region_id = region_id
        self.route_entry_name = route_entry_name
        self.route_entry_id = route_entry_id
        self.description = description

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.route_entry_id, 'route_entry_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['RouteEntryName'] = self.route_entry_name
        result['RouteEntryId'] = self.route_entry_id
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.route_entry_name = map.get('RouteEntryName')
        self.route_entry_id = map.get('RouteEntryId')
        self.description = map.get('Description')
        return self


class ModifyRouteEntryResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeRouteEntryListRequest(TeaModel):
    def __init__(self, region_id=None, route_table_id=None, route_entry_id=None, destination_cidr_block=None,
                 route_entry_name=None, ip_version=None, route_entry_type=None, next_hop_id=None, next_hop_type=None,
                 max_result=None, next_token=None):
        self.region_id = region_id
        self.route_table_id = route_table_id
        self.route_entry_id = route_entry_id
        self.destination_cidr_block = destination_cidr_block
        self.route_entry_name = route_entry_name
        self.ip_version = ip_version
        self.route_entry_type = route_entry_type
        self.next_hop_id = next_hop_id
        self.next_hop_type = next_hop_type
        self.max_result = max_result
        self.next_token = next_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.route_table_id, 'route_table_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['RouteTableId'] = self.route_table_id
        result['RouteEntryId'] = self.route_entry_id
        result['DestinationCidrBlock'] = self.destination_cidr_block
        result['RouteEntryName'] = self.route_entry_name
        result['IpVersion'] = self.ip_version
        result['RouteEntryType'] = self.route_entry_type
        result['NextHopId'] = self.next_hop_id
        result['NextHopType'] = self.next_hop_type
        result['MaxResult'] = self.max_result
        result['NextToken'] = self.next_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.route_table_id = map.get('RouteTableId')
        self.route_entry_id = map.get('RouteEntryId')
        self.destination_cidr_block = map.get('DestinationCidrBlock')
        self.route_entry_name = map.get('RouteEntryName')
        self.ip_version = map.get('IpVersion')
        self.route_entry_type = map.get('RouteEntryType')
        self.next_hop_id = map.get('NextHopId')
        self.next_hop_type = map.get('NextHopType')
        self.max_result = map.get('MaxResult')
        self.next_token = map.get('NextToken')
        return self


class DescribeRouteEntryListResponse(TeaModel):
    def __init__(self, request_id=None, next_token=None, route_entrys=None):
        self.request_id = request_id
        self.next_token = next_token
        self.route_entrys = route_entrys  # type: DescribeRouteEntryListResponseRouteEntrys

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.route_entrys, 'route_entrys')
        if self.route_entrys:
            self.route_entrys.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['NextToken'] = self.next_token
        if self.route_entrys is not None:
            result['RouteEntrys'] = self.route_entrys.to_map()
        else:
            result['RouteEntrys'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.next_token = map.get('NextToken')
        if map.get('RouteEntrys') is not None:
            temp_model = DescribeRouteEntryListResponseRouteEntrys()
            self.route_entrys = temp_model.from_map(map['RouteEntrys'])
        else:
            self.route_entrys = None
        return self


class DescribeRouteEntryListResponseRouteEntrysRouteEntryNextHopsNextHopNextHopRelatedInfo(TeaModel):
    def __init__(self, instance_type=None, region_id=None, instance_id=None):
        self.instance_type = instance_type
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.instance_type, 'instance_type')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['InstanceType'] = self.instance_type
        result['RegionId'] = self.region_id
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.instance_type = map.get('InstanceType')
        self.region_id = map.get('RegionId')
        self.instance_id = map.get('InstanceId')
        return self


class DescribeRouteEntryListResponseRouteEntrysRouteEntryNextHopsNextHop(TeaModel):
    def __init__(self, next_hop_type=None, next_hop_id=None, enabled=None, weight=None, next_hop_region_id=None,
                 next_hop_related_info=None):
        self.next_hop_type = next_hop_type
        self.next_hop_id = next_hop_id
        self.enabled = enabled
        self.weight = weight
        self.next_hop_region_id = next_hop_region_id
        self.next_hop_related_info = next_hop_related_info  # type: DescribeRouteEntryListResponseRouteEntrysRouteEntryNextHopsNextHopNextHopRelatedInfo

    def validate(self):
        self.validate_required(self.next_hop_type, 'next_hop_type')
        self.validate_required(self.next_hop_id, 'next_hop_id')
        self.validate_required(self.enabled, 'enabled')
        self.validate_required(self.weight, 'weight')
        self.validate_required(self.next_hop_region_id, 'next_hop_region_id')
        self.validate_required(self.next_hop_related_info, 'next_hop_related_info')
        if self.next_hop_related_info:
            self.next_hop_related_info.validate()

    def to_map(self):
        result = {}
        result['NextHopType'] = self.next_hop_type
        result['NextHopId'] = self.next_hop_id
        result['Enabled'] = self.enabled
        result['Weight'] = self.weight
        result['NextHopRegionId'] = self.next_hop_region_id
        if self.next_hop_related_info is not None:
            result['NextHopRelatedInfo'] = self.next_hop_related_info.to_map()
        else:
            result['NextHopRelatedInfo'] = None
        return result

    def from_map(self, map={}):
        self.next_hop_type = map.get('NextHopType')
        self.next_hop_id = map.get('NextHopId')
        self.enabled = map.get('Enabled')
        self.weight = map.get('Weight')
        self.next_hop_region_id = map.get('NextHopRegionId')
        if map.get('NextHopRelatedInfo') is not None:
            temp_model = DescribeRouteEntryListResponseRouteEntrysRouteEntryNextHopsNextHopNextHopRelatedInfo()
            self.next_hop_related_info = temp_model.from_map(map['NextHopRelatedInfo'])
        else:
            self.next_hop_related_info = None
        return self


class DescribeRouteEntryListResponseRouteEntrysRouteEntryNextHops(TeaModel):
    def __init__(self, next_hop=None):
        self.next_hop = next_hop

    def validate(self):
        self.validate_required(self.next_hop, 'next_hop')
        if self.next_hop:
            for k in self.next_hop:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['NextHop'] = []
        if self.next_hop is not None:
            for k in self.next_hop:
                result['NextHop'].append(k.to_map() if k else None)
        else:
            result['NextHop'] = None
        return result

    def from_map(self, map={}):
        self.next_hop = []
        if map.get('NextHop') is not None:
            for k in map.get('NextHop'):
                temp_model = DescribeRouteEntryListResponseRouteEntrysRouteEntryNextHopsNextHop()
                self.next_hop.append(temp_model.from_map(k))
        else:
            self.next_hop = None
        return self


class DescribeRouteEntryListResponseRouteEntrysRouteEntry(TeaModel):
    def __init__(self, route_table_id=None, destination_cidr_block=None, type=None, route_entry_id=None,
                 route_entry_name=None, description=None, status=None, ip_version=None, next_hops=None):
        self.route_table_id = route_table_id
        self.destination_cidr_block = destination_cidr_block
        self.type = type
        self.route_entry_id = route_entry_id
        self.route_entry_name = route_entry_name
        self.description = description
        self.status = status
        self.ip_version = ip_version
        self.next_hops = next_hops  # type: DescribeRouteEntryListResponseRouteEntrysRouteEntryNextHops

    def validate(self):
        self.validate_required(self.route_table_id, 'route_table_id')
        self.validate_required(self.destination_cidr_block, 'destination_cidr_block')
        self.validate_required(self.type, 'type')
        self.validate_required(self.route_entry_id, 'route_entry_id')
        self.validate_required(self.route_entry_name, 'route_entry_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.status, 'status')
        self.validate_required(self.ip_version, 'ip_version')
        self.validate_required(self.next_hops, 'next_hops')
        if self.next_hops:
            self.next_hops.validate()

    def to_map(self):
        result = {}
        result['RouteTableId'] = self.route_table_id
        result['DestinationCidrBlock'] = self.destination_cidr_block
        result['Type'] = self.type
        result['RouteEntryId'] = self.route_entry_id
        result['RouteEntryName'] = self.route_entry_name
        result['Description'] = self.description
        result['Status'] = self.status
        result['IpVersion'] = self.ip_version
        if self.next_hops is not None:
            result['NextHops'] = self.next_hops.to_map()
        else:
            result['NextHops'] = None
        return result

    def from_map(self, map={}):
        self.route_table_id = map.get('RouteTableId')
        self.destination_cidr_block = map.get('DestinationCidrBlock')
        self.type = map.get('Type')
        self.route_entry_id = map.get('RouteEntryId')
        self.route_entry_name = map.get('RouteEntryName')
        self.description = map.get('Description')
        self.status = map.get('Status')
        self.ip_version = map.get('IpVersion')
        if map.get('NextHops') is not None:
            temp_model = DescribeRouteEntryListResponseRouteEntrysRouteEntryNextHops()
            self.next_hops = temp_model.from_map(map['NextHops'])
        else:
            self.next_hops = None
        return self


class DescribeRouteEntryListResponseRouteEntrys(TeaModel):
    def __init__(self, route_entry=None):
        self.route_entry = route_entry

    def validate(self):
        self.validate_required(self.route_entry, 'route_entry')
        if self.route_entry:
            for k in self.route_entry:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RouteEntry'] = []
        if self.route_entry is not None:
            for k in self.route_entry:
                result['RouteEntry'].append(k.to_map() if k else None)
        else:
            result['RouteEntry'] = None
        return result

    def from_map(self, map={}):
        self.route_entry = []
        if map.get('RouteEntry') is not None:
            for k in map.get('RouteEntry'):
                temp_model = DescribeRouteEntryListResponseRouteEntrysRouteEntry()
                self.route_entry.append(temp_model.from_map(k))
        else:
            self.route_entry = None
        return self


class CreateIPv6TranslatorAclListRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, acl_name=None):
        self.region_id = region_id
        self.client_token = client_token
        self.acl_name = acl_name

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.acl_name, 'acl_name')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['AclName'] = self.acl_name
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.acl_name = map.get('AclName')
        return self


class CreateIPv6TranslatorAclListResponse(TeaModel):
    def __init__(self, request_id=None, acl_id=None):
        self.request_id = request_id
        self.acl_id = acl_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.acl_id, 'acl_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['AclId'] = self.acl_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.acl_id = map.get('AclId')
        return self


class DeleteIPv6TranslatorAclListRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, acl_id=None):
        self.client_token = client_token
        self.region_id = region_id
        self.acl_id = acl_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.acl_id, 'acl_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['AclId'] = self.acl_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.acl_id = map.get('AclId')
        return self


class DeleteIPv6TranslatorAclListResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AddIPv6TranslatorAclListEntryRequest(TeaModel):
    def __init__(self, region_id=None, acl_id=None, acl_entry_ip=None, acl_entry_comment=None):
        self.region_id = region_id
        self.acl_id = acl_id
        self.acl_entry_ip = acl_entry_ip
        self.acl_entry_comment = acl_entry_comment

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.acl_id, 'acl_id')
        self.validate_required(self.acl_entry_ip, 'acl_entry_ip')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['AclId'] = self.acl_id
        result['AclEntryIp'] = self.acl_entry_ip
        result['AclEntryComment'] = self.acl_entry_comment
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.acl_id = map.get('AclId')
        self.acl_entry_ip = map.get('AclEntryIp')
        self.acl_entry_comment = map.get('AclEntryComment')
        return self


class AddIPv6TranslatorAclListEntryResponse(TeaModel):
    def __init__(self, request_id=None, acl_entry_id=None):
        self.request_id = request_id
        self.acl_entry_id = acl_entry_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.acl_entry_id, 'acl_entry_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['AclEntryId'] = self.acl_entry_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.acl_entry_id = map.get('AclEntryId')
        return self


class DescribeIPv6TranslatorAclListsRequest(TeaModel):
    def __init__(self, region_id=None, acl_id=None, page_number=None, page_size=None, acl_name=None):
        self.region_id = region_id
        self.acl_id = acl_id
        self.page_number = page_number
        self.page_size = page_size
        self.acl_name = acl_name

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['AclId'] = self.acl_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['AclName'] = self.acl_name
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.acl_id = map.get('AclId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.acl_name = map.get('AclName')
        return self


class DescribeIPv6TranslatorAclListsResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None,
                 ipv_6translator_acls=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.ipv_6translator_acls = ipv_6translator_acls  # type: DescribeIPv6TranslatorAclListsResponseIpv6TranslatorAcls

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.ipv_6translator_acls, 'ipv_6translator_acls')
        if self.ipv_6translator_acls:
            self.ipv_6translator_acls.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.ipv_6translator_acls is not None:
            result['Ipv6TranslatorAcls'] = self.ipv_6translator_acls.to_map()
        else:
            result['Ipv6TranslatorAcls'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('Ipv6TranslatorAcls') is not None:
            temp_model = DescribeIPv6TranslatorAclListsResponseIpv6TranslatorAcls()
            self.ipv_6translator_acls = temp_model.from_map(map['Ipv6TranslatorAcls'])
        else:
            self.ipv_6translator_acls = None
        return self


class DescribeIPv6TranslatorAclListsResponseIpv6TranslatorAclsIPv6TranslatorAcl(TeaModel):
    def __init__(self, acl_id=None, acl_name=None):
        self.acl_id = acl_id
        self.acl_name = acl_name

    def validate(self):
        self.validate_required(self.acl_id, 'acl_id')
        self.validate_required(self.acl_name, 'acl_name')

    def to_map(self):
        result = {}
        result['AclId'] = self.acl_id
        result['AclName'] = self.acl_name
        return result

    def from_map(self, map={}):
        self.acl_id = map.get('AclId')
        self.acl_name = map.get('AclName')
        return self


class DescribeIPv6TranslatorAclListsResponseIpv6TranslatorAcls(TeaModel):
    def __init__(self, ipv_6translator_acl=None):
        self.ipv_6translator_acl = ipv_6translator_acl

    def validate(self):
        self.validate_required(self.ipv_6translator_acl, 'ipv_6translator_acl')
        if self.ipv_6translator_acl:
            for k in self.ipv_6translator_acl:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['IPv6TranslatorAcl'] = []
        if self.ipv_6translator_acl is not None:
            for k in self.ipv_6translator_acl:
                result['IPv6TranslatorAcl'].append(k.to_map() if k else None)
        else:
            result['IPv6TranslatorAcl'] = None
        return result

    def from_map(self, map={}):
        self.ipv_6translator_acl = []
        if map.get('IPv6TranslatorAcl') is not None:
            for k in map.get('IPv6TranslatorAcl'):
                temp_model = DescribeIPv6TranslatorAclListsResponseIpv6TranslatorAclsIPv6TranslatorAcl()
                self.ipv_6translator_acl.append(temp_model.from_map(k))
        else:
            self.ipv_6translator_acl = None
        return self


class ModifyIPv6TranslatorAclAttributeRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, acl_id=None, acl_name=None):
        self.region_id = region_id
        self.client_token = client_token
        self.acl_id = acl_id
        self.acl_name = acl_name

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.acl_id, 'acl_id')
        self.validate_required(self.acl_name, 'acl_name')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['AclId'] = self.acl_id
        result['AclName'] = self.acl_name
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.acl_id = map.get('AclId')
        self.acl_name = map.get('AclName')
        return self


class ModifyIPv6TranslatorAclAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class RemoveIPv6TranslatorAclListEntryRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, acl_id=None, acl_entry_id=None):
        self.client_token = client_token
        self.region_id = region_id
        self.acl_id = acl_id
        self.acl_entry_id = acl_entry_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.acl_id, 'acl_id')
        self.validate_required(self.acl_entry_id, 'acl_entry_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['AclId'] = self.acl_id
        result['AclEntryId'] = self.acl_entry_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.acl_id = map.get('AclId')
        self.acl_entry_id = map.get('AclEntryId')
        return self


class RemoveIPv6TranslatorAclListEntryResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeIPv6TranslatorAclListAttributesRequest(TeaModel):
    def __init__(self, region_id=None, acl_id=None, page_number=None, page_size=None):
        self.region_id = region_id
        self.acl_id = acl_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.acl_id, 'acl_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['AclId'] = self.acl_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.acl_id = map.get('AclId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeIPv6TranslatorAclListAttributesResponse(TeaModel):
    def __init__(self, request_id=None, acl_id=None, acl_name=None, total_count=None, page_number=None,
                 page_size=None, acl_entries=None):
        self.request_id = request_id
        self.acl_id = acl_id
        self.acl_name = acl_name
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.acl_entries = acl_entries  # type: DescribeIPv6TranslatorAclListAttributesResponseAclEntries

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.acl_id, 'acl_id')
        self.validate_required(self.acl_name, 'acl_name')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.acl_entries, 'acl_entries')
        if self.acl_entries:
            self.acl_entries.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['AclId'] = self.acl_id
        result['AclName'] = self.acl_name
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.acl_entries is not None:
            result['AclEntries'] = self.acl_entries.to_map()
        else:
            result['AclEntries'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.acl_id = map.get('AclId')
        self.acl_name = map.get('AclName')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('AclEntries') is not None:
            temp_model = DescribeIPv6TranslatorAclListAttributesResponseAclEntries()
            self.acl_entries = temp_model.from_map(map['AclEntries'])
        else:
            self.acl_entries = None
        return self


class DescribeIPv6TranslatorAclListAttributesResponseAclEntriesAclEntry(TeaModel):
    def __init__(self, acl_entry_id=None, acl_entry_ip=None, acl_entry_comment=None):
        self.acl_entry_id = acl_entry_id
        self.acl_entry_ip = acl_entry_ip
        self.acl_entry_comment = acl_entry_comment

    def validate(self):
        self.validate_required(self.acl_entry_id, 'acl_entry_id')
        self.validate_required(self.acl_entry_ip, 'acl_entry_ip')
        self.validate_required(self.acl_entry_comment, 'acl_entry_comment')

    def to_map(self):
        result = {}
        result['AclEntryId'] = self.acl_entry_id
        result['AclEntryIp'] = self.acl_entry_ip
        result['AclEntryComment'] = self.acl_entry_comment
        return result

    def from_map(self, map={}):
        self.acl_entry_id = map.get('AclEntryId')
        self.acl_entry_ip = map.get('AclEntryIp')
        self.acl_entry_comment = map.get('AclEntryComment')
        return self


class DescribeIPv6TranslatorAclListAttributesResponseAclEntries(TeaModel):
    def __init__(self, acl_entry=None):
        self.acl_entry = acl_entry

    def validate(self):
        self.validate_required(self.acl_entry, 'acl_entry')
        if self.acl_entry:
            for k in self.acl_entry:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['AclEntry'] = []
        if self.acl_entry is not None:
            for k in self.acl_entry:
                result['AclEntry'].append(k.to_map() if k else None)
        else:
            result['AclEntry'] = None
        return result

    def from_map(self, map={}):
        self.acl_entry = []
        if map.get('AclEntry') is not None:
            for k in map.get('AclEntry'):
                temp_model = DescribeIPv6TranslatorAclListAttributesResponseAclEntriesAclEntry()
                self.acl_entry.append(temp_model.from_map(k))
        else:
            self.acl_entry = None
        return self


class ModifyIPv6TranslatorAclListEntryRequest(TeaModel):
    def __init__(self, region_id=None, acl_id=None, acl_entry_id=None, acl_entry_comment=None):
        self.region_id = region_id
        self.acl_id = acl_id
        self.acl_entry_id = acl_entry_id
        self.acl_entry_comment = acl_entry_comment

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.acl_id, 'acl_id')
        self.validate_required(self.acl_entry_id, 'acl_entry_id')
        self.validate_required(self.acl_entry_comment, 'acl_entry_comment')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['AclId'] = self.acl_id
        result['AclEntryId'] = self.acl_entry_id
        result['AclEntryComment'] = self.acl_entry_comment
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.acl_id = map.get('AclId')
        self.acl_entry_id = map.get('AclEntryId')
        self.acl_entry_comment = map.get('AclEntryComment')
        return self


class ModifyIPv6TranslatorAclListEntryResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class UnTagResourcesRequest(TeaModel):
    def __init__(self, resource_type=None, resource_id=None, tag_key=None, region_id=None, all=None):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag_key = tag_key
        self.region_id = region_id
        self.all = all

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['ResourceType'] = self.resource_type
        result['ResourceId'] = self.resource_id
        result['TagKey'] = self.tag_key
        result['RegionId'] = self.region_id
        result['All'] = self.all
        return result

    def from_map(self, map={}):
        self.resource_type = map.get('ResourceType')
        self.resource_id = map.get('ResourceId')
        self.tag_key = map.get('TagKey')
        self.region_id = map.get('RegionId')
        self.all = map.get('All')
        return self


class UnTagResourcesResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(self, resource_type=None, resource_id=None, tag=None, region_id=None):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.tag, 'tag')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['ResourceType'] = self.resource_type
        result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.resource_type = map.get('ResourceType')
        self.resource_id = map.get('ResourceId')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        self.region_id = map.get('RegionId')
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(self, resource_type=None, resource_id=None, tag=None, region_id=None, next_token=None,
                 max_results=None):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag
        self.region_id = region_id
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['ResourceType'] = self.resource_type
        result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        result['RegionId'] = self.region_id
        result['NextToken'] = self.next_token
        result['MaxResults'] = self.max_results
        return result

    def from_map(self, map={}):
        self.resource_type = map.get('ResourceType')
        self.resource_id = map.get('ResourceId')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        self.region_id = map.get('RegionId')
        self.next_token = map.get('NextToken')
        self.max_results = map.get('MaxResults')
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, request_id=None, next_token=None, tag_resources=None):
        self.request_id = request_id
        self.next_token = next_token
        self.tag_resources = tag_resources  # type: ListTagResourcesResponseTagResources

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.tag_resources, 'tag_resources')
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['NextToken'] = self.next_token
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        else:
            result['TagResources'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.next_token = map.get('NextToken')
        if map.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseTagResources()
            self.tag_resources = temp_model.from_map(map['TagResources'])
        else:
            self.tag_resources = None
        return self


class ListTagResourcesResponseTagResourcesTagResource(TeaModel):
    def __init__(self, tag_key=None, tag_value=None, resourc_id=None, resource_type=None, resource_id=None):
        self.tag_key = tag_key
        self.tag_value = tag_value
        self.resourc_id = resourc_id
        self.resource_type = resource_type
        self.resource_id = resource_id

    def validate(self):
        self.validate_required(self.tag_key, 'tag_key')
        self.validate_required(self.tag_value, 'tag_value')
        self.validate_required(self.resourc_id, 'resourc_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['TagKey'] = self.tag_key
        result['TagValue'] = self.tag_value
        result['ResourcId'] = self.resourc_id
        result['ResourceType'] = self.resource_type
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.tag_key = map.get('TagKey')
        self.tag_value = map.get('TagValue')
        self.resourc_id = map.get('ResourcId')
        self.resource_type = map.get('ResourceType')
        self.resource_id = map.get('ResourceId')
        return self


class ListTagResourcesResponseTagResources(TeaModel):
    def __init__(self, tag_resource=None):
        self.tag_resource = tag_resource

    def validate(self):
        self.validate_required(self.tag_resource, 'tag_resource')
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        else:
            result['TagResource'] = None
        return result

    def from_map(self, map={}):
        self.tag_resource = []
        if map.get('TagResource') is not None:
            for k in map.get('TagResource'):
                temp_model = ListTagResourcesResponseTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        else:
            self.tag_resource = None
        return self


class ModifyIpv6InternetBandwidthRequest(TeaModel):
    def __init__(self, region_id=None, ipv_6address_id=None, ipv_6internet_bandwidth_id=None, bandwidth=None,
                 client_token=None):
        self.region_id = region_id
        self.ipv_6address_id = ipv_6address_id
        self.ipv_6internet_bandwidth_id = ipv_6internet_bandwidth_id
        self.bandwidth = bandwidth
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bandwidth, 'bandwidth')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Ipv6AddressId'] = self.ipv_6address_id
        result['Ipv6InternetBandwidthId'] = self.ipv_6internet_bandwidth_id
        result['Bandwidth'] = self.bandwidth
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ipv_6address_id = map.get('Ipv6AddressId')
        self.ipv_6internet_bandwidth_id = map.get('Ipv6InternetBandwidthId')
        self.bandwidth = map.get('Bandwidth')
        self.client_token = map.get('ClientToken')
        return self


class ModifyIpv6InternetBandwidthResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyIpv6GatewaySpecRequest(TeaModel):
    def __init__(self, region_id=None, ipv_6gateway_id=None, spec=None, client_token=None):
        self.region_id = region_id
        self.ipv_6gateway_id = ipv_6gateway_id
        self.spec = spec
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ipv_6gateway_id, 'ipv_6gateway_id')
        self.validate_required(self.spec, 'spec')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Ipv6GatewayId'] = self.ipv_6gateway_id
        result['Spec'] = self.spec
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ipv_6gateway_id = map.get('Ipv6GatewayId')
        self.spec = map.get('Spec')
        self.client_token = map.get('ClientToken')
        return self


class ModifyIpv6GatewaySpecResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyIpv6GatewayAttributeRequest(TeaModel):
    def __init__(self, region_id=None, ipv_6gateway_id=None, name=None, description=None):
        self.region_id = region_id
        self.ipv_6gateway_id = ipv_6gateway_id
        self.name = name
        self.description = description

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ipv_6gateway_id, 'ipv_6gateway_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Ipv6GatewayId'] = self.ipv_6gateway_id
        result['Name'] = self.name
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ipv_6gateway_id = map.get('Ipv6GatewayId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        return self


class ModifyIpv6GatewayAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyIpv6AddressAttributeRequest(TeaModel):
    def __init__(self, region_id=None, ipv_6address_id=None, name=None, description=None):
        self.region_id = region_id
        self.ipv_6address_id = ipv_6address_id
        self.name = name
        self.description = description

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ipv_6address_id, 'ipv_6address_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Ipv6AddressId'] = self.ipv_6address_id
        result['Name'] = self.name
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ipv_6address_id = map.get('Ipv6AddressId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        return self


class ModifyIpv6AddressAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeIpv6GatewaysRequest(TeaModel):
    def __init__(self, region_id=None, ipv_6gateway_id=None, vpc_id=None, name=None, page_number=None,
                 page_size=None):
        self.region_id = region_id
        self.ipv_6gateway_id = ipv_6gateway_id
        self.vpc_id = vpc_id
        self.name = name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Ipv6GatewayId'] = self.ipv_6gateway_id
        result['VpcId'] = self.vpc_id
        result['Name'] = self.name
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ipv_6gateway_id = map.get('Ipv6GatewayId')
        self.vpc_id = map.get('VpcId')
        self.name = map.get('Name')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeIpv6GatewaysResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, ipv_6gateways=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.ipv_6gateways = ipv_6gateways  # type: DescribeIpv6GatewaysResponseIpv6Gateways

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.ipv_6gateways, 'ipv_6gateways')
        if self.ipv_6gateways:
            self.ipv_6gateways.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.ipv_6gateways is not None:
            result['Ipv6Gateways'] = self.ipv_6gateways.to_map()
        else:
            result['Ipv6Gateways'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('Ipv6Gateways') is not None:
            temp_model = DescribeIpv6GatewaysResponseIpv6Gateways()
            self.ipv_6gateways = temp_model.from_map(map['Ipv6Gateways'])
        else:
            self.ipv_6gateways = None
        return self


class DescribeIpv6GatewaysResponseIpv6GatewaysIpv6Gateway(TeaModel):
    def __init__(self, region_id=None, ipv_6gateway_id=None, vpc_id=None, status=None, name=None, description=None,
                 spec=None, instance_charge_type=None, business_status=None, expired_time=None, creation_time=None):
        self.region_id = region_id
        self.ipv_6gateway_id = ipv_6gateway_id
        self.vpc_id = vpc_id
        self.status = status
        self.name = name
        self.description = description
        self.spec = spec
        self.instance_charge_type = instance_charge_type
        self.business_status = business_status
        self.expired_time = expired_time
        self.creation_time = creation_time

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ipv_6gateway_id, 'ipv_6gateway_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.spec, 'spec')
        self.validate_required(self.instance_charge_type, 'instance_charge_type')
        self.validate_required(self.business_status, 'business_status')
        self.validate_required(self.expired_time, 'expired_time')
        self.validate_required(self.creation_time, 'creation_time')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Ipv6GatewayId'] = self.ipv_6gateway_id
        result['VpcId'] = self.vpc_id
        result['Status'] = self.status
        result['Name'] = self.name
        result['Description'] = self.description
        result['Spec'] = self.spec
        result['InstanceChargeType'] = self.instance_charge_type
        result['BusinessStatus'] = self.business_status
        result['ExpiredTime'] = self.expired_time
        result['CreationTime'] = self.creation_time
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ipv_6gateway_id = map.get('Ipv6GatewayId')
        self.vpc_id = map.get('VpcId')
        self.status = map.get('Status')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.spec = map.get('Spec')
        self.instance_charge_type = map.get('InstanceChargeType')
        self.business_status = map.get('BusinessStatus')
        self.expired_time = map.get('ExpiredTime')
        self.creation_time = map.get('CreationTime')
        return self


class DescribeIpv6GatewaysResponseIpv6Gateways(TeaModel):
    def __init__(self, ipv_6gateway=None):
        self.ipv_6gateway = ipv_6gateway

    def validate(self):
        self.validate_required(self.ipv_6gateway, 'ipv_6gateway')
        if self.ipv_6gateway:
            for k in self.ipv_6gateway:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Ipv6Gateway'] = []
        if self.ipv_6gateway is not None:
            for k in self.ipv_6gateway:
                result['Ipv6Gateway'].append(k.to_map() if k else None)
        else:
            result['Ipv6Gateway'] = None
        return result

    def from_map(self, map={}):
        self.ipv_6gateway = []
        if map.get('Ipv6Gateway') is not None:
            for k in map.get('Ipv6Gateway'):
                temp_model = DescribeIpv6GatewaysResponseIpv6GatewaysIpv6Gateway()
                self.ipv_6gateway.append(temp_model.from_map(k))
        else:
            self.ipv_6gateway = None
        return self


class DescribeIpv6GatewayAttributeRequest(TeaModel):
    def __init__(self, region_id=None, ipv_6gateway_id=None):
        self.region_id = region_id
        self.ipv_6gateway_id = ipv_6gateway_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ipv_6gateway_id, 'ipv_6gateway_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Ipv6GatewayId'] = self.ipv_6gateway_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ipv_6gateway_id = map.get('Ipv6GatewayId')
        return self


class DescribeIpv6GatewayAttributeResponse(TeaModel):
    def __init__(self, request_id=None, region_id=None, ipv_6gateway_id=None, vpc_id=None, status=None,
                 business_status=None, name=None, description=None, spec=None, instance_charge_type=None, expired_time=None,
                 creation_time=None):
        self.request_id = request_id
        self.region_id = region_id
        self.ipv_6gateway_id = ipv_6gateway_id
        self.vpc_id = vpc_id
        self.status = status
        self.business_status = business_status
        self.name = name
        self.description = description
        self.spec = spec
        self.instance_charge_type = instance_charge_type
        self.expired_time = expired_time
        self.creation_time = creation_time

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ipv_6gateway_id, 'ipv_6gateway_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.business_status, 'business_status')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.spec, 'spec')
        self.validate_required(self.instance_charge_type, 'instance_charge_type')
        self.validate_required(self.expired_time, 'expired_time')
        self.validate_required(self.creation_time, 'creation_time')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['RegionId'] = self.region_id
        result['Ipv6GatewayId'] = self.ipv_6gateway_id
        result['VpcId'] = self.vpc_id
        result['Status'] = self.status
        result['BusinessStatus'] = self.business_status
        result['Name'] = self.name
        result['Description'] = self.description
        result['Spec'] = self.spec
        result['InstanceChargeType'] = self.instance_charge_type
        result['ExpiredTime'] = self.expired_time
        result['CreationTime'] = self.creation_time
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.region_id = map.get('RegionId')
        self.ipv_6gateway_id = map.get('Ipv6GatewayId')
        self.vpc_id = map.get('VpcId')
        self.status = map.get('Status')
        self.business_status = map.get('BusinessStatus')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.spec = map.get('Spec')
        self.instance_charge_type = map.get('InstanceChargeType')
        self.expired_time = map.get('ExpiredTime')
        self.creation_time = map.get('CreationTime')
        return self


class DescribeIpv6EgressOnlyRulesRequest(TeaModel):
    def __init__(self, region_id=None, ipv_6gateway_id=None, ipv_6egress_only_rule_id=None, name=None,
                 instance_type=None, instance_id=None, page_number=None, page_size=None):
        self.region_id = region_id
        self.ipv_6gateway_id = ipv_6gateway_id
        self.ipv_6egress_only_rule_id = ipv_6egress_only_rule_id
        self.name = name
        self.instance_type = instance_type
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ipv_6gateway_id, 'ipv_6gateway_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Ipv6GatewayId'] = self.ipv_6gateway_id
        result['Ipv6EgressOnlyRuleId'] = self.ipv_6egress_only_rule_id
        result['Name'] = self.name
        result['InstanceType'] = self.instance_type
        result['InstanceId'] = self.instance_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ipv_6gateway_id = map.get('Ipv6GatewayId')
        self.ipv_6egress_only_rule_id = map.get('Ipv6EgressOnlyRuleId')
        self.name = map.get('Name')
        self.instance_type = map.get('InstanceType')
        self.instance_id = map.get('InstanceId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeIpv6EgressOnlyRulesResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None,
                 ipv_6egress_only_rules=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.ipv_6egress_only_rules = ipv_6egress_only_rules  # type: DescribeIpv6EgressOnlyRulesResponseIpv6EgressOnlyRules

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.ipv_6egress_only_rules, 'ipv_6egress_only_rules')
        if self.ipv_6egress_only_rules:
            self.ipv_6egress_only_rules.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.ipv_6egress_only_rules is not None:
            result['Ipv6EgressOnlyRules'] = self.ipv_6egress_only_rules.to_map()
        else:
            result['Ipv6EgressOnlyRules'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('Ipv6EgressOnlyRules') is not None:
            temp_model = DescribeIpv6EgressOnlyRulesResponseIpv6EgressOnlyRules()
            self.ipv_6egress_only_rules = temp_model.from_map(map['Ipv6EgressOnlyRules'])
        else:
            self.ipv_6egress_only_rules = None
        return self


class DescribeIpv6EgressOnlyRulesResponseIpv6EgressOnlyRulesIpv6EgressOnlyRule(TeaModel):
    def __init__(self, ipv_6egress_only_rule_id=None, instance_type=None, instance_id=None, status=None, name=None,
                 description=None):
        self.ipv_6egress_only_rule_id = ipv_6egress_only_rule_id
        self.instance_type = instance_type
        self.instance_id = instance_id
        self.status = status
        self.name = name
        self.description = description

    def validate(self):
        self.validate_required(self.ipv_6egress_only_rule_id, 'ipv_6egress_only_rule_id')
        self.validate_required(self.instance_type, 'instance_type')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')

    def to_map(self):
        result = {}
        result['Ipv6EgressOnlyRuleId'] = self.ipv_6egress_only_rule_id
        result['InstanceType'] = self.instance_type
        result['InstanceId'] = self.instance_id
        result['Status'] = self.status
        result['Name'] = self.name
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.ipv_6egress_only_rule_id = map.get('Ipv6EgressOnlyRuleId')
        self.instance_type = map.get('InstanceType')
        self.instance_id = map.get('InstanceId')
        self.status = map.get('Status')
        self.name = map.get('Name')
        self.description = map.get('Description')
        return self


class DescribeIpv6EgressOnlyRulesResponseIpv6EgressOnlyRules(TeaModel):
    def __init__(self, ipv_6egress_only_rule=None):
        self.ipv_6egress_only_rule = ipv_6egress_only_rule

    def validate(self):
        self.validate_required(self.ipv_6egress_only_rule, 'ipv_6egress_only_rule')
        if self.ipv_6egress_only_rule:
            for k in self.ipv_6egress_only_rule:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Ipv6EgressOnlyRule'] = []
        if self.ipv_6egress_only_rule is not None:
            for k in self.ipv_6egress_only_rule:
                result['Ipv6EgressOnlyRule'].append(k.to_map() if k else None)
        else:
            result['Ipv6EgressOnlyRule'] = None
        return result

    def from_map(self, map={}):
        self.ipv_6egress_only_rule = []
        if map.get('Ipv6EgressOnlyRule') is not None:
            for k in map.get('Ipv6EgressOnlyRule'):
                temp_model = DescribeIpv6EgressOnlyRulesResponseIpv6EgressOnlyRulesIpv6EgressOnlyRule()
                self.ipv_6egress_only_rule.append(temp_model.from_map(k))
        else:
            self.ipv_6egress_only_rule = None
        return self


class DescribeIpv6AddressesRequest(TeaModel):
    def __init__(self, region_id=None, ipv_6address_id=None, ipv_6address=None, name=None,
                 associated_instance_id=None, associated_instance_type=None, network_type=None, vpc_id=None, v_switch_id=None,
                 ipv_6internet_bandwidth_id=None, page_number=None, page_size=None):
        self.region_id = region_id
        self.ipv_6address_id = ipv_6address_id
        self.ipv_6address = ipv_6address
        self.name = name
        self.associated_instance_id = associated_instance_id
        self.associated_instance_type = associated_instance_type
        self.network_type = network_type
        self.vpc_id = vpc_id
        self.v_switch_id = v_switch_id
        self.ipv_6internet_bandwidth_id = ipv_6internet_bandwidth_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Ipv6AddressId'] = self.ipv_6address_id
        result['Ipv6Address'] = self.ipv_6address
        result['Name'] = self.name
        result['AssociatedInstanceId'] = self.associated_instance_id
        result['AssociatedInstanceType'] = self.associated_instance_type
        result['NetworkType'] = self.network_type
        result['VpcId'] = self.vpc_id
        result['VSwitchId'] = self.v_switch_id
        result['Ipv6InternetBandwidthId'] = self.ipv_6internet_bandwidth_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ipv_6address_id = map.get('Ipv6AddressId')
        self.ipv_6address = map.get('Ipv6Address')
        self.name = map.get('Name')
        self.associated_instance_id = map.get('AssociatedInstanceId')
        self.associated_instance_type = map.get('AssociatedInstanceType')
        self.network_type = map.get('NetworkType')
        self.vpc_id = map.get('VpcId')
        self.v_switch_id = map.get('VSwitchId')
        self.ipv_6internet_bandwidth_id = map.get('Ipv6InternetBandwidthId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeIpv6AddressesResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, ipv_6addresses=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.ipv_6addresses = ipv_6addresses  # type: DescribeIpv6AddressesResponseIpv6Addresses

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.ipv_6addresses, 'ipv_6addresses')
        if self.ipv_6addresses:
            self.ipv_6addresses.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.ipv_6addresses is not None:
            result['Ipv6Addresses'] = self.ipv_6addresses.to_map()
        else:
            result['Ipv6Addresses'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('Ipv6Addresses') is not None:
            temp_model = DescribeIpv6AddressesResponseIpv6Addresses()
            self.ipv_6addresses = temp_model.from_map(map['Ipv6Addresses'])
        else:
            self.ipv_6addresses = None
        return self


class DescribeIpv6AddressesResponseIpv6AddressesIpv6AddressIpv6InternetBandwidth(TeaModel):
    def __init__(self, bandwidth=None, instance_charge_type=None, internet_charge_type=None, business_status=None,
                 ipv_6internet_bandwidth_id=None):
        self.bandwidth = bandwidth
        self.instance_charge_type = instance_charge_type
        self.internet_charge_type = internet_charge_type
        self.business_status = business_status
        self.ipv_6internet_bandwidth_id = ipv_6internet_bandwidth_id

    def validate(self):
        self.validate_required(self.bandwidth, 'bandwidth')
        self.validate_required(self.instance_charge_type, 'instance_charge_type')
        self.validate_required(self.internet_charge_type, 'internet_charge_type')
        self.validate_required(self.business_status, 'business_status')
        self.validate_required(self.ipv_6internet_bandwidth_id, 'ipv_6internet_bandwidth_id')

    def to_map(self):
        result = {}
        result['Bandwidth'] = self.bandwidth
        result['InstanceChargeType'] = self.instance_charge_type
        result['InternetChargeType'] = self.internet_charge_type
        result['BusinessStatus'] = self.business_status
        result['Ipv6InternetBandwidthId'] = self.ipv_6internet_bandwidth_id
        return result

    def from_map(self, map={}):
        self.bandwidth = map.get('Bandwidth')
        self.instance_charge_type = map.get('InstanceChargeType')
        self.internet_charge_type = map.get('InternetChargeType')
        self.business_status = map.get('BusinessStatus')
        self.ipv_6internet_bandwidth_id = map.get('Ipv6InternetBandwidthId')
        return self


class DescribeIpv6AddressesResponseIpv6AddressesIpv6Address(TeaModel):
    def __init__(self, ipv_6address_id=None, ipv_6address_name=None, v_switch_id=None, vpc_id=None,
                 ipv_6gateway_id=None, ipv_6address=None, associated_instance_id=None, associated_instance_type=None, status=None,
                 network_type=None, real_bandwidth=None, allocation_time=None, ipv_6internet_bandwidth=None):
        self.ipv_6address_id = ipv_6address_id
        self.ipv_6address_name = ipv_6address_name
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.ipv_6gateway_id = ipv_6gateway_id
        self.ipv_6address = ipv_6address
        self.associated_instance_id = associated_instance_id
        self.associated_instance_type = associated_instance_type
        self.status = status
        self.network_type = network_type
        self.real_bandwidth = real_bandwidth
        self.allocation_time = allocation_time
        self.ipv_6internet_bandwidth = ipv_6internet_bandwidth  # type: DescribeIpv6AddressesResponseIpv6AddressesIpv6AddressIpv6InternetBandwidth

    def validate(self):
        self.validate_required(self.ipv_6address_id, 'ipv_6address_id')
        self.validate_required(self.ipv_6address_name, 'ipv_6address_name')
        self.validate_required(self.v_switch_id, 'v_switch_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.ipv_6gateway_id, 'ipv_6gateway_id')
        self.validate_required(self.ipv_6address, 'ipv_6address')
        self.validate_required(self.associated_instance_id, 'associated_instance_id')
        self.validate_required(self.associated_instance_type, 'associated_instance_type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.network_type, 'network_type')
        self.validate_required(self.real_bandwidth, 'real_bandwidth')
        self.validate_required(self.allocation_time, 'allocation_time')
        self.validate_required(self.ipv_6internet_bandwidth, 'ipv_6internet_bandwidth')
        if self.ipv_6internet_bandwidth:
            self.ipv_6internet_bandwidth.validate()

    def to_map(self):
        result = {}
        result['Ipv6AddressId'] = self.ipv_6address_id
        result['Ipv6AddressName'] = self.ipv_6address_name
        result['VSwitchId'] = self.v_switch_id
        result['VpcId'] = self.vpc_id
        result['Ipv6GatewayId'] = self.ipv_6gateway_id
        result['Ipv6Address'] = self.ipv_6address
        result['AssociatedInstanceId'] = self.associated_instance_id
        result['AssociatedInstanceType'] = self.associated_instance_type
        result['Status'] = self.status
        result['NetworkType'] = self.network_type
        result['RealBandwidth'] = self.real_bandwidth
        result['AllocationTime'] = self.allocation_time
        if self.ipv_6internet_bandwidth is not None:
            result['Ipv6InternetBandwidth'] = self.ipv_6internet_bandwidth.to_map()
        else:
            result['Ipv6InternetBandwidth'] = None
        return result

    def from_map(self, map={}):
        self.ipv_6address_id = map.get('Ipv6AddressId')
        self.ipv_6address_name = map.get('Ipv6AddressName')
        self.v_switch_id = map.get('VSwitchId')
        self.vpc_id = map.get('VpcId')
        self.ipv_6gateway_id = map.get('Ipv6GatewayId')
        self.ipv_6address = map.get('Ipv6Address')
        self.associated_instance_id = map.get('AssociatedInstanceId')
        self.associated_instance_type = map.get('AssociatedInstanceType')
        self.status = map.get('Status')
        self.network_type = map.get('NetworkType')
        self.real_bandwidth = map.get('RealBandwidth')
        self.allocation_time = map.get('AllocationTime')
        if map.get('Ipv6InternetBandwidth') is not None:
            temp_model = DescribeIpv6AddressesResponseIpv6AddressesIpv6AddressIpv6InternetBandwidth()
            self.ipv_6internet_bandwidth = temp_model.from_map(map['Ipv6InternetBandwidth'])
        else:
            self.ipv_6internet_bandwidth = None
        return self


class DescribeIpv6AddressesResponseIpv6Addresses(TeaModel):
    def __init__(self, ipv_6address=None):
        self.ipv_6address = ipv_6address

    def validate(self):
        self.validate_required(self.ipv_6address, 'ipv_6address')
        if self.ipv_6address:
            for k in self.ipv_6address:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Ipv6Address'] = []
        if self.ipv_6address is not None:
            for k in self.ipv_6address:
                result['Ipv6Address'].append(k.to_map() if k else None)
        else:
            result['Ipv6Address'] = None
        return result

    def from_map(self, map={}):
        self.ipv_6address = []
        if map.get('Ipv6Address') is not None:
            for k in map.get('Ipv6Address'):
                temp_model = DescribeIpv6AddressesResponseIpv6AddressesIpv6Address()
                self.ipv_6address.append(temp_model.from_map(k))
        else:
            self.ipv_6address = None
        return self


class DeleteIpv6InternetBandwidthRequest(TeaModel):
    def __init__(self, region_id=None, ipv_6address_id=None, ipv_6internet_bandwidth_id=None):
        self.region_id = region_id
        self.ipv_6address_id = ipv_6address_id
        self.ipv_6internet_bandwidth_id = ipv_6internet_bandwidth_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Ipv6AddressId'] = self.ipv_6address_id
        result['Ipv6InternetBandwidthId'] = self.ipv_6internet_bandwidth_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ipv_6address_id = map.get('Ipv6AddressId')
        self.ipv_6internet_bandwidth_id = map.get('Ipv6InternetBandwidthId')
        return self


class DeleteIpv6InternetBandwidthResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteIpv6GatewayRequest(TeaModel):
    def __init__(self, region_id=None, ipv_6gateway_id=None):
        self.region_id = region_id
        self.ipv_6gateway_id = ipv_6gateway_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ipv_6gateway_id, 'ipv_6gateway_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Ipv6GatewayId'] = self.ipv_6gateway_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ipv_6gateway_id = map.get('Ipv6GatewayId')
        return self


class DeleteIpv6GatewayResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteIpv6EgressOnlyRuleRequest(TeaModel):
    def __init__(self, region_id=None, ipv_6egress_only_rule_id=None, client_token=None):
        self.region_id = region_id
        self.ipv_6egress_only_rule_id = ipv_6egress_only_rule_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ipv_6egress_only_rule_id, 'ipv_6egress_only_rule_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Ipv6EgressOnlyRuleId'] = self.ipv_6egress_only_rule_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ipv_6egress_only_rule_id = map.get('Ipv6EgressOnlyRuleId')
        self.client_token = map.get('ClientToken')
        return self


class DeleteIpv6EgressOnlyRuleResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateIpv6GatewayRequest(TeaModel):
    def __init__(self, region_id=None, vpc_id=None, spec=None, name=None, description=None, client_token=None):
        self.region_id = region_id
        self.vpc_id = vpc_id
        self.spec = spec
        self.name = name
        self.description = description
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpc_id, 'vpc_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VpcId'] = self.vpc_id
        result['Spec'] = self.spec
        result['Name'] = self.name
        result['Description'] = self.description
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vpc_id = map.get('VpcId')
        self.spec = map.get('Spec')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.client_token = map.get('ClientToken')
        return self


class CreateIpv6GatewayResponse(TeaModel):
    def __init__(self, request_id=None, ipv_6gateway_id=None):
        self.request_id = request_id
        self.ipv_6gateway_id = ipv_6gateway_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.ipv_6gateway_id, 'ipv_6gateway_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Ipv6GatewayId'] = self.ipv_6gateway_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.ipv_6gateway_id = map.get('Ipv6GatewayId')
        return self


class CreateIpv6EgressOnlyRuleRequest(TeaModel):
    def __init__(self, region_id=None, ipv_6gateway_id=None, instance_id=None, instance_type=None, name=None,
                 description=None, client_token=None):
        self.region_id = region_id
        self.ipv_6gateway_id = ipv_6gateway_id
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.name = name
        self.description = description
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ipv_6gateway_id, 'ipv_6gateway_id')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Ipv6GatewayId'] = self.ipv_6gateway_id
        result['InstanceId'] = self.instance_id
        result['InstanceType'] = self.instance_type
        result['Name'] = self.name
        result['Description'] = self.description
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ipv_6gateway_id = map.get('Ipv6GatewayId')
        self.instance_id = map.get('InstanceId')
        self.instance_type = map.get('InstanceType')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.client_token = map.get('ClientToken')
        return self


class CreateIpv6EgressOnlyRuleResponse(TeaModel):
    def __init__(self, request_id=None, ipv_6egress_rule_id=None):
        self.request_id = request_id
        self.ipv_6egress_rule_id = ipv_6egress_rule_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.ipv_6egress_rule_id, 'ipv_6egress_rule_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Ipv6EgressRuleId'] = self.ipv_6egress_rule_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.ipv_6egress_rule_id = map.get('Ipv6EgressRuleId')
        return self


class AllocateIpv6InternetBandwidthRequest(TeaModel):
    def __init__(self, region_id=None, ipv_6gateway_id=None, ipv_6address_id=None, internet_charge_type=None,
                 bandwidth=None, client_token=None):
        self.region_id = region_id
        self.ipv_6gateway_id = ipv_6gateway_id
        self.ipv_6address_id = ipv_6address_id
        self.internet_charge_type = internet_charge_type
        self.bandwidth = bandwidth
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ipv_6gateway_id, 'ipv_6gateway_id')
        self.validate_required(self.ipv_6address_id, 'ipv_6address_id')
        self.validate_required(self.bandwidth, 'bandwidth')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Ipv6GatewayId'] = self.ipv_6gateway_id
        result['Ipv6AddressId'] = self.ipv_6address_id
        result['InternetChargeType'] = self.internet_charge_type
        result['Bandwidth'] = self.bandwidth
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ipv_6gateway_id = map.get('Ipv6GatewayId')
        self.ipv_6address_id = map.get('Ipv6AddressId')
        self.internet_charge_type = map.get('InternetChargeType')
        self.bandwidth = map.get('Bandwidth')
        self.client_token = map.get('ClientToken')
        return self


class AllocateIpv6InternetBandwidthResponse(TeaModel):
    def __init__(self, request_id=None, ipv_6address_id=None, internet_bandwidth_id=None):
        self.request_id = request_id
        self.ipv_6address_id = ipv_6address_id
        self.internet_bandwidth_id = internet_bandwidth_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.ipv_6address_id, 'ipv_6address_id')
        self.validate_required(self.internet_bandwidth_id, 'internet_bandwidth_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Ipv6AddressId'] = self.ipv_6address_id
        result['InternetBandwidthId'] = self.internet_bandwidth_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.ipv_6address_id = map.get('Ipv6AddressId')
        self.internet_bandwidth_id = map.get('InternetBandwidthId')
        return self


class DeleteExpressConnectRequest(TeaModel):
    def __init__(self, region_id=None, router_interface_id=None, force=None, client_token=None):
        self.region_id = region_id
        self.router_interface_id = router_interface_id
        self.force = force
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.router_interface_id, 'router_interface_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['RouterInterfaceId'] = self.router_interface_id
        result['Force'] = self.force
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.router_interface_id = map.get('RouterInterfaceId')
        self.force = map.get('Force')
        self.client_token = map.get('ClientToken')
        return self


class DeleteExpressConnectResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateIPv6TranslatorRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, name=None, spec=None, pay_type=None, pricing_cycle=None,
                 duration=None, auto_pay=None, bandwidth=None):
        self.region_id = region_id
        self.client_token = client_token
        self.name = name
        self.spec = spec
        self.pay_type = pay_type
        self.pricing_cycle = pricing_cycle
        self.duration = duration
        self.auto_pay = auto_pay
        self.bandwidth = bandwidth

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['Name'] = self.name
        result['Spec'] = self.spec
        result['PayType'] = self.pay_type
        result['PricingCycle'] = self.pricing_cycle
        result['Duration'] = self.duration
        result['AutoPay'] = self.auto_pay
        result['Bandwidth'] = self.bandwidth
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.name = map.get('Name')
        self.spec = map.get('Spec')
        self.pay_type = map.get('PayType')
        self.pricing_cycle = map.get('PricingCycle')
        self.duration = map.get('Duration')
        self.auto_pay = map.get('AutoPay')
        self.bandwidth = map.get('Bandwidth')
        return self


class CreateIPv6TranslatorResponse(TeaModel):
    def __init__(self, request_id=None, ipv_6translator_id=None, name=None, spec=None, order_id=None):
        self.request_id = request_id
        self.ipv_6translator_id = ipv_6translator_id
        self.name = name
        self.spec = spec
        self.order_id = order_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.ipv_6translator_id, 'ipv_6translator_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.spec, 'spec')
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Ipv6TranslatorId'] = self.ipv_6translator_id
        result['Name'] = self.name
        result['Spec'] = self.spec
        result['OrderId'] = self.order_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.ipv_6translator_id = map.get('Ipv6TranslatorId')
        self.name = map.get('Name')
        self.spec = map.get('Spec')
        self.order_id = map.get('OrderId')
        return self


class DescribeIPv6TranslatorsRequest(TeaModel):
    def __init__(self, region_id=None, ipv_6translator_id=None, name=None, spec=None, status=None,
                 allocate_ipv_6addr=None, allocate_ipv_4addr=None, pay_type=None, page_number=None, page_size=None,
                 business_status=None):
        self.region_id = region_id
        self.ipv_6translator_id = ipv_6translator_id
        self.name = name
        self.spec = spec
        self.status = status
        self.allocate_ipv_6addr = allocate_ipv_6addr
        self.allocate_ipv_4addr = allocate_ipv_4addr
        self.pay_type = pay_type
        self.page_number = page_number
        self.page_size = page_size
        self.business_status = business_status

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Ipv6TranslatorId'] = self.ipv_6translator_id
        result['Name'] = self.name
        result['Spec'] = self.spec
        result['Status'] = self.status
        result['AllocateIpv6Addr'] = self.allocate_ipv_6addr
        result['AllocateIpv4Addr'] = self.allocate_ipv_4addr
        result['PayType'] = self.pay_type
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['BusinessStatus'] = self.business_status
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ipv_6translator_id = map.get('Ipv6TranslatorId')
        self.name = map.get('Name')
        self.spec = map.get('Spec')
        self.status = map.get('Status')
        self.allocate_ipv_6addr = map.get('AllocateIpv6Addr')
        self.allocate_ipv_4addr = map.get('AllocateIpv4Addr')
        self.pay_type = map.get('PayType')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.business_status = map.get('BusinessStatus')
        return self


class DescribeIPv6TranslatorsResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, ipv_6translators=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.ipv_6translators = ipv_6translators  # type: DescribeIPv6TranslatorsResponseIpv6Translators

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.ipv_6translators, 'ipv_6translators')
        if self.ipv_6translators:
            self.ipv_6translators.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.ipv_6translators is not None:
            result['Ipv6Translators'] = self.ipv_6translators.to_map()
        else:
            result['Ipv6Translators'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('Ipv6Translators') is not None:
            temp_model = DescribeIPv6TranslatorsResponseIpv6Translators()
            self.ipv_6translators = temp_model.from_map(map['Ipv6Translators'])
        else:
            self.ipv_6translators = None
        return self


class DescribeIPv6TranslatorsResponseIpv6TranslatorsIpv6TranslatorIpv6TranslatorEntryIds(TeaModel):
    def __init__(self, ipv_6translator_entry_id=None):
        # Ipv6TranslatorEntryId
        self.ipv_6translator_entry_id = ipv_6translator_entry_id

    def validate(self):
        self.validate_required(self.ipv_6translator_entry_id, 'ipv_6translator_entry_id')

    def to_map(self):
        result = {}
        result['Ipv6TranslatorEntryId'] = self.ipv_6translator_entry_id
        return result

    def from_map(self, map={}):
        self.ipv_6translator_entry_id = map.get('Ipv6TranslatorEntryId')
        return self


class DescribeIPv6TranslatorsResponseIpv6TranslatorsIpv6Translator(TeaModel):
    def __init__(self, ipv_6translator_id=None, create_time=None, end_time=None, spec=None, name=None,
                 description=None, status=None, business_status=None, pay_type=None, bandwidth=None, allocate_ipv_6addr=None,
                 allocate_ipv_4addr=None, available_bandwidth=None, region_id=None, ipv_6translator_entry_ids=None):
        self.ipv_6translator_id = ipv_6translator_id
        self.create_time = create_time
        self.end_time = end_time
        self.spec = spec
        self.name = name
        self.description = description
        self.status = status
        self.business_status = business_status
        self.pay_type = pay_type
        self.bandwidth = bandwidth
        self.allocate_ipv_6addr = allocate_ipv_6addr
        self.allocate_ipv_4addr = allocate_ipv_4addr
        self.available_bandwidth = available_bandwidth
        self.region_id = region_id
        self.ipv_6translator_entry_ids = ipv_6translator_entry_ids  # type: DescribeIPv6TranslatorsResponseIpv6TranslatorsIpv6TranslatorIpv6TranslatorEntryIds

    def validate(self):
        self.validate_required(self.ipv_6translator_id, 'ipv_6translator_id')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.spec, 'spec')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.status, 'status')
        self.validate_required(self.business_status, 'business_status')
        self.validate_required(self.pay_type, 'pay_type')
        self.validate_required(self.bandwidth, 'bandwidth')
        self.validate_required(self.allocate_ipv_6addr, 'allocate_ipv_6addr')
        self.validate_required(self.allocate_ipv_4addr, 'allocate_ipv_4addr')
        self.validate_required(self.available_bandwidth, 'available_bandwidth')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ipv_6translator_entry_ids, 'ipv_6translator_entry_ids')
        if self.ipv_6translator_entry_ids:
            self.ipv_6translator_entry_ids.validate()

    def to_map(self):
        result = {}
        result['Ipv6TranslatorId'] = self.ipv_6translator_id
        result['CreateTime'] = self.create_time
        result['EndTime'] = self.end_time
        result['Spec'] = self.spec
        result['Name'] = self.name
        result['Description'] = self.description
        result['Status'] = self.status
        result['BusinessStatus'] = self.business_status
        result['PayType'] = self.pay_type
        result['Bandwidth'] = self.bandwidth
        result['AllocateIpv6Addr'] = self.allocate_ipv_6addr
        result['AllocateIpv4Addr'] = self.allocate_ipv_4addr
        result['AvailableBandwidth'] = self.available_bandwidth
        result['RegionId'] = self.region_id
        if self.ipv_6translator_entry_ids is not None:
            result['Ipv6TranslatorEntryIds'] = self.ipv_6translator_entry_ids.to_map()
        else:
            result['Ipv6TranslatorEntryIds'] = None
        return result

    def from_map(self, map={}):
        self.ipv_6translator_id = map.get('Ipv6TranslatorId')
        self.create_time = map.get('CreateTime')
        self.end_time = map.get('EndTime')
        self.spec = map.get('Spec')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.status = map.get('Status')
        self.business_status = map.get('BusinessStatus')
        self.pay_type = map.get('PayType')
        self.bandwidth = map.get('Bandwidth')
        self.allocate_ipv_6addr = map.get('AllocateIpv6Addr')
        self.allocate_ipv_4addr = map.get('AllocateIpv4Addr')
        self.available_bandwidth = map.get('AvailableBandwidth')
        self.region_id = map.get('RegionId')
        if map.get('Ipv6TranslatorEntryIds') is not None:
            temp_model = DescribeIPv6TranslatorsResponseIpv6TranslatorsIpv6TranslatorIpv6TranslatorEntryIds()
            self.ipv_6translator_entry_ids = temp_model.from_map(map['Ipv6TranslatorEntryIds'])
        else:
            self.ipv_6translator_entry_ids = None
        return self


class DescribeIPv6TranslatorsResponseIpv6Translators(TeaModel):
    def __init__(self, ipv_6translator=None):
        self.ipv_6translator = ipv_6translator

    def validate(self):
        self.validate_required(self.ipv_6translator, 'ipv_6translator')
        if self.ipv_6translator:
            for k in self.ipv_6translator:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Ipv6Translator'] = []
        if self.ipv_6translator is not None:
            for k in self.ipv_6translator:
                result['Ipv6Translator'].append(k.to_map() if k else None)
        else:
            result['Ipv6Translator'] = None
        return result

    def from_map(self, map={}):
        self.ipv_6translator = []
        if map.get('Ipv6Translator') is not None:
            for k in map.get('Ipv6Translator'):
                temp_model = DescribeIPv6TranslatorsResponseIpv6TranslatorsIpv6Translator()
                self.ipv_6translator.append(temp_model.from_map(k))
        else:
            self.ipv_6translator = None
        return self


class ModifyIPv6TranslatorAttributeRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, ipv_6translator_id=None, name=None, description=None):
        self.region_id = region_id
        self.client_token = client_token
        self.ipv_6translator_id = ipv_6translator_id
        self.name = name
        self.description = description

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ipv_6translator_id, 'ipv_6translator_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['Ipv6TranslatorId'] = self.ipv_6translator_id
        result['Name'] = self.name
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.ipv_6translator_id = map.get('Ipv6TranslatorId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        return self


class ModifyIPv6TranslatorAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyIPv6TranslatorBandwidthRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, ipv_6translator_id=None, bandwidth=None, auto_pay=None):
        self.region_id = region_id
        self.client_token = client_token
        self.ipv_6translator_id = ipv_6translator_id
        self.bandwidth = bandwidth
        self.auto_pay = auto_pay

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ipv_6translator_id, 'ipv_6translator_id')
        self.validate_required(self.bandwidth, 'bandwidth')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['Ipv6TranslatorId'] = self.ipv_6translator_id
        result['Bandwidth'] = self.bandwidth
        result['AutoPay'] = self.auto_pay
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.ipv_6translator_id = map.get('Ipv6TranslatorId')
        self.bandwidth = map.get('Bandwidth')
        self.auto_pay = map.get('AutoPay')
        return self


class ModifyIPv6TranslatorBandwidthResponse(TeaModel):
    def __init__(self, request_id=None, order_id=None):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['OrderId'] = self.order_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.order_id = map.get('OrderId')
        return self


class CreateIPv6TranslatorEntryRequest(TeaModel):
    def __init__(self, region_id=None, ipv_6translator_id=None, entry_name=None, entry_description=None,
                 allocate_ipv_6port=None, backend_ipv_4addr=None, backend_ipv_4port=None, trans_protocol=None, entry_bandwidth=None,
                 acl_status=None, acl_type=None, acl_id=None):
        self.region_id = region_id
        self.ipv_6translator_id = ipv_6translator_id
        self.entry_name = entry_name
        self.entry_description = entry_description
        self.allocate_ipv_6port = allocate_ipv_6port
        self.backend_ipv_4addr = backend_ipv_4addr
        self.backend_ipv_4port = backend_ipv_4port
        self.trans_protocol = trans_protocol
        self.entry_bandwidth = entry_bandwidth
        self.acl_status = acl_status
        self.acl_type = acl_type
        self.acl_id = acl_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ipv_6translator_id, 'ipv_6translator_id')
        self.validate_required(self.allocate_ipv_6port, 'allocate_ipv_6port')
        self.validate_required(self.backend_ipv_4addr, 'backend_ipv_4addr')
        self.validate_required(self.backend_ipv_4port, 'backend_ipv_4port')
        self.validate_required(self.trans_protocol, 'trans_protocol')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Ipv6TranslatorId'] = self.ipv_6translator_id
        result['EntryName'] = self.entry_name
        result['EntryDescription'] = self.entry_description
        result['AllocateIpv6Port'] = self.allocate_ipv_6port
        result['BackendIpv4Addr'] = self.backend_ipv_4addr
        result['BackendIpv4Port'] = self.backend_ipv_4port
        result['TransProtocol'] = self.trans_protocol
        result['EntryBandwidth'] = self.entry_bandwidth
        result['AclStatus'] = self.acl_status
        result['AclType'] = self.acl_type
        result['AclId'] = self.acl_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ipv_6translator_id = map.get('Ipv6TranslatorId')
        self.entry_name = map.get('EntryName')
        self.entry_description = map.get('EntryDescription')
        self.allocate_ipv_6port = map.get('AllocateIpv6Port')
        self.backend_ipv_4addr = map.get('BackendIpv4Addr')
        self.backend_ipv_4port = map.get('BackendIpv4Port')
        self.trans_protocol = map.get('TransProtocol')
        self.entry_bandwidth = map.get('EntryBandwidth')
        self.acl_status = map.get('AclStatus')
        self.acl_type = map.get('AclType')
        self.acl_id = map.get('AclId')
        return self


class CreateIPv6TranslatorEntryResponse(TeaModel):
    def __init__(self, request_id=None, ipv_6translator_entry_id=None):
        self.request_id = request_id
        self.ipv_6translator_entry_id = ipv_6translator_entry_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.ipv_6translator_entry_id, 'ipv_6translator_entry_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Ipv6TranslatorEntryId'] = self.ipv_6translator_entry_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.ipv_6translator_entry_id = map.get('Ipv6TranslatorEntryId')
        return self


class DeleteIPv6TranslatorEntryRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, ipv_6translator_entry_id=None, ipv_6translator_id=None):
        self.client_token = client_token
        self.region_id = region_id
        self.ipv_6translator_entry_id = ipv_6translator_entry_id
        self.ipv_6translator_id = ipv_6translator_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['Ipv6TranslatorEntryId'] = self.ipv_6translator_entry_id
        result['Ipv6TranslatorId'] = self.ipv_6translator_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.ipv_6translator_entry_id = map.get('Ipv6TranslatorEntryId')
        self.ipv_6translator_id = map.get('Ipv6TranslatorId')
        return self


class DeleteIPv6TranslatorEntryResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyIPv6TranslatorEntryRequest(TeaModel):
    def __init__(self, region_id=None, ipv_6translator_entry_id=None, entry_name=None, entry_description=None,
                 allocate_ipv_6port=None, backend_ipv_4addr=None, backend_ipv_4port=None, trans_protocol=None, entry_bandwidth=None,
                 acl_status=None, acl_type=None, acl_id=None):
        self.region_id = region_id
        self.ipv_6translator_entry_id = ipv_6translator_entry_id
        self.entry_name = entry_name
        self.entry_description = entry_description
        self.allocate_ipv_6port = allocate_ipv_6port
        self.backend_ipv_4addr = backend_ipv_4addr
        self.backend_ipv_4port = backend_ipv_4port
        self.trans_protocol = trans_protocol
        self.entry_bandwidth = entry_bandwidth
        self.acl_status = acl_status
        self.acl_type = acl_type
        self.acl_id = acl_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ipv_6translator_entry_id, 'ipv_6translator_entry_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Ipv6TranslatorEntryId'] = self.ipv_6translator_entry_id
        result['EntryName'] = self.entry_name
        result['EntryDescription'] = self.entry_description
        result['AllocateIpv6Port'] = self.allocate_ipv_6port
        result['BackendIpv4Addr'] = self.backend_ipv_4addr
        result['BackendIpv4Port'] = self.backend_ipv_4port
        result['TransProtocol'] = self.trans_protocol
        result['EntryBandwidth'] = self.entry_bandwidth
        result['AclStatus'] = self.acl_status
        result['AclType'] = self.acl_type
        result['AclId'] = self.acl_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ipv_6translator_entry_id = map.get('Ipv6TranslatorEntryId')
        self.entry_name = map.get('EntryName')
        self.entry_description = map.get('EntryDescription')
        self.allocate_ipv_6port = map.get('AllocateIpv6Port')
        self.backend_ipv_4addr = map.get('BackendIpv4Addr')
        self.backend_ipv_4port = map.get('BackendIpv4Port')
        self.trans_protocol = map.get('TransProtocol')
        self.entry_bandwidth = map.get('EntryBandwidth')
        self.acl_status = map.get('AclStatus')
        self.acl_type = map.get('AclType')
        self.acl_id = map.get('AclId')
        return self


class ModifyIPv6TranslatorEntryResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeIPv6TranslatorEntriesRequest(TeaModel):
    def __init__(self, region_id=None, ipv_6translator_id=None, ipv_6translator_entry_id=None, entry_name=None,
                 allocate_ipv_6addr=None, allocate_ipv_6port=None, backend_ipv_4addr=None, backend_ipv_4port=None,
                 trans_protocol=None, acl_status=None, acl_type=None, acl_id=None, page_number=None, page_size=None,
                 client_token=None):
        self.region_id = region_id
        self.ipv_6translator_id = ipv_6translator_id
        self.ipv_6translator_entry_id = ipv_6translator_entry_id
        self.entry_name = entry_name
        self.allocate_ipv_6addr = allocate_ipv_6addr
        self.allocate_ipv_6port = allocate_ipv_6port
        self.backend_ipv_4addr = backend_ipv_4addr
        self.backend_ipv_4port = backend_ipv_4port
        self.trans_protocol = trans_protocol
        self.acl_status = acl_status
        self.acl_type = acl_type
        self.acl_id = acl_id
        self.page_number = page_number
        self.page_size = page_size
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Ipv6TranslatorId'] = self.ipv_6translator_id
        result['Ipv6TranslatorEntryId'] = self.ipv_6translator_entry_id
        result['EntryName'] = self.entry_name
        result['AllocateIpv6Addr'] = self.allocate_ipv_6addr
        result['AllocateIpv6Port'] = self.allocate_ipv_6port
        result['BackendIpv4Addr'] = self.backend_ipv_4addr
        result['BackendIpv4Port'] = self.backend_ipv_4port
        result['TransProtocol'] = self.trans_protocol
        result['AclStatus'] = self.acl_status
        result['AclType'] = self.acl_type
        result['AclId'] = self.acl_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ipv_6translator_id = map.get('Ipv6TranslatorId')
        self.ipv_6translator_entry_id = map.get('Ipv6TranslatorEntryId')
        self.entry_name = map.get('EntryName')
        self.allocate_ipv_6addr = map.get('AllocateIpv6Addr')
        self.allocate_ipv_6port = map.get('AllocateIpv6Port')
        self.backend_ipv_4addr = map.get('BackendIpv4Addr')
        self.backend_ipv_4port = map.get('BackendIpv4Port')
        self.trans_protocol = map.get('TransProtocol')
        self.acl_status = map.get('AclStatus')
        self.acl_type = map.get('AclType')
        self.acl_id = map.get('AclId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.client_token = map.get('ClientToken')
        return self


class DescribeIPv6TranslatorEntriesResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None,
                 ipv_6translator_entries=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.ipv_6translator_entries = ipv_6translator_entries  # type: DescribeIPv6TranslatorEntriesResponseIpv6TranslatorEntries

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.ipv_6translator_entries, 'ipv_6translator_entries')
        if self.ipv_6translator_entries:
            self.ipv_6translator_entries.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.ipv_6translator_entries is not None:
            result['Ipv6TranslatorEntries'] = self.ipv_6translator_entries.to_map()
        else:
            result['Ipv6TranslatorEntries'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('Ipv6TranslatorEntries') is not None:
            temp_model = DescribeIPv6TranslatorEntriesResponseIpv6TranslatorEntries()
            self.ipv_6translator_entries = temp_model.from_map(map['Ipv6TranslatorEntries'])
        else:
            self.ipv_6translator_entries = None
        return self


class DescribeIPv6TranslatorEntriesResponseIpv6TranslatorEntriesIpv6TranslatorEntry(TeaModel):
    def __init__(self, ipv_6translator_id=None, ipv_6translator_entry_id=None, allocate_ipv_6addr=None,
                 allocate_ipv_6port=None, backend_ipv_4addr=None, backend_ipv_4port=None, trans_protocol=None, entry_bandwidth=None,
                 entry_description=None, entry_name=None, entry_status=None, acl_status=None, acl_type=None, acl_id=None,
                 region_id=None):
        self.ipv_6translator_id = ipv_6translator_id
        self.ipv_6translator_entry_id = ipv_6translator_entry_id
        self.allocate_ipv_6addr = allocate_ipv_6addr
        self.allocate_ipv_6port = allocate_ipv_6port
        self.backend_ipv_4addr = backend_ipv_4addr
        self.backend_ipv_4port = backend_ipv_4port
        self.trans_protocol = trans_protocol
        self.entry_bandwidth = entry_bandwidth
        self.entry_description = entry_description
        self.entry_name = entry_name
        self.entry_status = entry_status
        self.acl_status = acl_status
        self.acl_type = acl_type
        self.acl_id = acl_id
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.ipv_6translator_id, 'ipv_6translator_id')
        self.validate_required(self.ipv_6translator_entry_id, 'ipv_6translator_entry_id')
        self.validate_required(self.allocate_ipv_6addr, 'allocate_ipv_6addr')
        self.validate_required(self.allocate_ipv_6port, 'allocate_ipv_6port')
        self.validate_required(self.backend_ipv_4addr, 'backend_ipv_4addr')
        self.validate_required(self.backend_ipv_4port, 'backend_ipv_4port')
        self.validate_required(self.trans_protocol, 'trans_protocol')
        self.validate_required(self.entry_bandwidth, 'entry_bandwidth')
        self.validate_required(self.entry_description, 'entry_description')
        self.validate_required(self.entry_name, 'entry_name')
        self.validate_required(self.entry_status, 'entry_status')
        self.validate_required(self.acl_status, 'acl_status')
        self.validate_required(self.acl_type, 'acl_type')
        self.validate_required(self.acl_id, 'acl_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['Ipv6TranslatorId'] = self.ipv_6translator_id
        result['Ipv6TranslatorEntryId'] = self.ipv_6translator_entry_id
        result['AllocateIpv6Addr'] = self.allocate_ipv_6addr
        result['AllocateIpv6Port'] = self.allocate_ipv_6port
        result['BackendIpv4Addr'] = self.backend_ipv_4addr
        result['BackendIpv4Port'] = self.backend_ipv_4port
        result['TransProtocol'] = self.trans_protocol
        result['EntryBandwidth'] = self.entry_bandwidth
        result['EntryDescription'] = self.entry_description
        result['EntryName'] = self.entry_name
        result['EntryStatus'] = self.entry_status
        result['AclStatus'] = self.acl_status
        result['AclType'] = self.acl_type
        result['AclId'] = self.acl_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.ipv_6translator_id = map.get('Ipv6TranslatorId')
        self.ipv_6translator_entry_id = map.get('Ipv6TranslatorEntryId')
        self.allocate_ipv_6addr = map.get('AllocateIpv6Addr')
        self.allocate_ipv_6port = map.get('AllocateIpv6Port')
        self.backend_ipv_4addr = map.get('BackendIpv4Addr')
        self.backend_ipv_4port = map.get('BackendIpv4Port')
        self.trans_protocol = map.get('TransProtocol')
        self.entry_bandwidth = map.get('EntryBandwidth')
        self.entry_description = map.get('EntryDescription')
        self.entry_name = map.get('EntryName')
        self.entry_status = map.get('EntryStatus')
        self.acl_status = map.get('AclStatus')
        self.acl_type = map.get('AclType')
        self.acl_id = map.get('AclId')
        self.region_id = map.get('RegionId')
        return self


class DescribeIPv6TranslatorEntriesResponseIpv6TranslatorEntries(TeaModel):
    def __init__(self, ipv_6translator_entry=None):
        self.ipv_6translator_entry = ipv_6translator_entry

    def validate(self):
        self.validate_required(self.ipv_6translator_entry, 'ipv_6translator_entry')
        if self.ipv_6translator_entry:
            for k in self.ipv_6translator_entry:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Ipv6TranslatorEntry'] = []
        if self.ipv_6translator_entry is not None:
            for k in self.ipv_6translator_entry:
                result['Ipv6TranslatorEntry'].append(k.to_map() if k else None)
        else:
            result['Ipv6TranslatorEntry'] = None
        return result

    def from_map(self, map={}):
        self.ipv_6translator_entry = []
        if map.get('Ipv6TranslatorEntry') is not None:
            for k in map.get('Ipv6TranslatorEntry'):
                temp_model = DescribeIPv6TranslatorEntriesResponseIpv6TranslatorEntriesIpv6TranslatorEntry()
                self.ipv_6translator_entry.append(temp_model.from_map(k))
        else:
            self.ipv_6translator_entry = None
        return self


class DeleteIPv6TranslatorRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, ipv_6translator_id=None):
        self.client_token = client_token
        self.region_id = region_id
        self.ipv_6translator_id = ipv_6translator_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ipv_6translator_id, 'ipv_6translator_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['Ipv6TranslatorId'] = self.ipv_6translator_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.ipv_6translator_id = map.get('Ipv6TranslatorId')
        return self


class DeleteIPv6TranslatorResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AllocateEipAddressProRequest(TeaModel):
    def __init__(self, region_id=None, ip_address=None, instance_id=None, bandwidth=None, period=None, isp=None,
                 netmode=None, auto_pay=None, pricing_cycle=None, instance_charge_type=None, internet_charge_type=None,
                 resource_group_id=None, client_token=None):
        self.region_id = region_id
        self.ip_address = ip_address
        self.instance_id = instance_id
        self.bandwidth = bandwidth
        self.period = period
        self.isp = isp
        self.netmode = netmode
        self.auto_pay = auto_pay
        self.pricing_cycle = pricing_cycle
        self.instance_charge_type = instance_charge_type
        self.internet_charge_type = internet_charge_type
        self.resource_group_id = resource_group_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['IpAddress'] = self.ip_address
        result['InstanceId'] = self.instance_id
        result['Bandwidth'] = self.bandwidth
        result['Period'] = self.period
        result['ISP'] = self.isp
        result['Netmode'] = self.netmode
        result['AutoPay'] = self.auto_pay
        result['PricingCycle'] = self.pricing_cycle
        result['InstanceChargeType'] = self.instance_charge_type
        result['InternetChargeType'] = self.internet_charge_type
        result['ResourceGroupId'] = self.resource_group_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ip_address = map.get('IpAddress')
        self.instance_id = map.get('InstanceId')
        self.bandwidth = map.get('Bandwidth')
        self.period = map.get('Period')
        self.isp = map.get('ISP')
        self.netmode = map.get('Netmode')
        self.auto_pay = map.get('AutoPay')
        self.pricing_cycle = map.get('PricingCycle')
        self.instance_charge_type = map.get('InstanceChargeType')
        self.internet_charge_type = map.get('InternetChargeType')
        self.resource_group_id = map.get('ResourceGroupId')
        self.client_token = map.get('ClientToken')
        return self


class AllocateEipAddressProResponse(TeaModel):
    def __init__(self, request_id=None, allocation_id=None, eip_address=None, order_id=None, resource_group_id=None):
        self.request_id = request_id
        self.allocation_id = allocation_id
        self.eip_address = eip_address
        self.order_id = order_id
        self.resource_group_id = resource_group_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.allocation_id, 'allocation_id')
        self.validate_required(self.eip_address, 'eip_address')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.resource_group_id, 'resource_group_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['AllocationId'] = self.allocation_id
        result['EipAddress'] = self.eip_address
        result['OrderId'] = self.order_id
        result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.allocation_id = map.get('AllocationId')
        self.eip_address = map.get('EipAddress')
        self.order_id = map.get('OrderId')
        self.resource_group_id = map.get('ResourceGroupId')
        return self


class DescribeHighDefinitionMonitorLogAttributeRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, instance_type=None):
        self.region_id = region_id
        self.instance_id = instance_id
        self.instance_type = instance_type

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['InstanceId'] = self.instance_id
        result['InstanceType'] = self.instance_type
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.instance_id = map.get('InstanceId')
        self.instance_type = map.get('InstanceType')
        return self


class DescribeHighDefinitionMonitorLogAttributeResponse(TeaModel):
    def __init__(self, request_id=None, success=None, instance_id=None, instance_type=None, log_project=None,
                 log_store=None):
        self.request_id = request_id
        self.success = success
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.log_project = log_project
        self.log_store = log_store

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.instance_type, 'instance_type')
        self.validate_required(self.log_project, 'log_project')
        self.validate_required(self.log_store, 'log_store')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['InstanceId'] = self.instance_id
        result['InstanceType'] = self.instance_type
        result['LogProject'] = self.log_project
        result['LogStore'] = self.log_store
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.instance_id = map.get('InstanceId')
        self.instance_type = map.get('InstanceType')
        self.log_project = map.get('LogProject')
        self.log_store = map.get('LogStore')
        return self


class ModifyFlowLogAttributeRequest(TeaModel):
    def __init__(self, region_id=None, flow_log_id=None, flow_log_name=None, description=None):
        self.region_id = region_id
        self.flow_log_id = flow_log_id
        self.flow_log_name = flow_log_name
        self.description = description

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.flow_log_id, 'flow_log_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['FlowLogId'] = self.flow_log_id
        result['FlowLogName'] = self.flow_log_name
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.flow_log_id = map.get('FlowLogId')
        self.flow_log_name = map.get('FlowLogName')
        self.description = map.get('Description')
        return self


class ModifyFlowLogAttributeResponse(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id
        self.success = success

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        return self


class DescribeFlowLogsRequest(TeaModel):
    def __init__(self, region_id=None, flow_log_name=None, flow_log_id=None, description=None, resource_type=None,
                 resource_id=None, traffic_type=None, project_name=None, log_store_name=None, status=None, page_number=None,
                 page_size=None, vpc_id=None):
        self.region_id = region_id
        self.flow_log_name = flow_log_name
        self.flow_log_id = flow_log_id
        self.description = description
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.traffic_type = traffic_type
        self.project_name = project_name
        self.log_store_name = log_store_name
        self.status = status
        self.page_number = page_number
        self.page_size = page_size
        self.vpc_id = vpc_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['FlowLogName'] = self.flow_log_name
        result['FlowLogId'] = self.flow_log_id
        result['Description'] = self.description
        result['ResourceType'] = self.resource_type
        result['ResourceId'] = self.resource_id
        result['TrafficType'] = self.traffic_type
        result['ProjectName'] = self.project_name
        result['LogStoreName'] = self.log_store_name
        result['Status'] = self.status
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['VpcId'] = self.vpc_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.flow_log_name = map.get('FlowLogName')
        self.flow_log_id = map.get('FlowLogId')
        self.description = map.get('Description')
        self.resource_type = map.get('ResourceType')
        self.resource_id = map.get('ResourceId')
        self.traffic_type = map.get('TrafficType')
        self.project_name = map.get('ProjectName')
        self.log_store_name = map.get('LogStoreName')
        self.status = map.get('Status')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.vpc_id = map.get('VpcId')
        return self


class DescribeFlowLogsResponse(TeaModel):
    def __init__(self, request_id=None, success=None, total_count=None, page_number=None, page_size=None,
                 flow_logs=None):
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.flow_logs = flow_logs  # type: DescribeFlowLogsResponseFlowLogs

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.flow_logs, 'flow_logs')
        if self.flow_logs:
            self.flow_logs.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.flow_logs is not None:
            result['FlowLogs'] = self.flow_logs.to_map()
        else:
            result['FlowLogs'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('FlowLogs') is not None:
            temp_model = DescribeFlowLogsResponseFlowLogs()
            self.flow_logs = temp_model.from_map(map['FlowLogs'])
        else:
            self.flow_logs = None
        return self


class DescribeFlowLogsResponseFlowLogsFlowLog(TeaModel):
    def __init__(self, flow_log_id=None, flow_log_name=None, description=None, creation_time=None,
                 resource_type=None, resource_id=None, project_name=None, log_store_name=None, status=None, traffic_type=None,
                 region_id=None):
        self.flow_log_id = flow_log_id
        self.flow_log_name = flow_log_name
        self.description = description
        self.creation_time = creation_time
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.project_name = project_name
        self.log_store_name = log_store_name
        self.status = status
        self.traffic_type = traffic_type
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.flow_log_id, 'flow_log_id')
        self.validate_required(self.flow_log_name, 'flow_log_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.log_store_name, 'log_store_name')
        self.validate_required(self.status, 'status')
        self.validate_required(self.traffic_type, 'traffic_type')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['FlowLogId'] = self.flow_log_id
        result['FlowLogName'] = self.flow_log_name
        result['Description'] = self.description
        result['CreationTime'] = self.creation_time
        result['ResourceType'] = self.resource_type
        result['ResourceId'] = self.resource_id
        result['ProjectName'] = self.project_name
        result['LogStoreName'] = self.log_store_name
        result['Status'] = self.status
        result['TrafficType'] = self.traffic_type
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.flow_log_id = map.get('FlowLogId')
        self.flow_log_name = map.get('FlowLogName')
        self.description = map.get('Description')
        self.creation_time = map.get('CreationTime')
        self.resource_type = map.get('ResourceType')
        self.resource_id = map.get('ResourceId')
        self.project_name = map.get('ProjectName')
        self.log_store_name = map.get('LogStoreName')
        self.status = map.get('Status')
        self.traffic_type = map.get('TrafficType')
        self.region_id = map.get('RegionId')
        return self


class DescribeFlowLogsResponseFlowLogs(TeaModel):
    def __init__(self, flow_log=None):
        self.flow_log = flow_log

    def validate(self):
        self.validate_required(self.flow_log, 'flow_log')
        if self.flow_log:
            for k in self.flow_log:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['FlowLog'] = []
        if self.flow_log is not None:
            for k in self.flow_log:
                result['FlowLog'].append(k.to_map() if k else None)
        else:
            result['FlowLog'] = None
        return result

    def from_map(self, map={}):
        self.flow_log = []
        if map.get('FlowLog') is not None:
            for k in map.get('FlowLog'):
                temp_model = DescribeFlowLogsResponseFlowLogsFlowLog()
                self.flow_log.append(temp_model.from_map(k))
        else:
            self.flow_log = None
        return self


class DeleteFlowLogRequest(TeaModel):
    def __init__(self, region_id=None, flow_log_id=None):
        self.region_id = region_id
        self.flow_log_id = flow_log_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.flow_log_id, 'flow_log_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['FlowLogId'] = self.flow_log_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.flow_log_id = map.get('FlowLogId')
        return self


class DeleteFlowLogResponse(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id
        self.success = success

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        return self


class DeactiveFlowLogRequest(TeaModel):
    def __init__(self, region_id=None, flow_log_id=None):
        self.region_id = region_id
        self.flow_log_id = flow_log_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.flow_log_id, 'flow_log_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['FlowLogId'] = self.flow_log_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.flow_log_id = map.get('FlowLogId')
        return self


class DeactiveFlowLogResponse(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id
        self.success = success

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        return self


class CreateFlowLogRequest(TeaModel):
    def __init__(self, region_id=None, flow_log_name=None, description=None, resource_type=None, resource_id=None,
                 traffic_type=None, project_name=None, log_store_name=None):
        self.region_id = region_id
        self.flow_log_name = flow_log_name
        self.description = description
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.traffic_type = traffic_type
        self.project_name = project_name
        self.log_store_name = log_store_name

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.traffic_type, 'traffic_type')
        self.validate_required(self.project_name, 'project_name')
        self.validate_required(self.log_store_name, 'log_store_name')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['FlowLogName'] = self.flow_log_name
        result['Description'] = self.description
        result['ResourceType'] = self.resource_type
        result['ResourceId'] = self.resource_id
        result['TrafficType'] = self.traffic_type
        result['ProjectName'] = self.project_name
        result['LogStoreName'] = self.log_store_name
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.flow_log_name = map.get('FlowLogName')
        self.description = map.get('Description')
        self.resource_type = map.get('ResourceType')
        self.resource_id = map.get('ResourceId')
        self.traffic_type = map.get('TrafficType')
        self.project_name = map.get('ProjectName')
        self.log_store_name = map.get('LogStoreName')
        return self


class CreateFlowLogResponse(TeaModel):
    def __init__(self, request_id=None, success=None, flow_log_id=None):
        self.request_id = request_id
        self.success = success
        self.flow_log_id = flow_log_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.flow_log_id, 'flow_log_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['FlowLogId'] = self.flow_log_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.flow_log_id = map.get('FlowLogId')
        return self


class ActiveFlowLogRequest(TeaModel):
    def __init__(self, region_id=None, flow_log_id=None):
        self.region_id = region_id
        self.flow_log_id = flow_log_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.flow_log_id, 'flow_log_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['FlowLogId'] = self.flow_log_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.flow_log_id = map.get('FlowLogId')
        return self


class ActiveFlowLogResponse(TeaModel):
    def __init__(self, request_id=None, success=None):
        self.request_id = request_id
        self.success = success

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        return self


class UnassociateRouteTableRequest(TeaModel):
    def __init__(self, region_id=None, route_table_id=None, v_switch_id=None, client_token=None):
        self.region_id = region_id
        self.route_table_id = route_table_id
        self.v_switch_id = v_switch_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.route_table_id, 'route_table_id')
        self.validate_required(self.v_switch_id, 'v_switch_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['RouteTableId'] = self.route_table_id
        result['VSwitchId'] = self.v_switch_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.route_table_id = map.get('RouteTableId')
        self.v_switch_id = map.get('VSwitchId')
        self.client_token = map.get('ClientToken')
        return self


class UnassociateRouteTableResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteRouteTableRequest(TeaModel):
    def __init__(self, region_id=None, route_table_id=None):
        self.region_id = region_id
        self.route_table_id = route_table_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.route_table_id, 'route_table_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['RouteTableId'] = self.route_table_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.route_table_id = map.get('RouteTableId')
        return self


class DeleteRouteTableResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateRouteTableRequest(TeaModel):
    def __init__(self, region_id=None, vpc_id=None, route_table_name=None, description=None, client_token=None):
        self.region_id = region_id
        self.vpc_id = vpc_id
        self.route_table_name = route_table_name
        self.description = description
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpc_id, 'vpc_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VpcId'] = self.vpc_id
        result['RouteTableName'] = self.route_table_name
        result['Description'] = self.description
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vpc_id = map.get('VpcId')
        self.route_table_name = map.get('RouteTableName')
        self.description = map.get('Description')
        self.client_token = map.get('ClientToken')
        return self


class CreateRouteTableResponse(TeaModel):
    def __init__(self, request_id=None, route_table_id=None):
        self.request_id = request_id
        self.route_table_id = route_table_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.route_table_id, 'route_table_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['RouteTableId'] = self.route_table_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.route_table_id = map.get('RouteTableId')
        return self


class AssociateRouteTableRequest(TeaModel):
    def __init__(self, region_id=None, route_table_id=None, v_switch_id=None, client_token=None):
        self.region_id = region_id
        self.route_table_id = route_table_id
        self.v_switch_id = v_switch_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.route_table_id, 'route_table_id')
        self.validate_required(self.v_switch_id, 'v_switch_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['RouteTableId'] = self.route_table_id
        result['VSwitchId'] = self.v_switch_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.route_table_id = map.get('RouteTableId')
        self.v_switch_id = map.get('VSwitchId')
        self.client_token = map.get('ClientToken')
        return self


class AssociateRouteTableResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateVpnGatewayRequest(TeaModel):
    def __init__(self, region_id=None, name=None, vpc_id=None, instance_charge_type=None, period=None, auto_pay=None,
                 bandwidth=None, enable_ipsec=None, enable_ssl=None, ssl_connections=None, v_switch_id=None):
        self.region_id = region_id
        self.name = name
        self.vpc_id = vpc_id
        self.instance_charge_type = instance_charge_type
        self.period = period
        self.auto_pay = auto_pay
        self.bandwidth = bandwidth
        self.enable_ipsec = enable_ipsec
        self.enable_ssl = enable_ssl
        self.ssl_connections = ssl_connections
        self.v_switch_id = v_switch_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.bandwidth, 'bandwidth')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Name'] = self.name
        result['VpcId'] = self.vpc_id
        result['InstanceChargeType'] = self.instance_charge_type
        result['Period'] = self.period
        result['AutoPay'] = self.auto_pay
        result['Bandwidth'] = self.bandwidth
        result['EnableIpsec'] = self.enable_ipsec
        result['EnableSsl'] = self.enable_ssl
        result['SslConnections'] = self.ssl_connections
        result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.name = map.get('Name')
        self.vpc_id = map.get('VpcId')
        self.instance_charge_type = map.get('InstanceChargeType')
        self.period = map.get('Period')
        self.auto_pay = map.get('AutoPay')
        self.bandwidth = map.get('Bandwidth')
        self.enable_ipsec = map.get('EnableIpsec')
        self.enable_ssl = map.get('EnableSsl')
        self.ssl_connections = map.get('SslConnections')
        self.v_switch_id = map.get('VSwitchId')
        return self


class CreateVpnGatewayResponse(TeaModel):
    def __init__(self, request_id=None, vpn_gateway_id=None, name=None, order_id=None):
        self.request_id = request_id
        self.vpn_gateway_id = vpn_gateway_id
        self.name = name
        self.order_id = order_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['Name'] = self.name
        result['OrderId'] = self.order_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.name = map.get('Name')
        self.order_id = map.get('OrderId')
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, new_resource_group_id=None, region_id=None):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.new_resource_group_id = new_resource_group_id
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.new_resource_group_id, 'new_resource_group_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['ResourceId'] = self.resource_id
        result['ResourceType'] = self.resource_type
        result['NewResourceGroupId'] = self.new_resource_group_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.resource_id = map.get('ResourceId')
        self.resource_type = map.get('ResourceType')
        self.new_resource_group_id = map.get('NewResourceGroupId')
        self.region_id = map.get('RegionId')
        return self


class MoveResourceGroupResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class RevokeInstanceFromCenRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, instance_type=None, cen_id=None, cen_owner_id=None,
                 client_token=None):
        self.region_id = region_id
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.cen_id = cen_id
        self.cen_owner_id = cen_owner_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.instance_type, 'instance_type')
        self.validate_required(self.cen_id, 'cen_id')
        self.validate_required(self.cen_owner_id, 'cen_owner_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['InstanceId'] = self.instance_id
        result['InstanceType'] = self.instance_type
        result['CenId'] = self.cen_id
        result['CenOwnerId'] = self.cen_owner_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.instance_id = map.get('InstanceId')
        self.instance_type = map.get('InstanceType')
        self.cen_id = map.get('CenId')
        self.cen_owner_id = map.get('CenOwnerId')
        self.client_token = map.get('ClientToken')
        return self


class RevokeInstanceFromCenResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class GrantInstanceToCenRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, instance_type=None, cen_id=None, cen_owner_id=None,
                 client_token=None):
        self.region_id = region_id
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.cen_id = cen_id
        self.cen_owner_id = cen_owner_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.instance_type, 'instance_type')
        self.validate_required(self.cen_id, 'cen_id')
        self.validate_required(self.cen_owner_id, 'cen_owner_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['InstanceId'] = self.instance_id
        result['InstanceType'] = self.instance_type
        result['CenId'] = self.cen_id
        result['CenOwnerId'] = self.cen_owner_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.instance_id = map.get('InstanceId')
        self.instance_type = map.get('InstanceType')
        self.cen_id = map.get('CenId')
        self.cen_owner_id = map.get('CenOwnerId')
        self.client_token = map.get('ClientToken')
        return self


class GrantInstanceToCenResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeGrantRulesToCenRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, instance_type=None, resource_group_id=None,
                 client_token=None):
        self.region_id = region_id
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.resource_group_id = resource_group_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.instance_type, 'instance_type')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['InstanceId'] = self.instance_id
        result['InstanceType'] = self.instance_type
        result['ResourceGroupId'] = self.resource_group_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.instance_id = map.get('InstanceId')
        self.instance_type = map.get('InstanceType')
        self.resource_group_id = map.get('ResourceGroupId')
        self.client_token = map.get('ClientToken')
        return self


class DescribeGrantRulesToCenResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, cen_grant_rules=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.cen_grant_rules = cen_grant_rules  # type: DescribeGrantRulesToCenResponseCenGrantRules

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.cen_grant_rules, 'cen_grant_rules')
        if self.cen_grant_rules:
            self.cen_grant_rules.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.cen_grant_rules is not None:
            result['CenGrantRules'] = self.cen_grant_rules.to_map()
        else:
            result['CenGrantRules'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('CenGrantRules') is not None:
            temp_model = DescribeGrantRulesToCenResponseCenGrantRules()
            self.cen_grant_rules = temp_model.from_map(map['CenGrantRules'])
        else:
            self.cen_grant_rules = None
        return self


class DescribeGrantRulesToCenResponseCenGrantRulesCbnGrantRule(TeaModel):
    def __init__(self, cen_instance_id=None, cen_owner_id=None, creation_time=None):
        self.cen_instance_id = cen_instance_id
        self.cen_owner_id = cen_owner_id
        self.creation_time = creation_time

    def validate(self):
        self.validate_required(self.cen_instance_id, 'cen_instance_id')
        self.validate_required(self.cen_owner_id, 'cen_owner_id')
        self.validate_required(self.creation_time, 'creation_time')

    def to_map(self):
        result = {}
        result['CenInstanceId'] = self.cen_instance_id
        result['CenOwnerId'] = self.cen_owner_id
        result['CreationTime'] = self.creation_time
        return result

    def from_map(self, map={}):
        self.cen_instance_id = map.get('CenInstanceId')
        self.cen_owner_id = map.get('CenOwnerId')
        self.creation_time = map.get('CreationTime')
        return self


class DescribeGrantRulesToCenResponseCenGrantRules(TeaModel):
    def __init__(self, cbn_grant_rule=None):
        self.cbn_grant_rule = cbn_grant_rule

    def validate(self):
        self.validate_required(self.cbn_grant_rule, 'cbn_grant_rule')
        if self.cbn_grant_rule:
            for k in self.cbn_grant_rule:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['CbnGrantRule'] = []
        if self.cbn_grant_rule is not None:
            for k in self.cbn_grant_rule:
                result['CbnGrantRule'].append(k.to_map() if k else None)
        else:
            result['CbnGrantRule'] = None
        return result

    def from_map(self, map={}):
        self.cbn_grant_rule = []
        if map.get('CbnGrantRule') is not None:
            for k in map.get('CbnGrantRule'):
                temp_model = DescribeGrantRulesToCenResponseCenGrantRulesCbnGrantRule()
                self.cbn_grant_rule.append(temp_model.from_map(k))
        else:
            self.cbn_grant_rule = None
        return self


class ModifySslVpnServerRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, ssl_vpn_server_id=None, name=None, client_ip_pool=None,
                 local_subnet=None, proto=None, cipher=None, port=None, compress=None, enable_multi_factor_auth=None,
                 idaa_sinstance_id=None):
        self.client_token = client_token
        self.region_id = region_id
        self.ssl_vpn_server_id = ssl_vpn_server_id
        self.name = name
        self.client_ip_pool = client_ip_pool
        self.local_subnet = local_subnet
        self.proto = proto
        self.cipher = cipher
        self.port = port
        self.compress = compress
        self.enable_multi_factor_auth = enable_multi_factor_auth
        self.idaa_sinstance_id = idaa_sinstance_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ssl_vpn_server_id, 'ssl_vpn_server_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['SslVpnServerId'] = self.ssl_vpn_server_id
        result['Name'] = self.name
        result['ClientIpPool'] = self.client_ip_pool
        result['LocalSubnet'] = self.local_subnet
        result['Proto'] = self.proto
        result['Cipher'] = self.cipher
        result['Port'] = self.port
        result['Compress'] = self.compress
        result['EnableMultiFactorAuth'] = self.enable_multi_factor_auth
        result['IDaaSInstanceId'] = self.idaa_sinstance_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.ssl_vpn_server_id = map.get('SslVpnServerId')
        self.name = map.get('Name')
        self.client_ip_pool = map.get('ClientIpPool')
        self.local_subnet = map.get('LocalSubnet')
        self.proto = map.get('Proto')
        self.cipher = map.get('Cipher')
        self.port = map.get('Port')
        self.compress = map.get('Compress')
        self.enable_multi_factor_auth = map.get('EnableMultiFactorAuth')
        self.idaa_sinstance_id = map.get('IDaaSInstanceId')
        return self


class ModifySslVpnServerResponse(TeaModel):
    def __init__(self, request_id=None, region_id=None, ssl_vpn_server_id=None, vpn_gateway_id=None, name=None,
                 local_subnet=None, client_ip_pool=None, create_time=None, cipher=None, proto=None, port=None, compress=None,
                 connections=None, max_connections=None, internet_ip=None, enable_multi_factor_auth=None,
                 idaa_sinstance_id=None):
        self.request_id = request_id
        self.region_id = region_id
        self.ssl_vpn_server_id = ssl_vpn_server_id
        self.vpn_gateway_id = vpn_gateway_id
        self.name = name
        self.local_subnet = local_subnet
        self.client_ip_pool = client_ip_pool
        self.create_time = create_time
        self.cipher = cipher
        self.proto = proto
        self.port = port
        self.compress = compress
        self.connections = connections
        self.max_connections = max_connections
        self.internet_ip = internet_ip
        self.enable_multi_factor_auth = enable_multi_factor_auth
        self.idaa_sinstance_id = idaa_sinstance_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ssl_vpn_server_id, 'ssl_vpn_server_id')
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.local_subnet, 'local_subnet')
        self.validate_required(self.client_ip_pool, 'client_ip_pool')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.cipher, 'cipher')
        self.validate_required(self.proto, 'proto')
        self.validate_required(self.port, 'port')
        self.validate_required(self.compress, 'compress')
        self.validate_required(self.connections, 'connections')
        self.validate_required(self.max_connections, 'max_connections')
        self.validate_required(self.internet_ip, 'internet_ip')
        self.validate_required(self.enable_multi_factor_auth, 'enable_multi_factor_auth')
        self.validate_required(self.idaa_sinstance_id, 'idaa_sinstance_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['RegionId'] = self.region_id
        result['SslVpnServerId'] = self.ssl_vpn_server_id
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['Name'] = self.name
        result['LocalSubnet'] = self.local_subnet
        result['ClientIpPool'] = self.client_ip_pool
        result['CreateTime'] = self.create_time
        result['Cipher'] = self.cipher
        result['Proto'] = self.proto
        result['Port'] = self.port
        result['Compress'] = self.compress
        result['Connections'] = self.connections
        result['MaxConnections'] = self.max_connections
        result['InternetIp'] = self.internet_ip
        result['EnableMultiFactorAuth'] = self.enable_multi_factor_auth
        result['IDaaSInstanceId'] = self.idaa_sinstance_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.region_id = map.get('RegionId')
        self.ssl_vpn_server_id = map.get('SslVpnServerId')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.name = map.get('Name')
        self.local_subnet = map.get('LocalSubnet')
        self.client_ip_pool = map.get('ClientIpPool')
        self.create_time = map.get('CreateTime')
        self.cipher = map.get('Cipher')
        self.proto = map.get('Proto')
        self.port = map.get('Port')
        self.compress = map.get('Compress')
        self.connections = map.get('Connections')
        self.max_connections = map.get('MaxConnections')
        self.internet_ip = map.get('InternetIp')
        self.enable_multi_factor_auth = map.get('EnableMultiFactorAuth')
        self.idaa_sinstance_id = map.get('IDaaSInstanceId')
        return self


class ModifySslVpnClientCertRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, ssl_vpn_client_cert_id=None, name=None):
        self.client_token = client_token
        self.region_id = region_id
        self.ssl_vpn_client_cert_id = ssl_vpn_client_cert_id
        self.name = name

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ssl_vpn_client_cert_id, 'ssl_vpn_client_cert_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['SslVpnClientCertId'] = self.ssl_vpn_client_cert_id
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.ssl_vpn_client_cert_id = map.get('SslVpnClientCertId')
        self.name = map.get('Name')
        return self


class ModifySslVpnClientCertResponse(TeaModel):
    def __init__(self, request_id=None, name=None, ssl_vpn_client_cert_id=None):
        self.request_id = request_id
        self.name = name
        self.ssl_vpn_client_cert_id = ssl_vpn_client_cert_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.ssl_vpn_client_cert_id, 'ssl_vpn_client_cert_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Name'] = self.name
        result['SslVpnClientCertId'] = self.ssl_vpn_client_cert_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.name = map.get('Name')
        self.ssl_vpn_client_cert_id = map.get('SslVpnClientCertId')
        return self


class DescribeSslVpnServersRequest(TeaModel):
    def __init__(self, region_id=None, ssl_vpn_server_id=None, vpn_gateway_id=None, name=None, page_number=None,
                 page_size=None):
        self.region_id = region_id
        self.ssl_vpn_server_id = ssl_vpn_server_id
        self.vpn_gateway_id = vpn_gateway_id
        self.name = name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['SslVpnServerId'] = self.ssl_vpn_server_id
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['Name'] = self.name
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ssl_vpn_server_id = map.get('SslVpnServerId')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.name = map.get('Name')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeSslVpnServersResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, ssl_vpn_servers=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.ssl_vpn_servers = ssl_vpn_servers  # type: DescribeSslVpnServersResponseSslVpnServers

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.ssl_vpn_servers, 'ssl_vpn_servers')
        if self.ssl_vpn_servers:
            self.ssl_vpn_servers.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.ssl_vpn_servers is not None:
            result['SslVpnServers'] = self.ssl_vpn_servers.to_map()
        else:
            result['SslVpnServers'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('SslVpnServers') is not None:
            temp_model = DescribeSslVpnServersResponseSslVpnServers()
            self.ssl_vpn_servers = temp_model.from_map(map['SslVpnServers'])
        else:
            self.ssl_vpn_servers = None
        return self


class DescribeSslVpnServersResponseSslVpnServersSslVpnServer(TeaModel):
    def __init__(self, region_id=None, ssl_vpn_server_id=None, vpn_gateway_id=None, name=None, local_subnet=None,
                 client_ip_pool=None, create_time=None, cipher=None, proto=None, port=None, compress=None, connections=None,
                 max_connections=None, internet_ip=None, enable_multi_factor_auth=None, idaa_sinstance_id=None):
        self.region_id = region_id
        self.ssl_vpn_server_id = ssl_vpn_server_id
        self.vpn_gateway_id = vpn_gateway_id
        self.name = name
        self.local_subnet = local_subnet
        self.client_ip_pool = client_ip_pool
        self.create_time = create_time
        self.cipher = cipher
        self.proto = proto
        self.port = port
        self.compress = compress
        self.connections = connections
        self.max_connections = max_connections
        self.internet_ip = internet_ip
        self.enable_multi_factor_auth = enable_multi_factor_auth
        self.idaa_sinstance_id = idaa_sinstance_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ssl_vpn_server_id, 'ssl_vpn_server_id')
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.local_subnet, 'local_subnet')
        self.validate_required(self.client_ip_pool, 'client_ip_pool')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.cipher, 'cipher')
        self.validate_required(self.proto, 'proto')
        self.validate_required(self.port, 'port')
        self.validate_required(self.compress, 'compress')
        self.validate_required(self.connections, 'connections')
        self.validate_required(self.max_connections, 'max_connections')
        self.validate_required(self.internet_ip, 'internet_ip')
        self.validate_required(self.enable_multi_factor_auth, 'enable_multi_factor_auth')
        self.validate_required(self.idaa_sinstance_id, 'idaa_sinstance_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['SslVpnServerId'] = self.ssl_vpn_server_id
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['Name'] = self.name
        result['LocalSubnet'] = self.local_subnet
        result['ClientIpPool'] = self.client_ip_pool
        result['CreateTime'] = self.create_time
        result['Cipher'] = self.cipher
        result['Proto'] = self.proto
        result['Port'] = self.port
        result['Compress'] = self.compress
        result['Connections'] = self.connections
        result['MaxConnections'] = self.max_connections
        result['InternetIp'] = self.internet_ip
        result['EnableMultiFactorAuth'] = self.enable_multi_factor_auth
        result['IDaaSInstanceId'] = self.idaa_sinstance_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ssl_vpn_server_id = map.get('SslVpnServerId')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.name = map.get('Name')
        self.local_subnet = map.get('LocalSubnet')
        self.client_ip_pool = map.get('ClientIpPool')
        self.create_time = map.get('CreateTime')
        self.cipher = map.get('Cipher')
        self.proto = map.get('Proto')
        self.port = map.get('Port')
        self.compress = map.get('Compress')
        self.connections = map.get('Connections')
        self.max_connections = map.get('MaxConnections')
        self.internet_ip = map.get('InternetIp')
        self.enable_multi_factor_auth = map.get('EnableMultiFactorAuth')
        self.idaa_sinstance_id = map.get('IDaaSInstanceId')
        return self


class DescribeSslVpnServersResponseSslVpnServers(TeaModel):
    def __init__(self, ssl_vpn_server=None):
        self.ssl_vpn_server = ssl_vpn_server

    def validate(self):
        self.validate_required(self.ssl_vpn_server, 'ssl_vpn_server')
        if self.ssl_vpn_server:
            for k in self.ssl_vpn_server:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['SslVpnServer'] = []
        if self.ssl_vpn_server is not None:
            for k in self.ssl_vpn_server:
                result['SslVpnServer'].append(k.to_map() if k else None)
        else:
            result['SslVpnServer'] = None
        return result

    def from_map(self, map={}):
        self.ssl_vpn_server = []
        if map.get('SslVpnServer') is not None:
            for k in map.get('SslVpnServer'):
                temp_model = DescribeSslVpnServersResponseSslVpnServersSslVpnServer()
                self.ssl_vpn_server.append(temp_model.from_map(k))
        else:
            self.ssl_vpn_server = None
        return self


class DescribeSslVpnClientCertsRequest(TeaModel):
    def __init__(self, region_id=None, ssl_vpn_server_id=None, ssl_vpn_client_cert_id=None, name=None,
                 page_number=None, page_size=None):
        self.region_id = region_id
        self.ssl_vpn_server_id = ssl_vpn_server_id
        self.ssl_vpn_client_cert_id = ssl_vpn_client_cert_id
        self.name = name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['SslVpnServerId'] = self.ssl_vpn_server_id
        result['SslVpnClientCertId'] = self.ssl_vpn_client_cert_id
        result['Name'] = self.name
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ssl_vpn_server_id = map.get('SslVpnServerId')
        self.ssl_vpn_client_cert_id = map.get('SslVpnClientCertId')
        self.name = map.get('Name')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeSslVpnClientCertsResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None,
                 ssl_vpn_client_cert_keys=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.ssl_vpn_client_cert_keys = ssl_vpn_client_cert_keys  # type: DescribeSslVpnClientCertsResponseSslVpnClientCertKeys

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.ssl_vpn_client_cert_keys, 'ssl_vpn_client_cert_keys')
        if self.ssl_vpn_client_cert_keys:
            self.ssl_vpn_client_cert_keys.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.ssl_vpn_client_cert_keys is not None:
            result['SslVpnClientCertKeys'] = self.ssl_vpn_client_cert_keys.to_map()
        else:
            result['SslVpnClientCertKeys'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('SslVpnClientCertKeys') is not None:
            temp_model = DescribeSslVpnClientCertsResponseSslVpnClientCertKeys()
            self.ssl_vpn_client_cert_keys = temp_model.from_map(map['SslVpnClientCertKeys'])
        else:
            self.ssl_vpn_client_cert_keys = None
        return self


class DescribeSslVpnClientCertsResponseSslVpnClientCertKeysSslVpnClientCertKey(TeaModel):
    def __init__(self, region_id=None, ssl_vpn_client_cert_id=None, name=None, ssl_vpn_server_id=None,
                 create_time=None, end_time=None, status=None):
        self.region_id = region_id
        self.ssl_vpn_client_cert_id = ssl_vpn_client_cert_id
        self.name = name
        self.ssl_vpn_server_id = ssl_vpn_server_id
        self.create_time = create_time
        self.end_time = end_time
        self.status = status

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ssl_vpn_client_cert_id, 'ssl_vpn_client_cert_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.ssl_vpn_server_id, 'ssl_vpn_server_id')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['SslVpnClientCertId'] = self.ssl_vpn_client_cert_id
        result['Name'] = self.name
        result['SslVpnServerId'] = self.ssl_vpn_server_id
        result['CreateTime'] = self.create_time
        result['EndTime'] = self.end_time
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ssl_vpn_client_cert_id = map.get('SslVpnClientCertId')
        self.name = map.get('Name')
        self.ssl_vpn_server_id = map.get('SslVpnServerId')
        self.create_time = map.get('CreateTime')
        self.end_time = map.get('EndTime')
        self.status = map.get('Status')
        return self


class DescribeSslVpnClientCertsResponseSslVpnClientCertKeys(TeaModel):
    def __init__(self, ssl_vpn_client_cert_key=None):
        self.ssl_vpn_client_cert_key = ssl_vpn_client_cert_key

    def validate(self):
        self.validate_required(self.ssl_vpn_client_cert_key, 'ssl_vpn_client_cert_key')
        if self.ssl_vpn_client_cert_key:
            for k in self.ssl_vpn_client_cert_key:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['SslVpnClientCertKey'] = []
        if self.ssl_vpn_client_cert_key is not None:
            for k in self.ssl_vpn_client_cert_key:
                result['SslVpnClientCertKey'].append(k.to_map() if k else None)
        else:
            result['SslVpnClientCertKey'] = None
        return result

    def from_map(self, map={}):
        self.ssl_vpn_client_cert_key = []
        if map.get('SslVpnClientCertKey') is not None:
            for k in map.get('SslVpnClientCertKey'):
                temp_model = DescribeSslVpnClientCertsResponseSslVpnClientCertKeysSslVpnClientCertKey()
                self.ssl_vpn_client_cert_key.append(temp_model.from_map(k))
        else:
            self.ssl_vpn_client_cert_key = None
        return self


class DescribeSslVpnClientCertRequest(TeaModel):
    def __init__(self, region_id=None, ssl_vpn_client_cert_id=None):
        self.region_id = region_id
        self.ssl_vpn_client_cert_id = ssl_vpn_client_cert_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ssl_vpn_client_cert_id, 'ssl_vpn_client_cert_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['SslVpnClientCertId'] = self.ssl_vpn_client_cert_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ssl_vpn_client_cert_id = map.get('SslVpnClientCertId')
        return self


class DescribeSslVpnClientCertResponse(TeaModel):
    def __init__(self, request_id=None, region_id=None, ssl_vpn_client_cert_id=None, name=None,
                 ssl_vpn_server_id=None, ca_cert=None, client_cert=None, client_key=None, client_config=None, create_time=None,
                 end_time=None, status=None):
        self.request_id = request_id
        self.region_id = region_id
        self.ssl_vpn_client_cert_id = ssl_vpn_client_cert_id
        self.name = name
        self.ssl_vpn_server_id = ssl_vpn_server_id
        self.ca_cert = ca_cert
        self.client_cert = client_cert
        self.client_key = client_key
        self.client_config = client_config
        self.create_time = create_time
        self.end_time = end_time
        self.status = status

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ssl_vpn_client_cert_id, 'ssl_vpn_client_cert_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.ssl_vpn_server_id, 'ssl_vpn_server_id')
        self.validate_required(self.ca_cert, 'ca_cert')
        self.validate_required(self.client_cert, 'client_cert')
        self.validate_required(self.client_key, 'client_key')
        self.validate_required(self.client_config, 'client_config')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['RegionId'] = self.region_id
        result['SslVpnClientCertId'] = self.ssl_vpn_client_cert_id
        result['Name'] = self.name
        result['SslVpnServerId'] = self.ssl_vpn_server_id
        result['CaCert'] = self.ca_cert
        result['ClientCert'] = self.client_cert
        result['ClientKey'] = self.client_key
        result['ClientConfig'] = self.client_config
        result['CreateTime'] = self.create_time
        result['EndTime'] = self.end_time
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.region_id = map.get('RegionId')
        self.ssl_vpn_client_cert_id = map.get('SslVpnClientCertId')
        self.name = map.get('Name')
        self.ssl_vpn_server_id = map.get('SslVpnServerId')
        self.ca_cert = map.get('CaCert')
        self.client_cert = map.get('ClientCert')
        self.client_key = map.get('ClientKey')
        self.client_config = map.get('ClientConfig')
        self.create_time = map.get('CreateTime')
        self.end_time = map.get('EndTime')
        self.status = map.get('Status')
        return self


class DeleteSslVpnServerRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, ssl_vpn_server_id=None):
        self.region_id = region_id
        self.client_token = client_token
        self.ssl_vpn_server_id = ssl_vpn_server_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ssl_vpn_server_id, 'ssl_vpn_server_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['SslVpnServerId'] = self.ssl_vpn_server_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.ssl_vpn_server_id = map.get('SslVpnServerId')
        return self


class DeleteSslVpnServerResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteSslVpnClientCertRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, ssl_vpn_client_cert_id=None):
        self.region_id = region_id
        self.client_token = client_token
        self.ssl_vpn_client_cert_id = ssl_vpn_client_cert_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ssl_vpn_client_cert_id, 'ssl_vpn_client_cert_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['SslVpnClientCertId'] = self.ssl_vpn_client_cert_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.ssl_vpn_client_cert_id = map.get('SslVpnClientCertId')
        return self


class DeleteSslVpnClientCertResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateSslVpnServerRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, vpn_gateway_id=None, name=None, client_ip_pool=None,
                 local_subnet=None, proto=None, cipher=None, port=None, compress=None, enable_multi_factor_auth=None,
                 idaa_sinstance_id=None):
        self.client_token = client_token
        self.region_id = region_id
        self.vpn_gateway_id = vpn_gateway_id
        self.name = name
        self.client_ip_pool = client_ip_pool
        self.local_subnet = local_subnet
        self.proto = proto
        self.cipher = cipher
        self.port = port
        self.compress = compress
        self.enable_multi_factor_auth = enable_multi_factor_auth
        self.idaa_sinstance_id = idaa_sinstance_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')
        self.validate_required(self.client_ip_pool, 'client_ip_pool')
        self.validate_required(self.local_subnet, 'local_subnet')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['Name'] = self.name
        result['ClientIpPool'] = self.client_ip_pool
        result['LocalSubnet'] = self.local_subnet
        result['Proto'] = self.proto
        result['Cipher'] = self.cipher
        result['Port'] = self.port
        result['Compress'] = self.compress
        result['EnableMultiFactorAuth'] = self.enable_multi_factor_auth
        result['IDaaSInstanceId'] = self.idaa_sinstance_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.name = map.get('Name')
        self.client_ip_pool = map.get('ClientIpPool')
        self.local_subnet = map.get('LocalSubnet')
        self.proto = map.get('Proto')
        self.cipher = map.get('Cipher')
        self.port = map.get('Port')
        self.compress = map.get('Compress')
        self.enable_multi_factor_auth = map.get('EnableMultiFactorAuth')
        self.idaa_sinstance_id = map.get('IDaaSInstanceId')
        return self


class CreateSslVpnServerResponse(TeaModel):
    def __init__(self, request_id=None, ssl_vpn_server_id=None, name=None):
        self.request_id = request_id
        self.ssl_vpn_server_id = ssl_vpn_server_id
        self.name = name

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.ssl_vpn_server_id, 'ssl_vpn_server_id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['SslVpnServerId'] = self.ssl_vpn_server_id
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.ssl_vpn_server_id = map.get('SslVpnServerId')
        self.name = map.get('Name')
        return self


class CreateSslVpnClientCertRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, ssl_vpn_server_id=None, name=None):
        self.client_token = client_token
        self.region_id = region_id
        self.ssl_vpn_server_id = ssl_vpn_server_id
        self.name = name

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ssl_vpn_server_id, 'ssl_vpn_server_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['SslVpnServerId'] = self.ssl_vpn_server_id
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.ssl_vpn_server_id = map.get('SslVpnServerId')
        self.name = map.get('Name')
        return self


class CreateSslVpnClientCertResponse(TeaModel):
    def __init__(self, request_id=None, name=None, ssl_vpn_client_cert_id=None):
        self.request_id = request_id
        self.name = name
        self.ssl_vpn_client_cert_id = ssl_vpn_client_cert_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.ssl_vpn_client_cert_id, 'ssl_vpn_client_cert_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Name'] = self.name
        result['SslVpnClientCertId'] = self.ssl_vpn_client_cert_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.name = map.get('Name')
        self.ssl_vpn_client_cert_id = map.get('SslVpnClientCertId')
        return self


class RemoveGlobalAccelerationInstanceIpRequest(TeaModel):
    def __init__(self, region_id=None, global_acceleration_instance_id=None, ip_instance_id=None):
        self.region_id = region_id
        self.global_acceleration_instance_id = global_acceleration_instance_id
        self.ip_instance_id = ip_instance_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.global_acceleration_instance_id, 'global_acceleration_instance_id')
        self.validate_required(self.ip_instance_id, 'ip_instance_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['GlobalAccelerationInstanceId'] = self.global_acceleration_instance_id
        result['IpInstanceId'] = self.ip_instance_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.global_acceleration_instance_id = map.get('GlobalAccelerationInstanceId')
        self.ip_instance_id = map.get('IpInstanceId')
        return self


class RemoveGlobalAccelerationInstanceIpResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AddGlobalAccelerationInstanceIpRequest(TeaModel):
    def __init__(self, region_id=None, global_acceleration_instance_id=None, ip_instance_id=None):
        self.region_id = region_id
        self.global_acceleration_instance_id = global_acceleration_instance_id
        self.ip_instance_id = ip_instance_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.global_acceleration_instance_id, 'global_acceleration_instance_id')
        self.validate_required(self.ip_instance_id, 'ip_instance_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['GlobalAccelerationInstanceId'] = self.global_acceleration_instance_id
        result['IpInstanceId'] = self.ip_instance_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.global_acceleration_instance_id = map.get('GlobalAccelerationInstanceId')
        self.ip_instance_id = map.get('IpInstanceId')
        return self


class AddGlobalAccelerationInstanceIpResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeRouteTableListRequest(TeaModel):
    def __init__(self, router_type=None, router_id=None, vpc_id=None, route_table_id=None, route_table_name=None,
                 page_number=None, page_size=None, resource_group_id=None, region_id=None):
        self.router_type = router_type
        self.router_id = router_id
        self.vpc_id = vpc_id
        self.route_table_id = route_table_id
        self.route_table_name = route_table_name
        self.page_number = page_number
        self.page_size = page_size
        self.resource_group_id = resource_group_id
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RouterType'] = self.router_type
        result['RouterId'] = self.router_id
        result['VpcId'] = self.vpc_id
        result['RouteTableId'] = self.route_table_id
        result['RouteTableName'] = self.route_table_name
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['ResourceGroupId'] = self.resource_group_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.router_type = map.get('RouterType')
        self.router_id = map.get('RouterId')
        self.vpc_id = map.get('VpcId')
        self.route_table_id = map.get('RouteTableId')
        self.route_table_name = map.get('RouteTableName')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.resource_group_id = map.get('ResourceGroupId')
        self.region_id = map.get('RegionId')
        return self


class DescribeRouteTableListResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, success=None, page_size=None, page_number=None,
                 total_count=None, router_table_list=None):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.success = success
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count
        self.router_table_list = router_table_list  # type: DescribeRouteTableListResponseRouterTableList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.success, 'success')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.router_table_list, 'router_table_list')
        if self.router_table_list:
            self.router_table_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        result['Success'] = self.success
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        result['TotalCount'] = self.total_count
        if self.router_table_list is not None:
            result['RouterTableList'] = self.router_table_list.to_map()
        else:
            result['RouterTableList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.success = map.get('Success')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        self.total_count = map.get('TotalCount')
        if map.get('RouterTableList') is not None:
            temp_model = DescribeRouteTableListResponseRouterTableList()
            self.router_table_list = temp_model.from_map(map['RouterTableList'])
        else:
            self.router_table_list = None
        return self


class DescribeRouteTableListResponseRouterTableListRouterTableListTypeTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class DescribeRouteTableListResponseRouterTableListRouterTableListTypeTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag

    def validate(self):
        self.validate_required(self.tag, 'tag')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        return result

    def from_map(self, map={}):
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = DescribeRouteTableListResponseRouterTableListRouterTableListTypeTagsTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        return self


class DescribeRouteTableListResponseRouterTableListRouterTableListTypeVSwitchIds(TeaModel):
    def __init__(self, v_switch_id=None):
        # VSwitchId
        self.v_switch_id = v_switch_id

    def validate(self):
        self.validate_required(self.v_switch_id, 'v_switch_id')

    def to_map(self):
        result = {}
        result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, map={}):
        self.v_switch_id = map.get('VSwitchId')
        return self


class DescribeRouteTableListResponseRouterTableListRouterTableListType(TeaModel):
    def __init__(self, vpc_id=None, router_type=None, router_id=None, route_table_id=None, route_table_name=None,
                 route_table_type=None, description=None, resource_group_id=None, creation_time=None, status=None, owner_id=None,
                 tags=None, v_switch_ids=None):
        self.vpc_id = vpc_id
        self.router_type = router_type
        self.router_id = router_id
        self.route_table_id = route_table_id
        self.route_table_name = route_table_name
        self.route_table_type = route_table_type
        self.description = description
        self.resource_group_id = resource_group_id
        self.creation_time = creation_time
        self.status = status
        self.owner_id = owner_id
        self.tags = tags  # type: DescribeRouteTableListResponseRouterTableListRouterTableListTypeTags
        self.v_switch_ids = v_switch_ids  # type: DescribeRouteTableListResponseRouterTableListRouterTableListTypeVSwitchIds

    def validate(self):
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.router_type, 'router_type')
        self.validate_required(self.router_id, 'router_id')
        self.validate_required(self.route_table_id, 'route_table_id')
        self.validate_required(self.route_table_name, 'route_table_name')
        self.validate_required(self.route_table_type, 'route_table_type')
        self.validate_required(self.description, 'description')
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.tags, 'tags')
        if self.tags:
            self.tags.validate()
        self.validate_required(self.v_switch_ids, 'v_switch_ids')
        if self.v_switch_ids:
            self.v_switch_ids.validate()

    def to_map(self):
        result = {}
        result['VpcId'] = self.vpc_id
        result['RouterType'] = self.router_type
        result['RouterId'] = self.router_id
        result['RouteTableId'] = self.route_table_id
        result['RouteTableName'] = self.route_table_name
        result['RouteTableType'] = self.route_table_type
        result['Description'] = self.description
        result['ResourceGroupId'] = self.resource_group_id
        result['CreationTime'] = self.creation_time
        result['Status'] = self.status
        result['OwnerId'] = self.owner_id
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        else:
            result['Tags'] = None
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids.to_map()
        else:
            result['VSwitchIds'] = None
        return result

    def from_map(self, map={}):
        self.vpc_id = map.get('VpcId')
        self.router_type = map.get('RouterType')
        self.router_id = map.get('RouterId')
        self.route_table_id = map.get('RouteTableId')
        self.route_table_name = map.get('RouteTableName')
        self.route_table_type = map.get('RouteTableType')
        self.description = map.get('Description')
        self.resource_group_id = map.get('ResourceGroupId')
        self.creation_time = map.get('CreationTime')
        self.status = map.get('Status')
        self.owner_id = map.get('OwnerId')
        if map.get('Tags') is not None:
            temp_model = DescribeRouteTableListResponseRouterTableListRouterTableListTypeTags()
            self.tags = temp_model.from_map(map['Tags'])
        else:
            self.tags = None
        if map.get('VSwitchIds') is not None:
            temp_model = DescribeRouteTableListResponseRouterTableListRouterTableListTypeVSwitchIds()
            self.v_switch_ids = temp_model.from_map(map['VSwitchIds'])
        else:
            self.v_switch_ids = None
        return self


class DescribeRouteTableListResponseRouterTableList(TeaModel):
    def __init__(self, router_table_list_type=None):
        self.router_table_list_type = router_table_list_type

    def validate(self):
        self.validate_required(self.router_table_list_type, 'router_table_list_type')
        if self.router_table_list_type:
            for k in self.router_table_list_type:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RouterTableListType'] = []
        if self.router_table_list_type is not None:
            for k in self.router_table_list_type:
                result['RouterTableListType'].append(k.to_map() if k else None)
        else:
            result['RouterTableListType'] = None
        return result

    def from_map(self, map={}):
        self.router_table_list_type = []
        if map.get('RouterTableListType') is not None:
            for k in map.get('RouterTableListType'):
                temp_model = DescribeRouteTableListResponseRouterTableListRouterTableListType()
                self.router_table_list_type.append(temp_model.from_map(k))
        else:
            self.router_table_list_type = None
        return self


class ModifyRouteTableAttributesRequest(TeaModel):
    def __init__(self, route_table_id=None, route_table_name=None, description=None, region_id=None):
        self.route_table_id = route_table_id
        self.route_table_name = route_table_name
        self.description = description
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.route_table_id, 'route_table_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RouteTableId'] = self.route_table_id
        result['RouteTableName'] = self.route_table_name
        result['Description'] = self.description
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.route_table_id = map.get('RouteTableId')
        self.route_table_name = map.get('RouteTableName')
        self.description = map.get('Description')
        self.region_id = map.get('RegionId')
        return self


class ModifyRouteTableAttributesResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, success=None):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.success = success

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.success = map.get('Success')
        return self


class DescribeBgpNetworksRequest(TeaModel):
    def __init__(self, router_id=None, region_id=None, page_number=None, page_size=None):
        self.router_id = router_id
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RouterId'] = self.router_id
        result['RegionId'] = self.region_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.router_id = map.get('RouterId')
        self.region_id = map.get('RegionId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeBgpNetworksResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, bgp_networks=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.bgp_networks = bgp_networks  # type: DescribeBgpNetworksResponseBgpNetworks

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.bgp_networks, 'bgp_networks')
        if self.bgp_networks:
            self.bgp_networks.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.bgp_networks is not None:
            result['BgpNetworks'] = self.bgp_networks.to_map()
        else:
            result['BgpNetworks'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('BgpNetworks') is not None:
            temp_model = DescribeBgpNetworksResponseBgpNetworks()
            self.bgp_networks = temp_model.from_map(map['BgpNetworks'])
        else:
            self.bgp_networks = None
        return self


class DescribeBgpNetworksResponseBgpNetworksBgpNetwork(TeaModel):
    def __init__(self, vpc_id=None, dst_cidr_block=None, router_id=None, status=None):
        self.vpc_id = vpc_id
        self.dst_cidr_block = dst_cidr_block
        self.router_id = router_id
        self.status = status

    def validate(self):
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.dst_cidr_block, 'dst_cidr_block')
        self.validate_required(self.router_id, 'router_id')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['VpcId'] = self.vpc_id
        result['DstCidrBlock'] = self.dst_cidr_block
        result['RouterId'] = self.router_id
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.vpc_id = map.get('VpcId')
        self.dst_cidr_block = map.get('DstCidrBlock')
        self.router_id = map.get('RouterId')
        self.status = map.get('Status')
        return self


class DescribeBgpNetworksResponseBgpNetworks(TeaModel):
    def __init__(self, bgp_network=None):
        self.bgp_network = bgp_network

    def validate(self):
        self.validate_required(self.bgp_network, 'bgp_network')
        if self.bgp_network:
            for k in self.bgp_network:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['BgpNetwork'] = []
        if self.bgp_network is not None:
            for k in self.bgp_network:
                result['BgpNetwork'].append(k.to_map() if k else None)
        else:
            result['BgpNetwork'] = None
        return result

    def from_map(self, map={}):
        self.bgp_network = []
        if map.get('BgpNetwork') is not None:
            for k in map.get('BgpNetwork'):
                temp_model = DescribeBgpNetworksResponseBgpNetworksBgpNetwork()
                self.bgp_network.append(temp_model.from_map(k))
        else:
            self.bgp_network = None
        return self


class ModifyCommonBandwidthPackagePayTypeRequest(TeaModel):
    def __init__(self, bandwidth_package_id=None, pay_type=None, pricing_cycle=None, duration=None, auto_pay=None,
                 bandwidth=None, kbps_bandwidth=None, resource_bid=None, resource_uid=None, region_id=None):
        self.bandwidth_package_id = bandwidth_package_id
        self.pay_type = pay_type
        self.pricing_cycle = pricing_cycle
        self.duration = duration
        self.auto_pay = auto_pay
        self.bandwidth = bandwidth
        self.kbps_bandwidth = kbps_bandwidth
        self.resource_bid = resource_bid
        self.resource_uid = resource_uid
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.bandwidth_package_id, 'bandwidth_package_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['BandwidthPackageId'] = self.bandwidth_package_id
        result['PayType'] = self.pay_type
        result['PricingCycle'] = self.pricing_cycle
        result['Duration'] = self.duration
        result['AutoPay'] = self.auto_pay
        result['Bandwidth'] = self.bandwidth
        result['KbpsBandwidth'] = self.kbps_bandwidth
        result['ResourceBid'] = self.resource_bid
        result['ResourceUid'] = self.resource_uid
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        self.pay_type = map.get('PayType')
        self.pricing_cycle = map.get('PricingCycle')
        self.duration = map.get('Duration')
        self.auto_pay = map.get('AutoPay')
        self.bandwidth = map.get('Bandwidth')
        self.kbps_bandwidth = map.get('KbpsBandwidth')
        self.resource_bid = map.get('ResourceBid')
        self.resource_uid = map.get('ResourceUid')
        self.region_id = map.get('RegionId')
        return self


class ModifyCommonBandwidthPackagePayTypeResponse(TeaModel):
    def __init__(self, request_id=None, order_id=None, code=None, message=None):
        self.request_id = request_id
        self.order_id = order_id
        self.code = code
        self.message = message

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['OrderId'] = self.order_id
        result['Code'] = self.code
        result['Message'] = self.message
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.order_id = map.get('OrderId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        return self


class UnassociateGlobalAccelerationInstanceRequest(TeaModel):
    def __init__(self, region_id=None, global_acceleration_instance_id=None, instance_type=None):
        self.region_id = region_id
        self.global_acceleration_instance_id = global_acceleration_instance_id
        self.instance_type = instance_type

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.global_acceleration_instance_id, 'global_acceleration_instance_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['GlobalAccelerationInstanceId'] = self.global_acceleration_instance_id
        result['InstanceType'] = self.instance_type
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.global_acceleration_instance_id = map.get('GlobalAccelerationInstanceId')
        self.instance_type = map.get('InstanceType')
        return self


class UnassociateGlobalAccelerationInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyGlobalAccelerationInstanceSpecRequest(TeaModel):
    def __init__(self, region_id=None, global_acceleration_instance_id=None, bandwidth=None):
        self.region_id = region_id
        self.global_acceleration_instance_id = global_acceleration_instance_id
        self.bandwidth = bandwidth

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.global_acceleration_instance_id, 'global_acceleration_instance_id')
        self.validate_required(self.bandwidth, 'bandwidth')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['GlobalAccelerationInstanceId'] = self.global_acceleration_instance_id
        result['Bandwidth'] = self.bandwidth
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.global_acceleration_instance_id = map.get('GlobalAccelerationInstanceId')
        self.bandwidth = map.get('Bandwidth')
        return self


class ModifyGlobalAccelerationInstanceSpecResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyGlobalAccelerationInstanceAttributesRequest(TeaModel):
    def __init__(self, region_id=None, global_acceleration_instance_id=None, name=None, description=None):
        self.region_id = region_id
        self.global_acceleration_instance_id = global_acceleration_instance_id
        self.name = name
        self.description = description

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.global_acceleration_instance_id, 'global_acceleration_instance_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['GlobalAccelerationInstanceId'] = self.global_acceleration_instance_id
        result['Name'] = self.name
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.global_acceleration_instance_id = map.get('GlobalAccelerationInstanceId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        return self


class ModifyGlobalAccelerationInstanceAttributesResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeServerRelatedGlobalAccelerationInstancesRequest(TeaModel):
    def __init__(self, region_id=None, server_id=None, server_type=None):
        self.region_id = region_id
        self.server_id = server_id
        self.server_type = server_type

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.server_id, 'server_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ServerId'] = self.server_id
        result['ServerType'] = self.server_type
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.server_id = map.get('ServerId')
        self.server_type = map.get('ServerType')
        return self


class DescribeServerRelatedGlobalAccelerationInstancesResponse(TeaModel):
    def __init__(self, request_id=None, global_acceleration_instances=None):
        self.request_id = request_id
        self.global_acceleration_instances = global_acceleration_instances  # type: DescribeServerRelatedGlobalAccelerationInstancesResponseGlobalAccelerationInstances

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.global_acceleration_instances, 'global_acceleration_instances')
        if self.global_acceleration_instances:
            self.global_acceleration_instances.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.global_acceleration_instances is not None:
            result['GlobalAccelerationInstances'] = self.global_acceleration_instances.to_map()
        else:
            result['GlobalAccelerationInstances'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('GlobalAccelerationInstances') is not None:
            temp_model = DescribeServerRelatedGlobalAccelerationInstancesResponseGlobalAccelerationInstances()
            self.global_acceleration_instances = temp_model.from_map(map['GlobalAccelerationInstances'])
        else:
            self.global_acceleration_instances = None
        return self


class DescribeServerRelatedGlobalAccelerationInstancesResponseGlobalAccelerationInstancesGlobalAccelerationInstance(TeaModel):
    def __init__(self, region_id=None, global_acceleration_instance_id=None, ip_address=None,
                 server_ip_address=None):
        self.region_id = region_id
        self.global_acceleration_instance_id = global_acceleration_instance_id
        self.ip_address = ip_address
        self.server_ip_address = server_ip_address

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.global_acceleration_instance_id, 'global_acceleration_instance_id')
        self.validate_required(self.ip_address, 'ip_address')
        self.validate_required(self.server_ip_address, 'server_ip_address')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['GlobalAccelerationInstanceId'] = self.global_acceleration_instance_id
        result['IpAddress'] = self.ip_address
        result['ServerIpAddress'] = self.server_ip_address
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.global_acceleration_instance_id = map.get('GlobalAccelerationInstanceId')
        self.ip_address = map.get('IpAddress')
        self.server_ip_address = map.get('ServerIpAddress')
        return self


class DescribeServerRelatedGlobalAccelerationInstancesResponseGlobalAccelerationInstances(TeaModel):
    def __init__(self, global_acceleration_instance=None):
        self.global_acceleration_instance = global_acceleration_instance

    def validate(self):
        self.validate_required(self.global_acceleration_instance, 'global_acceleration_instance')
        if self.global_acceleration_instance:
            for k in self.global_acceleration_instance:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['GlobalAccelerationInstance'] = []
        if self.global_acceleration_instance is not None:
            for k in self.global_acceleration_instance:
                result['GlobalAccelerationInstance'].append(k.to_map() if k else None)
        else:
            result['GlobalAccelerationInstance'] = None
        return result

    def from_map(self, map={}):
        self.global_acceleration_instance = []
        if map.get('GlobalAccelerationInstance') is not None:
            for k in map.get('GlobalAccelerationInstance'):
                temp_model = DescribeServerRelatedGlobalAccelerationInstancesResponseGlobalAccelerationInstancesGlobalAccelerationInstance()
                self.global_acceleration_instance.append(temp_model.from_map(k))
        else:
            self.global_acceleration_instance = None
        return self


class DescribeGlobalAccelerationInstancesRequest(TeaModel):
    def __init__(self, region_id=None, include_reservation_data=None, global_acceleration_instance_id=None,
                 ip_address=None, name=None, status=None, bandwidth_type=None, service_location=None, server_id=None,
                 page_number=None, page_size=None):
        self.region_id = region_id
        self.include_reservation_data = include_reservation_data
        self.global_acceleration_instance_id = global_acceleration_instance_id
        self.ip_address = ip_address
        self.name = name
        self.status = status
        self.bandwidth_type = bandwidth_type
        self.service_location = service_location
        self.server_id = server_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['IncludeReservationData'] = self.include_reservation_data
        result['GlobalAccelerationInstanceId'] = self.global_acceleration_instance_id
        result['IpAddress'] = self.ip_address
        result['Name'] = self.name
        result['Status'] = self.status
        result['BandwidthType'] = self.bandwidth_type
        result['ServiceLocation'] = self.service_location
        result['ServerId'] = self.server_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.include_reservation_data = map.get('IncludeReservationData')
        self.global_acceleration_instance_id = map.get('GlobalAccelerationInstanceId')
        self.ip_address = map.get('IpAddress')
        self.name = map.get('Name')
        self.status = map.get('Status')
        self.bandwidth_type = map.get('BandwidthType')
        self.service_location = map.get('ServiceLocation')
        self.server_id = map.get('ServerId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeGlobalAccelerationInstancesResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None,
                 global_acceleration_instances=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.global_acceleration_instances = global_acceleration_instances  # type: DescribeGlobalAccelerationInstancesResponseGlobalAccelerationInstances

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.global_acceleration_instances, 'global_acceleration_instances')
        if self.global_acceleration_instances:
            self.global_acceleration_instances.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.global_acceleration_instances is not None:
            result['GlobalAccelerationInstances'] = self.global_acceleration_instances.to_map()
        else:
            result['GlobalAccelerationInstances'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('GlobalAccelerationInstances') is not None:
            temp_model = DescribeGlobalAccelerationInstancesResponseGlobalAccelerationInstances()
            self.global_acceleration_instances = temp_model.from_map(map['GlobalAccelerationInstances'])
        else:
            self.global_acceleration_instances = None
        return self


class DescribeGlobalAccelerationInstancesResponseGlobalAccelerationInstancesGlobalAccelerationInstanceBackendServersBackendServer(TeaModel):
    def __init__(self, region_id=None, server_id=None, server_ip_address=None, server_type=None):
        self.region_id = region_id
        self.server_id = server_id
        self.server_ip_address = server_ip_address
        self.server_type = server_type

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.server_id, 'server_id')
        self.validate_required(self.server_ip_address, 'server_ip_address')
        self.validate_required(self.server_type, 'server_type')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ServerId'] = self.server_id
        result['ServerIpAddress'] = self.server_ip_address
        result['ServerType'] = self.server_type
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.server_id = map.get('ServerId')
        self.server_ip_address = map.get('ServerIpAddress')
        self.server_type = map.get('ServerType')
        return self


class DescribeGlobalAccelerationInstancesResponseGlobalAccelerationInstancesGlobalAccelerationInstanceBackendServers(TeaModel):
    def __init__(self, backend_server=None):
        self.backend_server = backend_server

    def validate(self):
        self.validate_required(self.backend_server, 'backend_server')
        if self.backend_server:
            for k in self.backend_server:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['BackendServer'] = []
        if self.backend_server is not None:
            for k in self.backend_server:
                result['BackendServer'].append(k.to_map() if k else None)
        else:
            result['BackendServer'] = None
        return result

    def from_map(self, map={}):
        self.backend_server = []
        if map.get('BackendServer') is not None:
            for k in map.get('BackendServer'):
                temp_model = DescribeGlobalAccelerationInstancesResponseGlobalAccelerationInstancesGlobalAccelerationInstanceBackendServersBackendServer()
                self.backend_server.append(temp_model.from_map(k))
        else:
            self.backend_server = None
        return self


class DescribeGlobalAccelerationInstancesResponseGlobalAccelerationInstancesGlobalAccelerationInstancePublicIpAddressesPublicIpAddress(TeaModel):
    def __init__(self, allocation_id=None, ip_address=None):
        self.allocation_id = allocation_id
        self.ip_address = ip_address

    def validate(self):
        self.validate_required(self.allocation_id, 'allocation_id')
        self.validate_required(self.ip_address, 'ip_address')

    def to_map(self):
        result = {}
        result['AllocationId'] = self.allocation_id
        result['IpAddress'] = self.ip_address
        return result

    def from_map(self, map={}):
        self.allocation_id = map.get('AllocationId')
        self.ip_address = map.get('IpAddress')
        return self


class DescribeGlobalAccelerationInstancesResponseGlobalAccelerationInstancesGlobalAccelerationInstancePublicIpAddresses(TeaModel):
    def __init__(self, public_ip_address=None):
        self.public_ip_address = public_ip_address

    def validate(self):
        self.validate_required(self.public_ip_address, 'public_ip_address')
        if self.public_ip_address:
            for k in self.public_ip_address:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PublicIpAddress'] = []
        if self.public_ip_address is not None:
            for k in self.public_ip_address:
                result['PublicIpAddress'].append(k.to_map() if k else None)
        else:
            result['PublicIpAddress'] = None
        return result

    def from_map(self, map={}):
        self.public_ip_address = []
        if map.get('PublicIpAddress') is not None:
            for k in map.get('PublicIpAddress'):
                temp_model = DescribeGlobalAccelerationInstancesResponseGlobalAccelerationInstancesGlobalAccelerationInstancePublicIpAddressesPublicIpAddress()
                self.public_ip_address.append(temp_model.from_map(k))
        else:
            self.public_ip_address = None
        return self


class DescribeGlobalAccelerationInstancesResponseGlobalAccelerationInstancesGlobalAccelerationInstance(TeaModel):
    def __init__(self, region_id=None, global_acceleration_instance_id=None, ip_address=None, status=None,
                 bandwidth=None, internet_charge_type=None, charge_type=None, bandwidth_type=None,
                 acceleration_location=None, service_location=None, name=None, description=None, expired_time=None, creation_time=None,
                 has_reservation_data=None, reservation_bandwidth=None, reservation_internet_charge_type=None,
                 reservation_active_time=None, reservation_order_type=None, backend_servers=None, public_ip_addresses=None):
        self.region_id = region_id
        self.global_acceleration_instance_id = global_acceleration_instance_id
        self.ip_address = ip_address
        self.status = status
        self.bandwidth = bandwidth
        self.internet_charge_type = internet_charge_type
        self.charge_type = charge_type
        self.bandwidth_type = bandwidth_type
        self.acceleration_location = acceleration_location
        self.service_location = service_location
        self.name = name
        self.description = description
        self.expired_time = expired_time
        self.creation_time = creation_time
        self.has_reservation_data = has_reservation_data
        self.reservation_bandwidth = reservation_bandwidth
        self.reservation_internet_charge_type = reservation_internet_charge_type
        self.reservation_active_time = reservation_active_time
        self.reservation_order_type = reservation_order_type
        self.backend_servers = backend_servers  # type: DescribeGlobalAccelerationInstancesResponseGlobalAccelerationInstancesGlobalAccelerationInstanceBackendServers
        self.public_ip_addresses = public_ip_addresses  # type: DescribeGlobalAccelerationInstancesResponseGlobalAccelerationInstancesGlobalAccelerationInstancePublicIpAddresses

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.global_acceleration_instance_id, 'global_acceleration_instance_id')
        self.validate_required(self.ip_address, 'ip_address')
        self.validate_required(self.status, 'status')
        self.validate_required(self.bandwidth, 'bandwidth')
        self.validate_required(self.internet_charge_type, 'internet_charge_type')
        self.validate_required(self.charge_type, 'charge_type')
        self.validate_required(self.bandwidth_type, 'bandwidth_type')
        self.validate_required(self.acceleration_location, 'acceleration_location')
        self.validate_required(self.service_location, 'service_location')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.expired_time, 'expired_time')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.has_reservation_data, 'has_reservation_data')
        self.validate_required(self.reservation_bandwidth, 'reservation_bandwidth')
        self.validate_required(self.reservation_internet_charge_type, 'reservation_internet_charge_type')
        self.validate_required(self.reservation_active_time, 'reservation_active_time')
        self.validate_required(self.reservation_order_type, 'reservation_order_type')
        self.validate_required(self.backend_servers, 'backend_servers')
        if self.backend_servers:
            self.backend_servers.validate()
        self.validate_required(self.public_ip_addresses, 'public_ip_addresses')
        if self.public_ip_addresses:
            self.public_ip_addresses.validate()

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['GlobalAccelerationInstanceId'] = self.global_acceleration_instance_id
        result['IpAddress'] = self.ip_address
        result['Status'] = self.status
        result['Bandwidth'] = self.bandwidth
        result['InternetChargeType'] = self.internet_charge_type
        result['ChargeType'] = self.charge_type
        result['BandwidthType'] = self.bandwidth_type
        result['AccelerationLocation'] = self.acceleration_location
        result['ServiceLocation'] = self.service_location
        result['Name'] = self.name
        result['Description'] = self.description
        result['ExpiredTime'] = self.expired_time
        result['CreationTime'] = self.creation_time
        result['HasReservationData'] = self.has_reservation_data
        result['ReservationBandwidth'] = self.reservation_bandwidth
        result['ReservationInternetChargeType'] = self.reservation_internet_charge_type
        result['ReservationActiveTime'] = self.reservation_active_time
        result['ReservationOrderType'] = self.reservation_order_type
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers.to_map()
        else:
            result['BackendServers'] = None
        if self.public_ip_addresses is not None:
            result['PublicIpAddresses'] = self.public_ip_addresses.to_map()
        else:
            result['PublicIpAddresses'] = None
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.global_acceleration_instance_id = map.get('GlobalAccelerationInstanceId')
        self.ip_address = map.get('IpAddress')
        self.status = map.get('Status')
        self.bandwidth = map.get('Bandwidth')
        self.internet_charge_type = map.get('InternetChargeType')
        self.charge_type = map.get('ChargeType')
        self.bandwidth_type = map.get('BandwidthType')
        self.acceleration_location = map.get('AccelerationLocation')
        self.service_location = map.get('ServiceLocation')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.expired_time = map.get('ExpiredTime')
        self.creation_time = map.get('CreationTime')
        self.has_reservation_data = map.get('HasReservationData')
        self.reservation_bandwidth = map.get('ReservationBandwidth')
        self.reservation_internet_charge_type = map.get('ReservationInternetChargeType')
        self.reservation_active_time = map.get('ReservationActiveTime')
        self.reservation_order_type = map.get('ReservationOrderType')
        if map.get('BackendServers') is not None:
            temp_model = DescribeGlobalAccelerationInstancesResponseGlobalAccelerationInstancesGlobalAccelerationInstanceBackendServers()
            self.backend_servers = temp_model.from_map(map['BackendServers'])
        else:
            self.backend_servers = None
        if map.get('PublicIpAddresses') is not None:
            temp_model = DescribeGlobalAccelerationInstancesResponseGlobalAccelerationInstancesGlobalAccelerationInstancePublicIpAddresses()
            self.public_ip_addresses = temp_model.from_map(map['PublicIpAddresses'])
        else:
            self.public_ip_addresses = None
        return self


class DescribeGlobalAccelerationInstancesResponseGlobalAccelerationInstances(TeaModel):
    def __init__(self, global_acceleration_instance=None):
        self.global_acceleration_instance = global_acceleration_instance

    def validate(self):
        self.validate_required(self.global_acceleration_instance, 'global_acceleration_instance')
        if self.global_acceleration_instance:
            for k in self.global_acceleration_instance:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['GlobalAccelerationInstance'] = []
        if self.global_acceleration_instance is not None:
            for k in self.global_acceleration_instance:
                result['GlobalAccelerationInstance'].append(k.to_map() if k else None)
        else:
            result['GlobalAccelerationInstance'] = None
        return result

    def from_map(self, map={}):
        self.global_acceleration_instance = []
        if map.get('GlobalAccelerationInstance') is not None:
            for k in map.get('GlobalAccelerationInstance'):
                temp_model = DescribeGlobalAccelerationInstancesResponseGlobalAccelerationInstancesGlobalAccelerationInstance()
                self.global_acceleration_instance.append(temp_model.from_map(k))
        else:
            self.global_acceleration_instance = None
        return self


class DeleteGlobalAccelerationInstanceRequest(TeaModel):
    def __init__(self, region_id=None, global_acceleration_instance_id=None):
        self.region_id = region_id
        self.global_acceleration_instance_id = global_acceleration_instance_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.global_acceleration_instance_id, 'global_acceleration_instance_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['GlobalAccelerationInstanceId'] = self.global_acceleration_instance_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.global_acceleration_instance_id = map.get('GlobalAccelerationInstanceId')
        return self


class DeleteGlobalAccelerationInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateGlobalAccelerationInstanceRequest(TeaModel):
    def __init__(self, region_id=None, service_location=None, bandwidth=None, bandwidth_type=None, name=None,
                 description=None, client_token=None):
        self.region_id = region_id
        self.service_location = service_location
        self.bandwidth = bandwidth
        self.bandwidth_type = bandwidth_type
        self.name = name
        self.description = description
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.service_location, 'service_location')
        self.validate_required(self.bandwidth, 'bandwidth')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ServiceLocation'] = self.service_location
        result['Bandwidth'] = self.bandwidth
        result['BandwidthType'] = self.bandwidth_type
        result['Name'] = self.name
        result['Description'] = self.description
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.service_location = map.get('ServiceLocation')
        self.bandwidth = map.get('Bandwidth')
        self.bandwidth_type = map.get('BandwidthType')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.client_token = map.get('ClientToken')
        return self


class CreateGlobalAccelerationInstanceResponse(TeaModel):
    def __init__(self, request_id=None, global_acceleration_instance_id=None, ip_address=None):
        self.request_id = request_id
        self.global_acceleration_instance_id = global_acceleration_instance_id
        self.ip_address = ip_address

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.global_acceleration_instance_id, 'global_acceleration_instance_id')
        self.validate_required(self.ip_address, 'ip_address')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['GlobalAccelerationInstanceId'] = self.global_acceleration_instance_id
        result['IpAddress'] = self.ip_address
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.global_acceleration_instance_id = map.get('GlobalAccelerationInstanceId')
        self.ip_address = map.get('IpAddress')
        return self


class AssociateGlobalAccelerationInstanceRequest(TeaModel):
    def __init__(self, region_id=None, global_acceleration_instance_id=None, backend_server_id=None,
                 backend_server_region_id=None, backend_server_type=None):
        self.region_id = region_id
        self.global_acceleration_instance_id = global_acceleration_instance_id
        self.backend_server_id = backend_server_id
        self.backend_server_region_id = backend_server_region_id
        self.backend_server_type = backend_server_type

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.global_acceleration_instance_id, 'global_acceleration_instance_id')
        self.validate_required(self.backend_server_id, 'backend_server_id')
        self.validate_required(self.backend_server_region_id, 'backend_server_region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['GlobalAccelerationInstanceId'] = self.global_acceleration_instance_id
        result['BackendServerId'] = self.backend_server_id
        result['BackendServerRegionId'] = self.backend_server_region_id
        result['BackendServerType'] = self.backend_server_type
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.global_acceleration_instance_id = map.get('GlobalAccelerationInstanceId')
        self.backend_server_id = map.get('BackendServerId')
        self.backend_server_region_id = map.get('BackendServerRegionId')
        self.backend_server_type = map.get('BackendServerType')
        return self


class AssociateGlobalAccelerationInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeVSwitchAttributesRequest(TeaModel):
    def __init__(self, v_switch_id=None, region_id=None, dry_run=None):
        self.v_switch_id = v_switch_id
        self.region_id = region_id
        self.dry_run = dry_run

    def validate(self):
        self.validate_required(self.v_switch_id, 'v_switch_id')

    def to_map(self):
        result = {}
        result['VSwitchId'] = self.v_switch_id
        result['RegionId'] = self.region_id
        result['DryRun'] = self.dry_run
        return result

    def from_map(self, map={}):
        self.v_switch_id = map.get('VSwitchId')
        self.region_id = map.get('RegionId')
        self.dry_run = map.get('DryRun')
        return self


class DescribeVSwitchAttributesResponse(TeaModel):
    def __init__(self, request_id=None, v_switch_id=None, vpc_id=None, status=None, cidr_block=None,
                 ipv_6cidr_block=None, zone_id=None, available_ip_address_count=None, description=None, v_switch_name=None,
                 creation_time=None, is_default=None, resource_group_id=None, network_acl_id=None, owner_id=None, share_type=None,
                 route_table=None):
        self.request_id = request_id
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.status = status
        self.cidr_block = cidr_block
        self.ipv_6cidr_block = ipv_6cidr_block
        self.zone_id = zone_id
        self.available_ip_address_count = available_ip_address_count
        self.description = description
        self.v_switch_name = v_switch_name
        self.creation_time = creation_time
        self.is_default = is_default
        self.resource_group_id = resource_group_id
        self.network_acl_id = network_acl_id
        self.owner_id = owner_id
        self.share_type = share_type
        self.route_table = route_table  # type: DescribeVSwitchAttributesResponseRouteTable

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.v_switch_id, 'v_switch_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.cidr_block, 'cidr_block')
        self.validate_required(self.ipv_6cidr_block, 'ipv_6cidr_block')
        self.validate_required(self.zone_id, 'zone_id')
        self.validate_required(self.available_ip_address_count, 'available_ip_address_count')
        self.validate_required(self.description, 'description')
        self.validate_required(self.v_switch_name, 'v_switch_name')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.is_default, 'is_default')
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.network_acl_id, 'network_acl_id')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.share_type, 'share_type')
        self.validate_required(self.route_table, 'route_table')
        if self.route_table:
            self.route_table.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['VSwitchId'] = self.v_switch_id
        result['VpcId'] = self.vpc_id
        result['Status'] = self.status
        result['CidrBlock'] = self.cidr_block
        result['Ipv6CidrBlock'] = self.ipv_6cidr_block
        result['ZoneId'] = self.zone_id
        result['AvailableIpAddressCount'] = self.available_ip_address_count
        result['Description'] = self.description
        result['VSwitchName'] = self.v_switch_name
        result['CreationTime'] = self.creation_time
        result['IsDefault'] = self.is_default
        result['ResourceGroupId'] = self.resource_group_id
        result['NetworkAclId'] = self.network_acl_id
        result['OwnerId'] = self.owner_id
        result['ShareType'] = self.share_type
        if self.route_table is not None:
            result['RouteTable'] = self.route_table.to_map()
        else:
            result['RouteTable'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.v_switch_id = map.get('VSwitchId')
        self.vpc_id = map.get('VpcId')
        self.status = map.get('Status')
        self.cidr_block = map.get('CidrBlock')
        self.ipv_6cidr_block = map.get('Ipv6CidrBlock')
        self.zone_id = map.get('ZoneId')
        self.available_ip_address_count = map.get('AvailableIpAddressCount')
        self.description = map.get('Description')
        self.v_switch_name = map.get('VSwitchName')
        self.creation_time = map.get('CreationTime')
        self.is_default = map.get('IsDefault')
        self.resource_group_id = map.get('ResourceGroupId')
        self.network_acl_id = map.get('NetworkAclId')
        self.owner_id = map.get('OwnerId')
        self.share_type = map.get('ShareType')
        if map.get('RouteTable') is not None:
            temp_model = DescribeVSwitchAttributesResponseRouteTable()
            self.route_table = temp_model.from_map(map['RouteTable'])
        else:
            self.route_table = None
        return self


class DescribeVSwitchAttributesResponseRouteTable(TeaModel):
    def __init__(self, route_table_id=None, route_table_type=None):
        self.route_table_id = route_table_id
        self.route_table_type = route_table_type

    def validate(self):
        self.validate_required(self.route_table_id, 'route_table_id')
        self.validate_required(self.route_table_type, 'route_table_type')

    def to_map(self):
        result = {}
        result['RouteTableId'] = self.route_table_id
        result['RouteTableType'] = self.route_table_type
        return result

    def from_map(self, map={}):
        self.route_table_id = map.get('RouteTableId')
        self.route_table_type = map.get('RouteTableType')
        return self


class RemoveCommonBandwidthPackageIpRequest(TeaModel):
    def __init__(self, region_id=None, bandwidth_package_id=None, ip_instance_id=None):
        self.region_id = region_id
        self.bandwidth_package_id = bandwidth_package_id
        self.ip_instance_id = ip_instance_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bandwidth_package_id, 'bandwidth_package_id')
        self.validate_required(self.ip_instance_id, 'ip_instance_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['BandwidthPackageId'] = self.bandwidth_package_id
        result['IpInstanceId'] = self.ip_instance_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        self.ip_instance_id = map.get('IpInstanceId')
        return self


class RemoveCommonBandwidthPackageIpResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyCommonBandwidthPackageSpecRequest(TeaModel):
    def __init__(self, region_id=None, bandwidth_package_id=None, bandwidth=None):
        self.region_id = region_id
        self.bandwidth_package_id = bandwidth_package_id
        self.bandwidth = bandwidth

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bandwidth_package_id, 'bandwidth_package_id')
        self.validate_required(self.bandwidth, 'bandwidth')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['BandwidthPackageId'] = self.bandwidth_package_id
        result['Bandwidth'] = self.bandwidth
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        self.bandwidth = map.get('Bandwidth')
        return self


class ModifyCommonBandwidthPackageSpecResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyCommonBandwidthPackageAttributeRequest(TeaModel):
    def __init__(self, region_id=None, bandwidth_package_id=None, name=None, description=None):
        self.region_id = region_id
        self.bandwidth_package_id = bandwidth_package_id
        self.name = name
        self.description = description

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bandwidth_package_id, 'bandwidth_package_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['BandwidthPackageId'] = self.bandwidth_package_id
        result['Name'] = self.name
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        return self


class ModifyCommonBandwidthPackageAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeCommonBandwidthPackagesRequest(TeaModel):
    def __init__(self, include_reservation_data=None, region_id=None, bandwidth_package_id=None,
                 resource_group_id=None, name=None, page_number=None, page_size=None, dry_run=None):
        self.include_reservation_data = include_reservation_data
        self.region_id = region_id
        self.bandwidth_package_id = bandwidth_package_id
        self.resource_group_id = resource_group_id
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.dry_run = dry_run

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['IncludeReservationData'] = self.include_reservation_data
        result['RegionId'] = self.region_id
        result['BandwidthPackageId'] = self.bandwidth_package_id
        result['ResourceGroupId'] = self.resource_group_id
        result['Name'] = self.name
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['DryRun'] = self.dry_run
        return result

    def from_map(self, map={}):
        self.include_reservation_data = map.get('IncludeReservationData')
        self.region_id = map.get('RegionId')
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        self.resource_group_id = map.get('ResourceGroupId')
        self.name = map.get('Name')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.dry_run = map.get('DryRun')
        return self


class DescribeCommonBandwidthPackagesResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None,
                 common_bandwidth_packages=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.common_bandwidth_packages = common_bandwidth_packages  # type: DescribeCommonBandwidthPackagesResponseCommonBandwidthPackages

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.common_bandwidth_packages, 'common_bandwidth_packages')
        if self.common_bandwidth_packages:
            self.common_bandwidth_packages.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.common_bandwidth_packages is not None:
            result['CommonBandwidthPackages'] = self.common_bandwidth_packages.to_map()
        else:
            result['CommonBandwidthPackages'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('CommonBandwidthPackages') is not None:
            temp_model = DescribeCommonBandwidthPackagesResponseCommonBandwidthPackages()
            self.common_bandwidth_packages = temp_model.from_map(map['CommonBandwidthPackages'])
        else:
            self.common_bandwidth_packages = None
        return self


class DescribeCommonBandwidthPackagesResponseCommonBandwidthPackagesCommonBandwidthPackagePublicIpAddressesPublicIpAddresse(TeaModel):
    def __init__(self, allocation_id=None, ip_address=None):
        self.allocation_id = allocation_id
        self.ip_address = ip_address

    def validate(self):
        self.validate_required(self.allocation_id, 'allocation_id')
        self.validate_required(self.ip_address, 'ip_address')

    def to_map(self):
        result = {}
        result['AllocationId'] = self.allocation_id
        result['IpAddress'] = self.ip_address
        return result

    def from_map(self, map={}):
        self.allocation_id = map.get('AllocationId')
        self.ip_address = map.get('IpAddress')
        return self


class DescribeCommonBandwidthPackagesResponseCommonBandwidthPackagesCommonBandwidthPackagePublicIpAddresses(TeaModel):
    def __init__(self, public_ip_addresse=None):
        self.public_ip_addresse = public_ip_addresse

    def validate(self):
        self.validate_required(self.public_ip_addresse, 'public_ip_addresse')
        if self.public_ip_addresse:
            for k in self.public_ip_addresse:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PublicIpAddresse'] = []
        if self.public_ip_addresse is not None:
            for k in self.public_ip_addresse:
                result['PublicIpAddresse'].append(k.to_map() if k else None)
        else:
            result['PublicIpAddresse'] = None
        return result

    def from_map(self, map={}):
        self.public_ip_addresse = []
        if map.get('PublicIpAddresse') is not None:
            for k in map.get('PublicIpAddresse'):
                temp_model = DescribeCommonBandwidthPackagesResponseCommonBandwidthPackagesCommonBandwidthPackagePublicIpAddressesPublicIpAddresse()
                self.public_ip_addresse.append(temp_model.from_map(k))
        else:
            self.public_ip_addresse = None
        return self


class DescribeCommonBandwidthPackagesResponseCommonBandwidthPackagesCommonBandwidthPackage(TeaModel):
    def __init__(self, bandwidth_package_id=None, region_id=None, name=None, description=None, bandwidth=None,
                 instance_charge_type=None, internet_charge_type=None, business_status=None, creation_time=None, expired_time=None,
                 status=None, ratio=None, resource_group_id=None, has_reservation_data=None, reservation_bandwidth=None,
                 reservation_internet_charge_type=None, reservation_active_time=None, reservation_order_type=None, isp=None,
                 deletion_protection=None, public_ip_addresses=None):
        self.bandwidth_package_id = bandwidth_package_id
        self.region_id = region_id
        self.name = name
        self.description = description
        self.bandwidth = bandwidth
        self.instance_charge_type = instance_charge_type
        self.internet_charge_type = internet_charge_type
        self.business_status = business_status
        self.creation_time = creation_time
        self.expired_time = expired_time
        self.status = status
        self.ratio = ratio
        self.resource_group_id = resource_group_id
        self.has_reservation_data = has_reservation_data
        self.reservation_bandwidth = reservation_bandwidth
        self.reservation_internet_charge_type = reservation_internet_charge_type
        self.reservation_active_time = reservation_active_time
        self.reservation_order_type = reservation_order_type
        self.isp = isp
        self.deletion_protection = deletion_protection
        self.public_ip_addresses = public_ip_addresses  # type: DescribeCommonBandwidthPackagesResponseCommonBandwidthPackagesCommonBandwidthPackagePublicIpAddresses

    def validate(self):
        self.validate_required(self.bandwidth_package_id, 'bandwidth_package_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.bandwidth, 'bandwidth')
        self.validate_required(self.instance_charge_type, 'instance_charge_type')
        self.validate_required(self.internet_charge_type, 'internet_charge_type')
        self.validate_required(self.business_status, 'business_status')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.expired_time, 'expired_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.ratio, 'ratio')
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.has_reservation_data, 'has_reservation_data')
        self.validate_required(self.reservation_bandwidth, 'reservation_bandwidth')
        self.validate_required(self.reservation_internet_charge_type, 'reservation_internet_charge_type')
        self.validate_required(self.reservation_active_time, 'reservation_active_time')
        self.validate_required(self.reservation_order_type, 'reservation_order_type')
        self.validate_required(self.isp, 'isp')
        self.validate_required(self.deletion_protection, 'deletion_protection')
        self.validate_required(self.public_ip_addresses, 'public_ip_addresses')
        if self.public_ip_addresses:
            self.public_ip_addresses.validate()

    def to_map(self):
        result = {}
        result['BandwidthPackageId'] = self.bandwidth_package_id
        result['RegionId'] = self.region_id
        result['Name'] = self.name
        result['Description'] = self.description
        result['Bandwidth'] = self.bandwidth
        result['InstanceChargeType'] = self.instance_charge_type
        result['InternetChargeType'] = self.internet_charge_type
        result['BusinessStatus'] = self.business_status
        result['CreationTime'] = self.creation_time
        result['ExpiredTime'] = self.expired_time
        result['Status'] = self.status
        result['Ratio'] = self.ratio
        result['ResourceGroupId'] = self.resource_group_id
        result['HasReservationData'] = self.has_reservation_data
        result['ReservationBandwidth'] = self.reservation_bandwidth
        result['ReservationInternetChargeType'] = self.reservation_internet_charge_type
        result['ReservationActiveTime'] = self.reservation_active_time
        result['ReservationOrderType'] = self.reservation_order_type
        result['ISP'] = self.isp
        result['DeletionProtection'] = self.deletion_protection
        if self.public_ip_addresses is not None:
            result['PublicIpAddresses'] = self.public_ip_addresses.to_map()
        else:
            result['PublicIpAddresses'] = None
        return result

    def from_map(self, map={}):
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        self.region_id = map.get('RegionId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.bandwidth = map.get('Bandwidth')
        self.instance_charge_type = map.get('InstanceChargeType')
        self.internet_charge_type = map.get('InternetChargeType')
        self.business_status = map.get('BusinessStatus')
        self.creation_time = map.get('CreationTime')
        self.expired_time = map.get('ExpiredTime')
        self.status = map.get('Status')
        self.ratio = map.get('Ratio')
        self.resource_group_id = map.get('ResourceGroupId')
        self.has_reservation_data = map.get('HasReservationData')
        self.reservation_bandwidth = map.get('ReservationBandwidth')
        self.reservation_internet_charge_type = map.get('ReservationInternetChargeType')
        self.reservation_active_time = map.get('ReservationActiveTime')
        self.reservation_order_type = map.get('ReservationOrderType')
        self.isp = map.get('ISP')
        self.deletion_protection = map.get('DeletionProtection')
        if map.get('PublicIpAddresses') is not None:
            temp_model = DescribeCommonBandwidthPackagesResponseCommonBandwidthPackagesCommonBandwidthPackagePublicIpAddresses()
            self.public_ip_addresses = temp_model.from_map(map['PublicIpAddresses'])
        else:
            self.public_ip_addresses = None
        return self


class DescribeCommonBandwidthPackagesResponseCommonBandwidthPackages(TeaModel):
    def __init__(self, common_bandwidth_package=None):
        self.common_bandwidth_package = common_bandwidth_package

    def validate(self):
        self.validate_required(self.common_bandwidth_package, 'common_bandwidth_package')
        if self.common_bandwidth_package:
            for k in self.common_bandwidth_package:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['CommonBandwidthPackage'] = []
        if self.common_bandwidth_package is not None:
            for k in self.common_bandwidth_package:
                result['CommonBandwidthPackage'].append(k.to_map() if k else None)
        else:
            result['CommonBandwidthPackage'] = None
        return result

    def from_map(self, map={}):
        self.common_bandwidth_package = []
        if map.get('CommonBandwidthPackage') is not None:
            for k in map.get('CommonBandwidthPackage'):
                temp_model = DescribeCommonBandwidthPackagesResponseCommonBandwidthPackagesCommonBandwidthPackage()
                self.common_bandwidth_package.append(temp_model.from_map(k))
        else:
            self.common_bandwidth_package = None
        return self


class DeleteCommonBandwidthPackageRequest(TeaModel):
    def __init__(self, region_id=None, force=None, bandwidth_package_id=None):
        self.region_id = region_id
        self.force = force
        self.bandwidth_package_id = bandwidth_package_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bandwidth_package_id, 'bandwidth_package_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Force'] = self.force
        result['BandwidthPackageId'] = self.bandwidth_package_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.force = map.get('Force')
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        return self


class DeleteCommonBandwidthPackageResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateCommonBandwidthPackageRequest(TeaModel):
    def __init__(self, region_id=None, zone=None, isp=None, name=None, description=None, client_token=None,
                 resource_group_id=None, bandwidth=None, ratio=None, internet_charge_type=None):
        self.region_id = region_id
        self.zone = zone
        self.isp = isp
        self.name = name
        self.description = description
        self.client_token = client_token
        self.resource_group_id = resource_group_id
        self.bandwidth = bandwidth
        self.ratio = ratio
        self.internet_charge_type = internet_charge_type

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bandwidth, 'bandwidth')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Zone'] = self.zone
        result['ISP'] = self.isp
        result['Name'] = self.name
        result['Description'] = self.description
        result['ClientToken'] = self.client_token
        result['ResourceGroupId'] = self.resource_group_id
        result['Bandwidth'] = self.bandwidth
        result['Ratio'] = self.ratio
        result['InternetChargeType'] = self.internet_charge_type
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.zone = map.get('Zone')
        self.isp = map.get('ISP')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.client_token = map.get('ClientToken')
        self.resource_group_id = map.get('ResourceGroupId')
        self.bandwidth = map.get('Bandwidth')
        self.ratio = map.get('Ratio')
        self.internet_charge_type = map.get('InternetChargeType')
        return self


class CreateCommonBandwidthPackageResponse(TeaModel):
    def __init__(self, request_id=None, bandwidth_package_id=None, resource_group_id=None):
        self.request_id = request_id
        self.bandwidth_package_id = bandwidth_package_id
        self.resource_group_id = resource_group_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.bandwidth_package_id, 'bandwidth_package_id')
        self.validate_required(self.resource_group_id, 'resource_group_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['BandwidthPackageId'] = self.bandwidth_package_id
        result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        self.resource_group_id = map.get('ResourceGroupId')
        return self


class AddCommonBandwidthPackageIpRequest(TeaModel):
    def __init__(self, region_id=None, bandwidth_package_id=None, ip_instance_id=None, ip_type=None):
        self.region_id = region_id
        self.bandwidth_package_id = bandwidth_package_id
        self.ip_instance_id = ip_instance_id
        self.ip_type = ip_type

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bandwidth_package_id, 'bandwidth_package_id')
        self.validate_required(self.ip_instance_id, 'ip_instance_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['BandwidthPackageId'] = self.bandwidth_package_id
        result['IpInstanceId'] = self.ip_instance_id
        result['IpType'] = self.ip_type
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        self.ip_instance_id = map.get('IpInstanceId')
        self.ip_type = map.get('IpType')
        return self


class AddCommonBandwidthPackageIpResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyVpnGatewayAttributeRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, vpn_gateway_id=None, name=None, description=None,
                 auto_propagate=None):
        self.region_id = region_id
        self.client_token = client_token
        self.vpn_gateway_id = vpn_gateway_id
        self.name = name
        self.description = description
        self.auto_propagate = auto_propagate

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['Name'] = self.name
        result['Description'] = self.description
        result['AutoPropagate'] = self.auto_propagate
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.auto_propagate = map.get('AutoPropagate')
        return self


class ModifyVpnGatewayAttributeResponse(TeaModel):
    def __init__(self, request_id=None, vpn_gateway_id=None, vpc_id=None, v_switch_id=None, internet_ip=None,
                 intranet_ip=None, create_time=None, end_time=None, spec=None, name=None, description=None, status=None,
                 business_status=None, enable_bgp=None, auto_propagate=None):
        self.request_id = request_id
        self.vpn_gateway_id = vpn_gateway_id
        self.vpc_id = vpc_id
        self.v_switch_id = v_switch_id
        self.internet_ip = internet_ip
        self.intranet_ip = intranet_ip
        self.create_time = create_time
        self.end_time = end_time
        self.spec = spec
        self.name = name
        self.description = description
        self.status = status
        self.business_status = business_status
        self.enable_bgp = enable_bgp
        self.auto_propagate = auto_propagate

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.v_switch_id, 'v_switch_id')
        self.validate_required(self.internet_ip, 'internet_ip')
        self.validate_required(self.intranet_ip, 'intranet_ip')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.spec, 'spec')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.status, 'status')
        self.validate_required(self.business_status, 'business_status')
        self.validate_required(self.enable_bgp, 'enable_bgp')
        self.validate_required(self.auto_propagate, 'auto_propagate')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['VpcId'] = self.vpc_id
        result['VSwitchId'] = self.v_switch_id
        result['InternetIp'] = self.internet_ip
        result['IntranetIp'] = self.intranet_ip
        result['CreateTime'] = self.create_time
        result['EndTime'] = self.end_time
        result['Spec'] = self.spec
        result['Name'] = self.name
        result['Description'] = self.description
        result['Status'] = self.status
        result['BusinessStatus'] = self.business_status
        result['EnableBgp'] = self.enable_bgp
        result['AutoPropagate'] = self.auto_propagate
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.vpc_id = map.get('VpcId')
        self.v_switch_id = map.get('VSwitchId')
        self.internet_ip = map.get('InternetIp')
        self.intranet_ip = map.get('IntranetIp')
        self.create_time = map.get('CreateTime')
        self.end_time = map.get('EndTime')
        self.spec = map.get('Spec')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.status = map.get('Status')
        self.business_status = map.get('BusinessStatus')
        self.enable_bgp = map.get('EnableBgp')
        self.auto_propagate = map.get('AutoPropagate')
        return self


class ModifyVpnConnectionAttributeRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, vpn_connection_id=None, name=None, local_subnet=None,
                 remote_subnet=None, effect_immediately=None, ike_config=None, ipsec_config=None, health_check_config=None,
                 auto_config_route=None, enable_dpd=None, enable_nat_traversal=None, bgp_config=None):
        self.region_id = region_id
        self.client_token = client_token
        self.vpn_connection_id = vpn_connection_id
        self.name = name
        self.local_subnet = local_subnet
        self.remote_subnet = remote_subnet
        self.effect_immediately = effect_immediately
        self.ike_config = ike_config
        self.ipsec_config = ipsec_config
        self.health_check_config = health_check_config
        self.auto_config_route = auto_config_route
        self.enable_dpd = enable_dpd
        self.enable_nat_traversal = enable_nat_traversal
        self.bgp_config = bgp_config

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpn_connection_id, 'vpn_connection_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['VpnConnectionId'] = self.vpn_connection_id
        result['Name'] = self.name
        result['LocalSubnet'] = self.local_subnet
        result['RemoteSubnet'] = self.remote_subnet
        result['EffectImmediately'] = self.effect_immediately
        result['IkeConfig'] = self.ike_config
        result['IpsecConfig'] = self.ipsec_config
        result['HealthCheckConfig'] = self.health_check_config
        result['AutoConfigRoute'] = self.auto_config_route
        result['EnableDpd'] = self.enable_dpd
        result['EnableNatTraversal'] = self.enable_nat_traversal
        result['BgpConfig'] = self.bgp_config
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.vpn_connection_id = map.get('VpnConnectionId')
        self.name = map.get('Name')
        self.local_subnet = map.get('LocalSubnet')
        self.remote_subnet = map.get('RemoteSubnet')
        self.effect_immediately = map.get('EffectImmediately')
        self.ike_config = map.get('IkeConfig')
        self.ipsec_config = map.get('IpsecConfig')
        self.health_check_config = map.get('HealthCheckConfig')
        self.auto_config_route = map.get('AutoConfigRoute')
        self.enable_dpd = map.get('EnableDpd')
        self.enable_nat_traversal = map.get('EnableNatTraversal')
        self.bgp_config = map.get('BgpConfig')
        return self


class ModifyVpnConnectionAttributeResponse(TeaModel):
    def __init__(self, request_id=None, vpn_connection_id=None, customer_gateway_id=None, vpn_gateway_id=None,
                 name=None, description=None, local_subnet=None, remote_subnet=None, create_time=None,
                 effect_immediately=None, enable_dpd=None, enable_nat_traversal=None, ike_config=None, ipsec_config=None,
                 vco_health_check=None, vpn_bgp_config=None):
        self.request_id = request_id
        self.vpn_connection_id = vpn_connection_id
        self.customer_gateway_id = customer_gateway_id
        self.vpn_gateway_id = vpn_gateway_id
        self.name = name
        self.description = description
        self.local_subnet = local_subnet
        self.remote_subnet = remote_subnet
        self.create_time = create_time
        self.effect_immediately = effect_immediately
        self.enable_dpd = enable_dpd
        self.enable_nat_traversal = enable_nat_traversal
        self.ike_config = ike_config  # type: ModifyVpnConnectionAttributeResponseIkeConfig
        self.ipsec_config = ipsec_config  # type: ModifyVpnConnectionAttributeResponseIpsecConfig
        self.vco_health_check = vco_health_check  # type: ModifyVpnConnectionAttributeResponseVcoHealthCheck
        self.vpn_bgp_config = vpn_bgp_config  # type: ModifyVpnConnectionAttributeResponseVpnBgpConfig

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.vpn_connection_id, 'vpn_connection_id')
        self.validate_required(self.customer_gateway_id, 'customer_gateway_id')
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.local_subnet, 'local_subnet')
        self.validate_required(self.remote_subnet, 'remote_subnet')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.effect_immediately, 'effect_immediately')
        self.validate_required(self.enable_dpd, 'enable_dpd')
        self.validate_required(self.enable_nat_traversal, 'enable_nat_traversal')
        self.validate_required(self.ike_config, 'ike_config')
        if self.ike_config:
            self.ike_config.validate()
        self.validate_required(self.ipsec_config, 'ipsec_config')
        if self.ipsec_config:
            self.ipsec_config.validate()
        self.validate_required(self.vco_health_check, 'vco_health_check')
        if self.vco_health_check:
            self.vco_health_check.validate()
        self.validate_required(self.vpn_bgp_config, 'vpn_bgp_config')
        if self.vpn_bgp_config:
            self.vpn_bgp_config.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['VpnConnectionId'] = self.vpn_connection_id
        result['CustomerGatewayId'] = self.customer_gateway_id
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['Name'] = self.name
        result['Description'] = self.description
        result['LocalSubnet'] = self.local_subnet
        result['RemoteSubnet'] = self.remote_subnet
        result['CreateTime'] = self.create_time
        result['EffectImmediately'] = self.effect_immediately
        result['EnableDpd'] = self.enable_dpd
        result['EnableNatTraversal'] = self.enable_nat_traversal
        if self.ike_config is not None:
            result['IkeConfig'] = self.ike_config.to_map()
        else:
            result['IkeConfig'] = None
        if self.ipsec_config is not None:
            result['IpsecConfig'] = self.ipsec_config.to_map()
        else:
            result['IpsecConfig'] = None
        if self.vco_health_check is not None:
            result['VcoHealthCheck'] = self.vco_health_check.to_map()
        else:
            result['VcoHealthCheck'] = None
        if self.vpn_bgp_config is not None:
            result['VpnBgpConfig'] = self.vpn_bgp_config.to_map()
        else:
            result['VpnBgpConfig'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.vpn_connection_id = map.get('VpnConnectionId')
        self.customer_gateway_id = map.get('CustomerGatewayId')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.local_subnet = map.get('LocalSubnet')
        self.remote_subnet = map.get('RemoteSubnet')
        self.create_time = map.get('CreateTime')
        self.effect_immediately = map.get('EffectImmediately')
        self.enable_dpd = map.get('EnableDpd')
        self.enable_nat_traversal = map.get('EnableNatTraversal')
        if map.get('IkeConfig') is not None:
            temp_model = ModifyVpnConnectionAttributeResponseIkeConfig()
            self.ike_config = temp_model.from_map(map['IkeConfig'])
        else:
            self.ike_config = None
        if map.get('IpsecConfig') is not None:
            temp_model = ModifyVpnConnectionAttributeResponseIpsecConfig()
            self.ipsec_config = temp_model.from_map(map['IpsecConfig'])
        else:
            self.ipsec_config = None
        if map.get('VcoHealthCheck') is not None:
            temp_model = ModifyVpnConnectionAttributeResponseVcoHealthCheck()
            self.vco_health_check = temp_model.from_map(map['VcoHealthCheck'])
        else:
            self.vco_health_check = None
        if map.get('VpnBgpConfig') is not None:
            temp_model = ModifyVpnConnectionAttributeResponseVpnBgpConfig()
            self.vpn_bgp_config = temp_model.from_map(map['VpnBgpConfig'])
        else:
            self.vpn_bgp_config = None
        return self


class ModifyVpnConnectionAttributeResponseIkeConfig(TeaModel):
    def __init__(self, psk=None, ike_version=None, ike_mode=None, ike_enc_alg=None, ike_auth_alg=None, ike_pfs=None,
                 ike_lifetime=None, local_id=None, remote_id=None):
        self.psk = psk
        self.ike_version = ike_version
        self.ike_mode = ike_mode
        self.ike_enc_alg = ike_enc_alg
        self.ike_auth_alg = ike_auth_alg
        self.ike_pfs = ike_pfs
        self.ike_lifetime = ike_lifetime
        self.local_id = local_id
        self.remote_id = remote_id

    def validate(self):
        self.validate_required(self.psk, 'psk')
        self.validate_required(self.ike_version, 'ike_version')
        self.validate_required(self.ike_mode, 'ike_mode')
        self.validate_required(self.ike_enc_alg, 'ike_enc_alg')
        self.validate_required(self.ike_auth_alg, 'ike_auth_alg')
        self.validate_required(self.ike_pfs, 'ike_pfs')
        self.validate_required(self.ike_lifetime, 'ike_lifetime')
        self.validate_required(self.local_id, 'local_id')
        self.validate_required(self.remote_id, 'remote_id')

    def to_map(self):
        result = {}
        result['Psk'] = self.psk
        result['IkeVersion'] = self.ike_version
        result['IkeMode'] = self.ike_mode
        result['IkeEncAlg'] = self.ike_enc_alg
        result['IkeAuthAlg'] = self.ike_auth_alg
        result['IkePfs'] = self.ike_pfs
        result['IkeLifetime'] = self.ike_lifetime
        result['LocalId'] = self.local_id
        result['RemoteId'] = self.remote_id
        return result

    def from_map(self, map={}):
        self.psk = map.get('Psk')
        self.ike_version = map.get('IkeVersion')
        self.ike_mode = map.get('IkeMode')
        self.ike_enc_alg = map.get('IkeEncAlg')
        self.ike_auth_alg = map.get('IkeAuthAlg')
        self.ike_pfs = map.get('IkePfs')
        self.ike_lifetime = map.get('IkeLifetime')
        self.local_id = map.get('LocalId')
        self.remote_id = map.get('RemoteId')
        return self


class ModifyVpnConnectionAttributeResponseIpsecConfig(TeaModel):
    def __init__(self, ipsec_enc_alg=None, ipsec_auth_alg=None, ipsec_pfs=None, ipsec_lifetime=None):
        self.ipsec_enc_alg = ipsec_enc_alg
        self.ipsec_auth_alg = ipsec_auth_alg
        self.ipsec_pfs = ipsec_pfs
        self.ipsec_lifetime = ipsec_lifetime

    def validate(self):
        self.validate_required(self.ipsec_enc_alg, 'ipsec_enc_alg')
        self.validate_required(self.ipsec_auth_alg, 'ipsec_auth_alg')
        self.validate_required(self.ipsec_pfs, 'ipsec_pfs')
        self.validate_required(self.ipsec_lifetime, 'ipsec_lifetime')

    def to_map(self):
        result = {}
        result['IpsecEncAlg'] = self.ipsec_enc_alg
        result['IpsecAuthAlg'] = self.ipsec_auth_alg
        result['IpsecPfs'] = self.ipsec_pfs
        result['IpsecLifetime'] = self.ipsec_lifetime
        return result

    def from_map(self, map={}):
        self.ipsec_enc_alg = map.get('IpsecEncAlg')
        self.ipsec_auth_alg = map.get('IpsecAuthAlg')
        self.ipsec_pfs = map.get('IpsecPfs')
        self.ipsec_lifetime = map.get('IpsecLifetime')
        return self


class ModifyVpnConnectionAttributeResponseVcoHealthCheck(TeaModel):
    def __init__(self, enable=None, sip=None, dip=None, interval=None, retry=None):
        self.enable = enable
        self.sip = sip
        self.dip = dip
        self.interval = interval
        self.retry = retry

    def validate(self):
        self.validate_required(self.enable, 'enable')
        self.validate_required(self.sip, 'sip')
        self.validate_required(self.dip, 'dip')
        self.validate_required(self.interval, 'interval')
        self.validate_required(self.retry, 'retry')

    def to_map(self):
        result = {}
        result['Enable'] = self.enable
        result['Sip'] = self.sip
        result['Dip'] = self.dip
        result['Interval'] = self.interval
        result['Retry'] = self.retry
        return result

    def from_map(self, map={}):
        self.enable = map.get('Enable')
        self.sip = map.get('Sip')
        self.dip = map.get('Dip')
        self.interval = map.get('Interval')
        self.retry = map.get('Retry')
        return self


class ModifyVpnConnectionAttributeResponseVpnBgpConfig(TeaModel):
    def __init__(self, enable_bgp=None, tunnel_cidr=None, local_bgp_ip=None, peer_bgp_ip=None, local_asn=None,
                 peer_asn=None, status=None):
        self.enable_bgp = enable_bgp
        self.tunnel_cidr = tunnel_cidr
        self.local_bgp_ip = local_bgp_ip
        self.peer_bgp_ip = peer_bgp_ip
        self.local_asn = local_asn
        self.peer_asn = peer_asn
        self.status = status

    def validate(self):
        self.validate_required(self.enable_bgp, 'enable_bgp')
        self.validate_required(self.tunnel_cidr, 'tunnel_cidr')
        self.validate_required(self.local_bgp_ip, 'local_bgp_ip')
        self.validate_required(self.peer_bgp_ip, 'peer_bgp_ip')
        self.validate_required(self.local_asn, 'local_asn')
        self.validate_required(self.peer_asn, 'peer_asn')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['EnableBgp'] = self.enable_bgp
        result['TunnelCidr'] = self.tunnel_cidr
        result['LocalBgpIp'] = self.local_bgp_ip
        result['PeerBgpIp'] = self.peer_bgp_ip
        result['LocalAsn'] = self.local_asn
        result['PeerAsn'] = self.peer_asn
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.enable_bgp = map.get('EnableBgp')
        self.tunnel_cidr = map.get('TunnelCidr')
        self.local_bgp_ip = map.get('LocalBgpIp')
        self.peer_bgp_ip = map.get('PeerBgpIp')
        self.local_asn = map.get('LocalAsn')
        self.peer_asn = map.get('PeerAsn')
        self.status = map.get('Status')
        return self


class ModifyCustomerGatewayAttributeRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, customer_gateway_id=None, name=None, description=None):
        self.region_id = region_id
        self.client_token = client_token
        self.customer_gateway_id = customer_gateway_id
        self.name = name
        self.description = description

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.customer_gateway_id, 'customer_gateway_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['CustomerGatewayId'] = self.customer_gateway_id
        result['Name'] = self.name
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.customer_gateway_id = map.get('CustomerGatewayId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        return self


class ModifyCustomerGatewayAttributeResponse(TeaModel):
    def __init__(self, request_id=None, customer_gateway_id=None, ip_address=None, name=None, description=None,
                 create_time=None):
        self.request_id = request_id
        self.customer_gateway_id = customer_gateway_id
        self.ip_address = ip_address
        self.name = name
        self.description = description
        self.create_time = create_time

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.customer_gateway_id, 'customer_gateway_id')
        self.validate_required(self.ip_address, 'ip_address')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.create_time, 'create_time')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['CustomerGatewayId'] = self.customer_gateway_id
        result['IpAddress'] = self.ip_address
        result['Name'] = self.name
        result['Description'] = self.description
        result['CreateTime'] = self.create_time
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.customer_gateway_id = map.get('CustomerGatewayId')
        self.ip_address = map.get('IpAddress')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.create_time = map.get('CreateTime')
        return self


class DownloadVpnConnectionConfigRequest(TeaModel):
    def __init__(self, region_id=None, vpn_connection_id=None):
        self.region_id = region_id
        self.vpn_connection_id = vpn_connection_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpn_connection_id, 'vpn_connection_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VpnConnectionId'] = self.vpn_connection_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vpn_connection_id = map.get('VpnConnectionId')
        return self


class DownloadVpnConnectionConfigResponse(TeaModel):
    def __init__(self, request_id=None, vpn_connection_config=None):
        self.request_id = request_id
        self.vpn_connection_config = vpn_connection_config  # type: DownloadVpnConnectionConfigResponseVpnConnectionConfig

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.vpn_connection_config, 'vpn_connection_config')
        if self.vpn_connection_config:
            self.vpn_connection_config.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.vpn_connection_config is not None:
            result['VpnConnectionConfig'] = self.vpn_connection_config.to_map()
        else:
            result['VpnConnectionConfig'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('VpnConnectionConfig') is not None:
            temp_model = DownloadVpnConnectionConfigResponseVpnConnectionConfig()
            self.vpn_connection_config = temp_model.from_map(map['VpnConnectionConfig'])
        else:
            self.vpn_connection_config = None
        return self


class DownloadVpnConnectionConfigResponseVpnConnectionConfigIkeConfig(TeaModel):
    def __init__(self, psk=None, ike_version=None, ike_mode=None, ike_enc_alg=None, ike_auth_alg=None, ike_pfs=None,
                 ike_lifetime=None, local_id=None, remote_id=None):
        self.psk = psk
        self.ike_version = ike_version
        self.ike_mode = ike_mode
        self.ike_enc_alg = ike_enc_alg
        self.ike_auth_alg = ike_auth_alg
        self.ike_pfs = ike_pfs
        self.ike_lifetime = ike_lifetime
        self.local_id = local_id
        self.remote_id = remote_id

    def validate(self):
        self.validate_required(self.psk, 'psk')
        self.validate_required(self.ike_version, 'ike_version')
        self.validate_required(self.ike_mode, 'ike_mode')
        self.validate_required(self.ike_enc_alg, 'ike_enc_alg')
        self.validate_required(self.ike_auth_alg, 'ike_auth_alg')
        self.validate_required(self.ike_pfs, 'ike_pfs')
        self.validate_required(self.ike_lifetime, 'ike_lifetime')
        self.validate_required(self.local_id, 'local_id')
        self.validate_required(self.remote_id, 'remote_id')

    def to_map(self):
        result = {}
        result['Psk'] = self.psk
        result['IkeVersion'] = self.ike_version
        result['IkeMode'] = self.ike_mode
        result['IkeEncAlg'] = self.ike_enc_alg
        result['IkeAuthAlg'] = self.ike_auth_alg
        result['IkePfs'] = self.ike_pfs
        result['IkeLifetime'] = self.ike_lifetime
        result['LocalId'] = self.local_id
        result['RemoteId'] = self.remote_id
        return result

    def from_map(self, map={}):
        self.psk = map.get('Psk')
        self.ike_version = map.get('IkeVersion')
        self.ike_mode = map.get('IkeMode')
        self.ike_enc_alg = map.get('IkeEncAlg')
        self.ike_auth_alg = map.get('IkeAuthAlg')
        self.ike_pfs = map.get('IkePfs')
        self.ike_lifetime = map.get('IkeLifetime')
        self.local_id = map.get('LocalId')
        self.remote_id = map.get('RemoteId')
        return self


class DownloadVpnConnectionConfigResponseVpnConnectionConfigIpsecConfig(TeaModel):
    def __init__(self, ipsec_enc_alg=None, ipsec_auth_alg=None, ipsec_pfs=None, ipsec_lifetime=None):
        self.ipsec_enc_alg = ipsec_enc_alg
        self.ipsec_auth_alg = ipsec_auth_alg
        self.ipsec_pfs = ipsec_pfs
        self.ipsec_lifetime = ipsec_lifetime

    def validate(self):
        self.validate_required(self.ipsec_enc_alg, 'ipsec_enc_alg')
        self.validate_required(self.ipsec_auth_alg, 'ipsec_auth_alg')
        self.validate_required(self.ipsec_pfs, 'ipsec_pfs')
        self.validate_required(self.ipsec_lifetime, 'ipsec_lifetime')

    def to_map(self):
        result = {}
        result['IpsecEncAlg'] = self.ipsec_enc_alg
        result['IpsecAuthAlg'] = self.ipsec_auth_alg
        result['IpsecPfs'] = self.ipsec_pfs
        result['IpsecLifetime'] = self.ipsec_lifetime
        return result

    def from_map(self, map={}):
        self.ipsec_enc_alg = map.get('IpsecEncAlg')
        self.ipsec_auth_alg = map.get('IpsecAuthAlg')
        self.ipsec_pfs = map.get('IpsecPfs')
        self.ipsec_lifetime = map.get('IpsecLifetime')
        return self


class DownloadVpnConnectionConfigResponseVpnConnectionConfig(TeaModel):
    def __init__(self, local_subnet=None, remote_subnet=None, local=None, remote=None, ike_config=None,
                 ipsec_config=None):
        self.local_subnet = local_subnet
        self.remote_subnet = remote_subnet
        self.local = local
        self.remote = remote
        self.ike_config = ike_config  # type: DownloadVpnConnectionConfigResponseVpnConnectionConfigIkeConfig
        self.ipsec_config = ipsec_config  # type: DownloadVpnConnectionConfigResponseVpnConnectionConfigIpsecConfig

    def validate(self):
        self.validate_required(self.local_subnet, 'local_subnet')
        self.validate_required(self.remote_subnet, 'remote_subnet')
        self.validate_required(self.local, 'local')
        self.validate_required(self.remote, 'remote')
        self.validate_required(self.ike_config, 'ike_config')
        if self.ike_config:
            self.ike_config.validate()
        self.validate_required(self.ipsec_config, 'ipsec_config')
        if self.ipsec_config:
            self.ipsec_config.validate()

    def to_map(self):
        result = {}
        result['LocalSubnet'] = self.local_subnet
        result['RemoteSubnet'] = self.remote_subnet
        result['Local'] = self.local
        result['Remote'] = self.remote
        if self.ike_config is not None:
            result['IkeConfig'] = self.ike_config.to_map()
        else:
            result['IkeConfig'] = None
        if self.ipsec_config is not None:
            result['IpsecConfig'] = self.ipsec_config.to_map()
        else:
            result['IpsecConfig'] = None
        return result

    def from_map(self, map={}):
        self.local_subnet = map.get('LocalSubnet')
        self.remote_subnet = map.get('RemoteSubnet')
        self.local = map.get('Local')
        self.remote = map.get('Remote')
        if map.get('IkeConfig') is not None:
            temp_model = DownloadVpnConnectionConfigResponseVpnConnectionConfigIkeConfig()
            self.ike_config = temp_model.from_map(map['IkeConfig'])
        else:
            self.ike_config = None
        if map.get('IpsecConfig') is not None:
            temp_model = DownloadVpnConnectionConfigResponseVpnConnectionConfigIpsecConfig()
            self.ipsec_config = temp_model.from_map(map['IpsecConfig'])
        else:
            self.ipsec_config = None
        return self


class DescribeVpnGatewaysRequest(TeaModel):
    def __init__(self, region_id=None, vpc_id=None, vpn_gateway_id=None, status=None, business_status=None,
                 page_number=None, page_size=None, tag=None, include_reservation_data=None):
        self.region_id = region_id
        self.vpc_id = vpc_id
        self.vpn_gateway_id = vpn_gateway_id
        self.status = status
        self.business_status = business_status
        self.page_number = page_number
        self.page_size = page_size
        self.tag = tag
        self.include_reservation_data = include_reservation_data

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VpcId'] = self.vpc_id
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['Status'] = self.status
        result['BusinessStatus'] = self.business_status
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        result['IncludeReservationData'] = self.include_reservation_data
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vpc_id = map.get('VpcId')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.status = map.get('Status')
        self.business_status = map.get('BusinessStatus')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = DescribeVpnGatewaysRequestTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        self.include_reservation_data = map.get('IncludeReservationData')
        return self


class DescribeVpnGatewaysRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class DescribeVpnGatewaysResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, vpn_gateways=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.vpn_gateways = vpn_gateways  # type: DescribeVpnGatewaysResponseVpnGateways

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.vpn_gateways, 'vpn_gateways')
        if self.vpn_gateways:
            self.vpn_gateways.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.vpn_gateways is not None:
            result['VpnGateways'] = self.vpn_gateways.to_map()
        else:
            result['VpnGateways'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('VpnGateways') is not None:
            temp_model = DescribeVpnGatewaysResponseVpnGateways()
            self.vpn_gateways = temp_model.from_map(map['VpnGateways'])
        else:
            self.vpn_gateways = None
        return self


class DescribeVpnGatewaysResponseVpnGatewaysVpnGatewayTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class DescribeVpnGatewaysResponseVpnGatewaysVpnGatewayTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag

    def validate(self):
        self.validate_required(self.tag, 'tag')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        return result

    def from_map(self, map={}):
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = DescribeVpnGatewaysResponseVpnGatewaysVpnGatewayTagsTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        return self


class DescribeVpnGatewaysResponseVpnGatewaysVpnGatewayReservationData(TeaModel):
    def __init__(self, status=None, reservation_end_time=None, reservation_order_type=None, reservation_spec=None,
                 reservation_ipsec=None, reservation_ssl=None, reservation_max_connections=None):
        self.status = status
        self.reservation_end_time = reservation_end_time
        self.reservation_order_type = reservation_order_type
        self.reservation_spec = reservation_spec
        self.reservation_ipsec = reservation_ipsec
        self.reservation_ssl = reservation_ssl
        self.reservation_max_connections = reservation_max_connections

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.reservation_end_time, 'reservation_end_time')
        self.validate_required(self.reservation_order_type, 'reservation_order_type')
        self.validate_required(self.reservation_spec, 'reservation_spec')
        self.validate_required(self.reservation_ipsec, 'reservation_ipsec')
        self.validate_required(self.reservation_ssl, 'reservation_ssl')
        self.validate_required(self.reservation_max_connections, 'reservation_max_connections')

    def to_map(self):
        result = {}
        result['Status'] = self.status
        result['ReservationEndTime'] = self.reservation_end_time
        result['ReservationOrderType'] = self.reservation_order_type
        result['ReservationSpec'] = self.reservation_spec
        result['ReservationIpsec'] = self.reservation_ipsec
        result['ReservationSsl'] = self.reservation_ssl
        result['ReservationMaxConnections'] = self.reservation_max_connections
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        self.reservation_end_time = map.get('ReservationEndTime')
        self.reservation_order_type = map.get('ReservationOrderType')
        self.reservation_spec = map.get('ReservationSpec')
        self.reservation_ipsec = map.get('ReservationIpsec')
        self.reservation_ssl = map.get('ReservationSsl')
        self.reservation_max_connections = map.get('ReservationMaxConnections')
        return self


class DescribeVpnGatewaysResponseVpnGatewaysVpnGateway(TeaModel):
    def __init__(self, vpn_gateway_id=None, vpc_id=None, v_switch_id=None, internet_ip=None, create_time=None,
                 end_time=None, spec=None, name=None, description=None, status=None, business_status=None, charge_type=None,
                 ipsec_vpn=None, ssl_vpn=None, ssl_max_connections=None, tag=None, enable_bgp=None, auto_propagate=None,
                 tags=None, reservation_data=None):
        self.vpn_gateway_id = vpn_gateway_id
        self.vpc_id = vpc_id
        self.v_switch_id = v_switch_id
        self.internet_ip = internet_ip
        self.create_time = create_time
        self.end_time = end_time
        self.spec = spec
        self.name = name
        self.description = description
        self.status = status
        self.business_status = business_status
        self.charge_type = charge_type
        self.ipsec_vpn = ipsec_vpn
        self.ssl_vpn = ssl_vpn
        self.ssl_max_connections = ssl_max_connections
        self.tag = tag
        self.enable_bgp = enable_bgp
        self.auto_propagate = auto_propagate
        self.tags = tags  # type: DescribeVpnGatewaysResponseVpnGatewaysVpnGatewayTags
        self.reservation_data = reservation_data  # type: DescribeVpnGatewaysResponseVpnGatewaysVpnGatewayReservationData

    def validate(self):
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.v_switch_id, 'v_switch_id')
        self.validate_required(self.internet_ip, 'internet_ip')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.spec, 'spec')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.status, 'status')
        self.validate_required(self.business_status, 'business_status')
        self.validate_required(self.charge_type, 'charge_type')
        self.validate_required(self.ipsec_vpn, 'ipsec_vpn')
        self.validate_required(self.ssl_vpn, 'ssl_vpn')
        self.validate_required(self.ssl_max_connections, 'ssl_max_connections')
        self.validate_required(self.tag, 'tag')
        self.validate_required(self.enable_bgp, 'enable_bgp')
        self.validate_required(self.auto_propagate, 'auto_propagate')
        self.validate_required(self.tags, 'tags')
        if self.tags:
            self.tags.validate()
        self.validate_required(self.reservation_data, 'reservation_data')
        if self.reservation_data:
            self.reservation_data.validate()

    def to_map(self):
        result = {}
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['VpcId'] = self.vpc_id
        result['VSwitchId'] = self.v_switch_id
        result['InternetIp'] = self.internet_ip
        result['CreateTime'] = self.create_time
        result['EndTime'] = self.end_time
        result['Spec'] = self.spec
        result['Name'] = self.name
        result['Description'] = self.description
        result['Status'] = self.status
        result['BusinessStatus'] = self.business_status
        result['ChargeType'] = self.charge_type
        result['IpsecVpn'] = self.ipsec_vpn
        result['SslVpn'] = self.ssl_vpn
        result['SslMaxConnections'] = self.ssl_max_connections
        result['Tag'] = self.tag
        result['EnableBgp'] = self.enable_bgp
        result['AutoPropagate'] = self.auto_propagate
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        else:
            result['Tags'] = None
        if self.reservation_data is not None:
            result['ReservationData'] = self.reservation_data.to_map()
        else:
            result['ReservationData'] = None
        return result

    def from_map(self, map={}):
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.vpc_id = map.get('VpcId')
        self.v_switch_id = map.get('VSwitchId')
        self.internet_ip = map.get('InternetIp')
        self.create_time = map.get('CreateTime')
        self.end_time = map.get('EndTime')
        self.spec = map.get('Spec')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.status = map.get('Status')
        self.business_status = map.get('BusinessStatus')
        self.charge_type = map.get('ChargeType')
        self.ipsec_vpn = map.get('IpsecVpn')
        self.ssl_vpn = map.get('SslVpn')
        self.ssl_max_connections = map.get('SslMaxConnections')
        self.tag = map.get('Tag')
        self.enable_bgp = map.get('EnableBgp')
        self.auto_propagate = map.get('AutoPropagate')
        if map.get('Tags') is not None:
            temp_model = DescribeVpnGatewaysResponseVpnGatewaysVpnGatewayTags()
            self.tags = temp_model.from_map(map['Tags'])
        else:
            self.tags = None
        if map.get('ReservationData') is not None:
            temp_model = DescribeVpnGatewaysResponseVpnGatewaysVpnGatewayReservationData()
            self.reservation_data = temp_model.from_map(map['ReservationData'])
        else:
            self.reservation_data = None
        return self


class DescribeVpnGatewaysResponseVpnGateways(TeaModel):
    def __init__(self, vpn_gateway=None):
        self.vpn_gateway = vpn_gateway

    def validate(self):
        self.validate_required(self.vpn_gateway, 'vpn_gateway')
        if self.vpn_gateway:
            for k in self.vpn_gateway:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['VpnGateway'] = []
        if self.vpn_gateway is not None:
            for k in self.vpn_gateway:
                result['VpnGateway'].append(k.to_map() if k else None)
        else:
            result['VpnGateway'] = None
        return result

    def from_map(self, map={}):
        self.vpn_gateway = []
        if map.get('VpnGateway') is not None:
            for k in map.get('VpnGateway'):
                temp_model = DescribeVpnGatewaysResponseVpnGatewaysVpnGateway()
                self.vpn_gateway.append(temp_model.from_map(k))
        else:
            self.vpn_gateway = None
        return self


class DescribeVpnGatewayRequest(TeaModel):
    def __init__(self, region_id=None, vpn_gateway_id=None, include_reservation_data=None):
        self.region_id = region_id
        self.vpn_gateway_id = vpn_gateway_id
        self.include_reservation_data = include_reservation_data

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['IncludeReservationData'] = self.include_reservation_data
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.include_reservation_data = map.get('IncludeReservationData')
        return self


class DescribeVpnGatewayResponse(TeaModel):
    def __init__(self, request_id=None, vpn_gateway_id=None, vpc_id=None, v_switch_id=None, internet_ip=None,
                 create_time=None, end_time=None, spec=None, name=None, description=None, status=None, business_status=None,
                 charge_type=None, ipsec_vpn=None, ssl_vpn=None, ssl_max_connections=None, tag=None, enable_bgp=None,
                 auto_propagate=None, tags=None, reservation_data=None):
        self.request_id = request_id
        self.vpn_gateway_id = vpn_gateway_id
        self.vpc_id = vpc_id
        self.v_switch_id = v_switch_id
        self.internet_ip = internet_ip
        self.create_time = create_time
        self.end_time = end_time
        self.spec = spec
        self.name = name
        self.description = description
        self.status = status
        self.business_status = business_status
        self.charge_type = charge_type
        self.ipsec_vpn = ipsec_vpn
        self.ssl_vpn = ssl_vpn
        self.ssl_max_connections = ssl_max_connections
        self.tag = tag
        self.enable_bgp = enable_bgp
        self.auto_propagate = auto_propagate
        self.tags = tags  # type: DescribeVpnGatewayResponseTags
        self.reservation_data = reservation_data  # type: DescribeVpnGatewayResponseReservationData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.v_switch_id, 'v_switch_id')
        self.validate_required(self.internet_ip, 'internet_ip')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.spec, 'spec')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.status, 'status')
        self.validate_required(self.business_status, 'business_status')
        self.validate_required(self.charge_type, 'charge_type')
        self.validate_required(self.ipsec_vpn, 'ipsec_vpn')
        self.validate_required(self.ssl_vpn, 'ssl_vpn')
        self.validate_required(self.ssl_max_connections, 'ssl_max_connections')
        self.validate_required(self.tag, 'tag')
        self.validate_required(self.enable_bgp, 'enable_bgp')
        self.validate_required(self.auto_propagate, 'auto_propagate')
        self.validate_required(self.tags, 'tags')
        if self.tags:
            self.tags.validate()
        self.validate_required(self.reservation_data, 'reservation_data')
        if self.reservation_data:
            self.reservation_data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['VpcId'] = self.vpc_id
        result['VSwitchId'] = self.v_switch_id
        result['InternetIp'] = self.internet_ip
        result['CreateTime'] = self.create_time
        result['EndTime'] = self.end_time
        result['Spec'] = self.spec
        result['Name'] = self.name
        result['Description'] = self.description
        result['Status'] = self.status
        result['BusinessStatus'] = self.business_status
        result['ChargeType'] = self.charge_type
        result['IpsecVpn'] = self.ipsec_vpn
        result['SslVpn'] = self.ssl_vpn
        result['SslMaxConnections'] = self.ssl_max_connections
        result['Tag'] = self.tag
        result['EnableBgp'] = self.enable_bgp
        result['AutoPropagate'] = self.auto_propagate
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        else:
            result['Tags'] = None
        if self.reservation_data is not None:
            result['ReservationData'] = self.reservation_data.to_map()
        else:
            result['ReservationData'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.vpc_id = map.get('VpcId')
        self.v_switch_id = map.get('VSwitchId')
        self.internet_ip = map.get('InternetIp')
        self.create_time = map.get('CreateTime')
        self.end_time = map.get('EndTime')
        self.spec = map.get('Spec')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.status = map.get('Status')
        self.business_status = map.get('BusinessStatus')
        self.charge_type = map.get('ChargeType')
        self.ipsec_vpn = map.get('IpsecVpn')
        self.ssl_vpn = map.get('SslVpn')
        self.ssl_max_connections = map.get('SslMaxConnections')
        self.tag = map.get('Tag')
        self.enable_bgp = map.get('EnableBgp')
        self.auto_propagate = map.get('AutoPropagate')
        if map.get('Tags') is not None:
            temp_model = DescribeVpnGatewayResponseTags()
            self.tags = temp_model.from_map(map['Tags'])
        else:
            self.tags = None
        if map.get('ReservationData') is not None:
            temp_model = DescribeVpnGatewayResponseReservationData()
            self.reservation_data = temp_model.from_map(map['ReservationData'])
        else:
            self.reservation_data = None
        return self


class DescribeVpnGatewayResponseTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class DescribeVpnGatewayResponseTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag

    def validate(self):
        self.validate_required(self.tag, 'tag')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        return result

    def from_map(self, map={}):
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = DescribeVpnGatewayResponseTagsTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        return self


class DescribeVpnGatewayResponseReservationData(TeaModel):
    def __init__(self, status=None, reservation_end_time=None, reservation_order_type=None, reservation_spec=None,
                 reservation_ipsec=None, reservation_ssl=None, reservation_max_connections=None):
        self.status = status
        self.reservation_end_time = reservation_end_time
        self.reservation_order_type = reservation_order_type
        self.reservation_spec = reservation_spec
        self.reservation_ipsec = reservation_ipsec
        self.reservation_ssl = reservation_ssl
        self.reservation_max_connections = reservation_max_connections

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.reservation_end_time, 'reservation_end_time')
        self.validate_required(self.reservation_order_type, 'reservation_order_type')
        self.validate_required(self.reservation_spec, 'reservation_spec')
        self.validate_required(self.reservation_ipsec, 'reservation_ipsec')
        self.validate_required(self.reservation_ssl, 'reservation_ssl')
        self.validate_required(self.reservation_max_connections, 'reservation_max_connections')

    def to_map(self):
        result = {}
        result['Status'] = self.status
        result['ReservationEndTime'] = self.reservation_end_time
        result['ReservationOrderType'] = self.reservation_order_type
        result['ReservationSpec'] = self.reservation_spec
        result['ReservationIpsec'] = self.reservation_ipsec
        result['ReservationSsl'] = self.reservation_ssl
        result['ReservationMaxConnections'] = self.reservation_max_connections
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        self.reservation_end_time = map.get('ReservationEndTime')
        self.reservation_order_type = map.get('ReservationOrderType')
        self.reservation_spec = map.get('ReservationSpec')
        self.reservation_ipsec = map.get('ReservationIpsec')
        self.reservation_ssl = map.get('ReservationSsl')
        self.reservation_max_connections = map.get('ReservationMaxConnections')
        return self


class DescribeVpnConnectionsRequest(TeaModel):
    def __init__(self, region_id=None, vpn_gateway_id=None, customer_gateway_id=None, page_number=None,
                 page_size=None, vpn_connection_id=None):
        self.region_id = region_id
        self.vpn_gateway_id = vpn_gateway_id
        self.customer_gateway_id = customer_gateway_id
        self.page_number = page_number
        self.page_size = page_size
        self.vpn_connection_id = vpn_connection_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['CustomerGatewayId'] = self.customer_gateway_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['VpnConnectionId'] = self.vpn_connection_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.customer_gateway_id = map.get('CustomerGatewayId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.vpn_connection_id = map.get('VpnConnectionId')
        return self


class DescribeVpnConnectionsResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, vpn_connections=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.vpn_connections = vpn_connections  # type: DescribeVpnConnectionsResponseVpnConnections

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.vpn_connections, 'vpn_connections')
        if self.vpn_connections:
            self.vpn_connections.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.vpn_connections is not None:
            result['VpnConnections'] = self.vpn_connections.to_map()
        else:
            result['VpnConnections'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('VpnConnections') is not None:
            temp_model = DescribeVpnConnectionsResponseVpnConnections()
            self.vpn_connections = temp_model.from_map(map['VpnConnections'])
        else:
            self.vpn_connections = None
        return self


class DescribeVpnConnectionsResponseVpnConnectionsVpnConnectionIkeConfig(TeaModel):
    def __init__(self, psk=None, ike_version=None, ike_mode=None, ike_enc_alg=None, ike_auth_alg=None, ike_pfs=None,
                 ike_lifetime=None, local_id=None, remote_id=None):
        self.psk = psk
        self.ike_version = ike_version
        self.ike_mode = ike_mode
        self.ike_enc_alg = ike_enc_alg
        self.ike_auth_alg = ike_auth_alg
        self.ike_pfs = ike_pfs
        self.ike_lifetime = ike_lifetime
        self.local_id = local_id
        self.remote_id = remote_id

    def validate(self):
        self.validate_required(self.psk, 'psk')
        self.validate_required(self.ike_version, 'ike_version')
        self.validate_required(self.ike_mode, 'ike_mode')
        self.validate_required(self.ike_enc_alg, 'ike_enc_alg')
        self.validate_required(self.ike_auth_alg, 'ike_auth_alg')
        self.validate_required(self.ike_pfs, 'ike_pfs')
        self.validate_required(self.ike_lifetime, 'ike_lifetime')
        self.validate_required(self.local_id, 'local_id')
        self.validate_required(self.remote_id, 'remote_id')

    def to_map(self):
        result = {}
        result['Psk'] = self.psk
        result['IkeVersion'] = self.ike_version
        result['IkeMode'] = self.ike_mode
        result['IkeEncAlg'] = self.ike_enc_alg
        result['IkeAuthAlg'] = self.ike_auth_alg
        result['IkePfs'] = self.ike_pfs
        result['IkeLifetime'] = self.ike_lifetime
        result['LocalId'] = self.local_id
        result['RemoteId'] = self.remote_id
        return result

    def from_map(self, map={}):
        self.psk = map.get('Psk')
        self.ike_version = map.get('IkeVersion')
        self.ike_mode = map.get('IkeMode')
        self.ike_enc_alg = map.get('IkeEncAlg')
        self.ike_auth_alg = map.get('IkeAuthAlg')
        self.ike_pfs = map.get('IkePfs')
        self.ike_lifetime = map.get('IkeLifetime')
        self.local_id = map.get('LocalId')
        self.remote_id = map.get('RemoteId')
        return self


class DescribeVpnConnectionsResponseVpnConnectionsVpnConnectionIpsecConfig(TeaModel):
    def __init__(self, ipsec_enc_alg=None, ipsec_auth_alg=None, ipsec_pfs=None, ipsec_lifetime=None):
        self.ipsec_enc_alg = ipsec_enc_alg
        self.ipsec_auth_alg = ipsec_auth_alg
        self.ipsec_pfs = ipsec_pfs
        self.ipsec_lifetime = ipsec_lifetime

    def validate(self):
        self.validate_required(self.ipsec_enc_alg, 'ipsec_enc_alg')
        self.validate_required(self.ipsec_auth_alg, 'ipsec_auth_alg')
        self.validate_required(self.ipsec_pfs, 'ipsec_pfs')
        self.validate_required(self.ipsec_lifetime, 'ipsec_lifetime')

    def to_map(self):
        result = {}
        result['IpsecEncAlg'] = self.ipsec_enc_alg
        result['IpsecAuthAlg'] = self.ipsec_auth_alg
        result['IpsecPfs'] = self.ipsec_pfs
        result['IpsecLifetime'] = self.ipsec_lifetime
        return result

    def from_map(self, map={}):
        self.ipsec_enc_alg = map.get('IpsecEncAlg')
        self.ipsec_auth_alg = map.get('IpsecAuthAlg')
        self.ipsec_pfs = map.get('IpsecPfs')
        self.ipsec_lifetime = map.get('IpsecLifetime')
        return self


class DescribeVpnConnectionsResponseVpnConnectionsVpnConnectionVcoHealthCheck(TeaModel):
    def __init__(self, enable=None, sip=None, dip=None, interval=None, retry=None, status=None):
        self.enable = enable
        self.sip = sip
        self.dip = dip
        self.interval = interval
        self.retry = retry
        self.status = status

    def validate(self):
        self.validate_required(self.enable, 'enable')
        self.validate_required(self.sip, 'sip')
        self.validate_required(self.dip, 'dip')
        self.validate_required(self.interval, 'interval')
        self.validate_required(self.retry, 'retry')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['Enable'] = self.enable
        result['Sip'] = self.sip
        result['Dip'] = self.dip
        result['Interval'] = self.interval
        result['Retry'] = self.retry
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.enable = map.get('Enable')
        self.sip = map.get('Sip')
        self.dip = map.get('Dip')
        self.interval = map.get('Interval')
        self.retry = map.get('Retry')
        self.status = map.get('Status')
        return self


class DescribeVpnConnectionsResponseVpnConnectionsVpnConnectionVpnBgpConfig(TeaModel):
    def __init__(self, tunnel_cidr=None, local_bgp_ip=None, peer_bgp_ip=None, local_asn=None, peer_asn=None,
                 status=None):
        self.tunnel_cidr = tunnel_cidr
        self.local_bgp_ip = local_bgp_ip
        self.peer_bgp_ip = peer_bgp_ip
        self.local_asn = local_asn
        self.peer_asn = peer_asn
        self.status = status

    def validate(self):
        self.validate_required(self.tunnel_cidr, 'tunnel_cidr')
        self.validate_required(self.local_bgp_ip, 'local_bgp_ip')
        self.validate_required(self.peer_bgp_ip, 'peer_bgp_ip')
        self.validate_required(self.local_asn, 'local_asn')
        self.validate_required(self.peer_asn, 'peer_asn')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['TunnelCidr'] = self.tunnel_cidr
        result['LocalBgpIp'] = self.local_bgp_ip
        result['PeerBgpIp'] = self.peer_bgp_ip
        result['LocalAsn'] = self.local_asn
        result['PeerAsn'] = self.peer_asn
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.tunnel_cidr = map.get('TunnelCidr')
        self.local_bgp_ip = map.get('LocalBgpIp')
        self.peer_bgp_ip = map.get('PeerBgpIp')
        self.local_asn = map.get('LocalAsn')
        self.peer_asn = map.get('PeerAsn')
        self.status = map.get('Status')
        return self


class DescribeVpnConnectionsResponseVpnConnectionsVpnConnection(TeaModel):
    def __init__(self, vpn_connection_id=None, customer_gateway_id=None, vpn_gateway_id=None, name=None,
                 local_subnet=None, remote_subnet=None, create_time=None, effect_immediately=None, status=None, enable_dpd=None,
                 enable_nat_traversal=None, ike_config=None, ipsec_config=None, vco_health_check=None, vpn_bgp_config=None):
        self.vpn_connection_id = vpn_connection_id
        self.customer_gateway_id = customer_gateway_id
        self.vpn_gateway_id = vpn_gateway_id
        self.name = name
        self.local_subnet = local_subnet
        self.remote_subnet = remote_subnet
        self.create_time = create_time
        self.effect_immediately = effect_immediately
        self.status = status
        self.enable_dpd = enable_dpd
        self.enable_nat_traversal = enable_nat_traversal
        self.ike_config = ike_config  # type: DescribeVpnConnectionsResponseVpnConnectionsVpnConnectionIkeConfig
        self.ipsec_config = ipsec_config  # type: DescribeVpnConnectionsResponseVpnConnectionsVpnConnectionIpsecConfig
        self.vco_health_check = vco_health_check  # type: DescribeVpnConnectionsResponseVpnConnectionsVpnConnectionVcoHealthCheck
        self.vpn_bgp_config = vpn_bgp_config  # type: DescribeVpnConnectionsResponseVpnConnectionsVpnConnectionVpnBgpConfig

    def validate(self):
        self.validate_required(self.vpn_connection_id, 'vpn_connection_id')
        self.validate_required(self.customer_gateway_id, 'customer_gateway_id')
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.local_subnet, 'local_subnet')
        self.validate_required(self.remote_subnet, 'remote_subnet')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.effect_immediately, 'effect_immediately')
        self.validate_required(self.status, 'status')
        self.validate_required(self.enable_dpd, 'enable_dpd')
        self.validate_required(self.enable_nat_traversal, 'enable_nat_traversal')
        self.validate_required(self.ike_config, 'ike_config')
        if self.ike_config:
            self.ike_config.validate()
        self.validate_required(self.ipsec_config, 'ipsec_config')
        if self.ipsec_config:
            self.ipsec_config.validate()
        self.validate_required(self.vco_health_check, 'vco_health_check')
        if self.vco_health_check:
            self.vco_health_check.validate()
        self.validate_required(self.vpn_bgp_config, 'vpn_bgp_config')
        if self.vpn_bgp_config:
            self.vpn_bgp_config.validate()

    def to_map(self):
        result = {}
        result['VpnConnectionId'] = self.vpn_connection_id
        result['CustomerGatewayId'] = self.customer_gateway_id
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['Name'] = self.name
        result['LocalSubnet'] = self.local_subnet
        result['RemoteSubnet'] = self.remote_subnet
        result['CreateTime'] = self.create_time
        result['EffectImmediately'] = self.effect_immediately
        result['Status'] = self.status
        result['EnableDpd'] = self.enable_dpd
        result['EnableNatTraversal'] = self.enable_nat_traversal
        if self.ike_config is not None:
            result['IkeConfig'] = self.ike_config.to_map()
        else:
            result['IkeConfig'] = None
        if self.ipsec_config is not None:
            result['IpsecConfig'] = self.ipsec_config.to_map()
        else:
            result['IpsecConfig'] = None
        if self.vco_health_check is not None:
            result['VcoHealthCheck'] = self.vco_health_check.to_map()
        else:
            result['VcoHealthCheck'] = None
        if self.vpn_bgp_config is not None:
            result['VpnBgpConfig'] = self.vpn_bgp_config.to_map()
        else:
            result['VpnBgpConfig'] = None
        return result

    def from_map(self, map={}):
        self.vpn_connection_id = map.get('VpnConnectionId')
        self.customer_gateway_id = map.get('CustomerGatewayId')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.name = map.get('Name')
        self.local_subnet = map.get('LocalSubnet')
        self.remote_subnet = map.get('RemoteSubnet')
        self.create_time = map.get('CreateTime')
        self.effect_immediately = map.get('EffectImmediately')
        self.status = map.get('Status')
        self.enable_dpd = map.get('EnableDpd')
        self.enable_nat_traversal = map.get('EnableNatTraversal')
        if map.get('IkeConfig') is not None:
            temp_model = DescribeVpnConnectionsResponseVpnConnectionsVpnConnectionIkeConfig()
            self.ike_config = temp_model.from_map(map['IkeConfig'])
        else:
            self.ike_config = None
        if map.get('IpsecConfig') is not None:
            temp_model = DescribeVpnConnectionsResponseVpnConnectionsVpnConnectionIpsecConfig()
            self.ipsec_config = temp_model.from_map(map['IpsecConfig'])
        else:
            self.ipsec_config = None
        if map.get('VcoHealthCheck') is not None:
            temp_model = DescribeVpnConnectionsResponseVpnConnectionsVpnConnectionVcoHealthCheck()
            self.vco_health_check = temp_model.from_map(map['VcoHealthCheck'])
        else:
            self.vco_health_check = None
        if map.get('VpnBgpConfig') is not None:
            temp_model = DescribeVpnConnectionsResponseVpnConnectionsVpnConnectionVpnBgpConfig()
            self.vpn_bgp_config = temp_model.from_map(map['VpnBgpConfig'])
        else:
            self.vpn_bgp_config = None
        return self


class DescribeVpnConnectionsResponseVpnConnections(TeaModel):
    def __init__(self, vpn_connection=None):
        self.vpn_connection = vpn_connection

    def validate(self):
        self.validate_required(self.vpn_connection, 'vpn_connection')
        if self.vpn_connection:
            for k in self.vpn_connection:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['VpnConnection'] = []
        if self.vpn_connection is not None:
            for k in self.vpn_connection:
                result['VpnConnection'].append(k.to_map() if k else None)
        else:
            result['VpnConnection'] = None
        return result

    def from_map(self, map={}):
        self.vpn_connection = []
        if map.get('VpnConnection') is not None:
            for k in map.get('VpnConnection'):
                temp_model = DescribeVpnConnectionsResponseVpnConnectionsVpnConnection()
                self.vpn_connection.append(temp_model.from_map(k))
        else:
            self.vpn_connection = None
        return self


class DescribeVpnConnectionRequest(TeaModel):
    def __init__(self, region_id=None, vpn_connection_id=None):
        self.region_id = region_id
        self.vpn_connection_id = vpn_connection_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpn_connection_id, 'vpn_connection_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VpnConnectionId'] = self.vpn_connection_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vpn_connection_id = map.get('VpnConnectionId')
        return self


class DescribeVpnConnectionResponse(TeaModel):
    def __init__(self, request_id=None, vpn_connection_id=None, customer_gateway_id=None, vpn_gateway_id=None,
                 name=None, local_subnet=None, remote_subnet=None, create_time=None, effect_immediately=None,
                 status=None, enable_dpd=None, enable_nat_traversal=None, ike_config=None, ipsec_config=None,
                 vco_health_check=None, vpn_bgp_config=None):
        self.request_id = request_id
        self.vpn_connection_id = vpn_connection_id
        self.customer_gateway_id = customer_gateway_id
        self.vpn_gateway_id = vpn_gateway_id
        self.name = name
        self.local_subnet = local_subnet
        self.remote_subnet = remote_subnet
        self.create_time = create_time
        self.effect_immediately = effect_immediately
        self.status = status
        self.enable_dpd = enable_dpd
        self.enable_nat_traversal = enable_nat_traversal
        self.ike_config = ike_config  # type: DescribeVpnConnectionResponseIkeConfig
        self.ipsec_config = ipsec_config  # type: DescribeVpnConnectionResponseIpsecConfig
        self.vco_health_check = vco_health_check  # type: DescribeVpnConnectionResponseVcoHealthCheck
        self.vpn_bgp_config = vpn_bgp_config  # type: DescribeVpnConnectionResponseVpnBgpConfig

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.vpn_connection_id, 'vpn_connection_id')
        self.validate_required(self.customer_gateway_id, 'customer_gateway_id')
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.local_subnet, 'local_subnet')
        self.validate_required(self.remote_subnet, 'remote_subnet')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.effect_immediately, 'effect_immediately')
        self.validate_required(self.status, 'status')
        self.validate_required(self.enable_dpd, 'enable_dpd')
        self.validate_required(self.enable_nat_traversal, 'enable_nat_traversal')
        self.validate_required(self.ike_config, 'ike_config')
        if self.ike_config:
            self.ike_config.validate()
        self.validate_required(self.ipsec_config, 'ipsec_config')
        if self.ipsec_config:
            self.ipsec_config.validate()
        self.validate_required(self.vco_health_check, 'vco_health_check')
        if self.vco_health_check:
            self.vco_health_check.validate()
        self.validate_required(self.vpn_bgp_config, 'vpn_bgp_config')
        if self.vpn_bgp_config:
            self.vpn_bgp_config.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['VpnConnectionId'] = self.vpn_connection_id
        result['CustomerGatewayId'] = self.customer_gateway_id
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['Name'] = self.name
        result['LocalSubnet'] = self.local_subnet
        result['RemoteSubnet'] = self.remote_subnet
        result['CreateTime'] = self.create_time
        result['EffectImmediately'] = self.effect_immediately
        result['Status'] = self.status
        result['EnableDpd'] = self.enable_dpd
        result['EnableNatTraversal'] = self.enable_nat_traversal
        if self.ike_config is not None:
            result['IkeConfig'] = self.ike_config.to_map()
        else:
            result['IkeConfig'] = None
        if self.ipsec_config is not None:
            result['IpsecConfig'] = self.ipsec_config.to_map()
        else:
            result['IpsecConfig'] = None
        if self.vco_health_check is not None:
            result['VcoHealthCheck'] = self.vco_health_check.to_map()
        else:
            result['VcoHealthCheck'] = None
        if self.vpn_bgp_config is not None:
            result['VpnBgpConfig'] = self.vpn_bgp_config.to_map()
        else:
            result['VpnBgpConfig'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.vpn_connection_id = map.get('VpnConnectionId')
        self.customer_gateway_id = map.get('CustomerGatewayId')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.name = map.get('Name')
        self.local_subnet = map.get('LocalSubnet')
        self.remote_subnet = map.get('RemoteSubnet')
        self.create_time = map.get('CreateTime')
        self.effect_immediately = map.get('EffectImmediately')
        self.status = map.get('Status')
        self.enable_dpd = map.get('EnableDpd')
        self.enable_nat_traversal = map.get('EnableNatTraversal')
        if map.get('IkeConfig') is not None:
            temp_model = DescribeVpnConnectionResponseIkeConfig()
            self.ike_config = temp_model.from_map(map['IkeConfig'])
        else:
            self.ike_config = None
        if map.get('IpsecConfig') is not None:
            temp_model = DescribeVpnConnectionResponseIpsecConfig()
            self.ipsec_config = temp_model.from_map(map['IpsecConfig'])
        else:
            self.ipsec_config = None
        if map.get('VcoHealthCheck') is not None:
            temp_model = DescribeVpnConnectionResponseVcoHealthCheck()
            self.vco_health_check = temp_model.from_map(map['VcoHealthCheck'])
        else:
            self.vco_health_check = None
        if map.get('VpnBgpConfig') is not None:
            temp_model = DescribeVpnConnectionResponseVpnBgpConfig()
            self.vpn_bgp_config = temp_model.from_map(map['VpnBgpConfig'])
        else:
            self.vpn_bgp_config = None
        return self


class DescribeVpnConnectionResponseIkeConfig(TeaModel):
    def __init__(self, psk=None, ike_version=None, ike_mode=None, ike_enc_alg=None, ike_auth_alg=None, ike_pfs=None,
                 ike_lifetime=None, local_id=None, remote_id=None):
        self.psk = psk
        self.ike_version = ike_version
        self.ike_mode = ike_mode
        self.ike_enc_alg = ike_enc_alg
        self.ike_auth_alg = ike_auth_alg
        self.ike_pfs = ike_pfs
        self.ike_lifetime = ike_lifetime
        self.local_id = local_id
        self.remote_id = remote_id

    def validate(self):
        self.validate_required(self.psk, 'psk')
        self.validate_required(self.ike_version, 'ike_version')
        self.validate_required(self.ike_mode, 'ike_mode')
        self.validate_required(self.ike_enc_alg, 'ike_enc_alg')
        self.validate_required(self.ike_auth_alg, 'ike_auth_alg')
        self.validate_required(self.ike_pfs, 'ike_pfs')
        self.validate_required(self.ike_lifetime, 'ike_lifetime')
        self.validate_required(self.local_id, 'local_id')
        self.validate_required(self.remote_id, 'remote_id')

    def to_map(self):
        result = {}
        result['Psk'] = self.psk
        result['IkeVersion'] = self.ike_version
        result['IkeMode'] = self.ike_mode
        result['IkeEncAlg'] = self.ike_enc_alg
        result['IkeAuthAlg'] = self.ike_auth_alg
        result['IkePfs'] = self.ike_pfs
        result['IkeLifetime'] = self.ike_lifetime
        result['LocalId'] = self.local_id
        result['RemoteId'] = self.remote_id
        return result

    def from_map(self, map={}):
        self.psk = map.get('Psk')
        self.ike_version = map.get('IkeVersion')
        self.ike_mode = map.get('IkeMode')
        self.ike_enc_alg = map.get('IkeEncAlg')
        self.ike_auth_alg = map.get('IkeAuthAlg')
        self.ike_pfs = map.get('IkePfs')
        self.ike_lifetime = map.get('IkeLifetime')
        self.local_id = map.get('LocalId')
        self.remote_id = map.get('RemoteId')
        return self


class DescribeVpnConnectionResponseIpsecConfig(TeaModel):
    def __init__(self, ipsec_enc_alg=None, ipsec_auth_alg=None, ipsec_pfs=None, ipsec_lifetime=None):
        self.ipsec_enc_alg = ipsec_enc_alg
        self.ipsec_auth_alg = ipsec_auth_alg
        self.ipsec_pfs = ipsec_pfs
        self.ipsec_lifetime = ipsec_lifetime

    def validate(self):
        self.validate_required(self.ipsec_enc_alg, 'ipsec_enc_alg')
        self.validate_required(self.ipsec_auth_alg, 'ipsec_auth_alg')
        self.validate_required(self.ipsec_pfs, 'ipsec_pfs')
        self.validate_required(self.ipsec_lifetime, 'ipsec_lifetime')

    def to_map(self):
        result = {}
        result['IpsecEncAlg'] = self.ipsec_enc_alg
        result['IpsecAuthAlg'] = self.ipsec_auth_alg
        result['IpsecPfs'] = self.ipsec_pfs
        result['IpsecLifetime'] = self.ipsec_lifetime
        return result

    def from_map(self, map={}):
        self.ipsec_enc_alg = map.get('IpsecEncAlg')
        self.ipsec_auth_alg = map.get('IpsecAuthAlg')
        self.ipsec_pfs = map.get('IpsecPfs')
        self.ipsec_lifetime = map.get('IpsecLifetime')
        return self


class DescribeVpnConnectionResponseVcoHealthCheck(TeaModel):
    def __init__(self, enable=None, sip=None, dip=None, interval=None, retry=None, status=None):
        self.enable = enable
        self.sip = sip
        self.dip = dip
        self.interval = interval
        self.retry = retry
        self.status = status

    def validate(self):
        self.validate_required(self.enable, 'enable')
        self.validate_required(self.sip, 'sip')
        self.validate_required(self.dip, 'dip')
        self.validate_required(self.interval, 'interval')
        self.validate_required(self.retry, 'retry')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['Enable'] = self.enable
        result['Sip'] = self.sip
        result['Dip'] = self.dip
        result['Interval'] = self.interval
        result['Retry'] = self.retry
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.enable = map.get('Enable')
        self.sip = map.get('Sip')
        self.dip = map.get('Dip')
        self.interval = map.get('Interval')
        self.retry = map.get('Retry')
        self.status = map.get('Status')
        return self


class DescribeVpnConnectionResponseVpnBgpConfig(TeaModel):
    def __init__(self, enable_bgp=None, tunnel_cidr=None, local_bgp_ip=None, peer_bgp_ip=None, local_asn=None,
                 peer_asn=None, status=None):
        self.enable_bgp = enable_bgp
        self.tunnel_cidr = tunnel_cidr
        self.local_bgp_ip = local_bgp_ip
        self.peer_bgp_ip = peer_bgp_ip
        self.local_asn = local_asn
        self.peer_asn = peer_asn
        self.status = status

    def validate(self):
        self.validate_required(self.enable_bgp, 'enable_bgp')
        self.validate_required(self.tunnel_cidr, 'tunnel_cidr')
        self.validate_required(self.local_bgp_ip, 'local_bgp_ip')
        self.validate_required(self.peer_bgp_ip, 'peer_bgp_ip')
        self.validate_required(self.local_asn, 'local_asn')
        self.validate_required(self.peer_asn, 'peer_asn')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['EnableBgp'] = self.enable_bgp
        result['TunnelCidr'] = self.tunnel_cidr
        result['LocalBgpIp'] = self.local_bgp_ip
        result['PeerBgpIp'] = self.peer_bgp_ip
        result['LocalAsn'] = self.local_asn
        result['PeerAsn'] = self.peer_asn
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.enable_bgp = map.get('EnableBgp')
        self.tunnel_cidr = map.get('TunnelCidr')
        self.local_bgp_ip = map.get('LocalBgpIp')
        self.peer_bgp_ip = map.get('PeerBgpIp')
        self.local_asn = map.get('LocalAsn')
        self.peer_asn = map.get('PeerAsn')
        self.status = map.get('Status')
        return self


class DescribeCustomerGatewaysRequest(TeaModel):
    def __init__(self, region_id=None, customer_gateway_id=None, page_number=None, page_size=None):
        self.region_id = region_id
        self.customer_gateway_id = customer_gateway_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['CustomerGatewayId'] = self.customer_gateway_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.customer_gateway_id = map.get('CustomerGatewayId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeCustomerGatewaysResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, customer_gateways=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.customer_gateways = customer_gateways  # type: DescribeCustomerGatewaysResponseCustomerGateways

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.customer_gateways, 'customer_gateways')
        if self.customer_gateways:
            self.customer_gateways.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.customer_gateways is not None:
            result['CustomerGateways'] = self.customer_gateways.to_map()
        else:
            result['CustomerGateways'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('CustomerGateways') is not None:
            temp_model = DescribeCustomerGatewaysResponseCustomerGateways()
            self.customer_gateways = temp_model.from_map(map['CustomerGateways'])
        else:
            self.customer_gateways = None
        return self


class DescribeCustomerGatewaysResponseCustomerGatewaysCustomerGateway(TeaModel):
    def __init__(self, customer_gateway_id=None, name=None, ip_address=None, description=None, create_time=None,
                 asn=None):
        self.customer_gateway_id = customer_gateway_id
        self.name = name
        self.ip_address = ip_address
        self.description = description
        self.create_time = create_time
        self.asn = asn

    def validate(self):
        self.validate_required(self.customer_gateway_id, 'customer_gateway_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.ip_address, 'ip_address')
        self.validate_required(self.description, 'description')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.asn, 'asn')

    def to_map(self):
        result = {}
        result['CustomerGatewayId'] = self.customer_gateway_id
        result['Name'] = self.name
        result['IpAddress'] = self.ip_address
        result['Description'] = self.description
        result['CreateTime'] = self.create_time
        result['Asn'] = self.asn
        return result

    def from_map(self, map={}):
        self.customer_gateway_id = map.get('CustomerGatewayId')
        self.name = map.get('Name')
        self.ip_address = map.get('IpAddress')
        self.description = map.get('Description')
        self.create_time = map.get('CreateTime')
        self.asn = map.get('Asn')
        return self


class DescribeCustomerGatewaysResponseCustomerGateways(TeaModel):
    def __init__(self, customer_gateway=None):
        self.customer_gateway = customer_gateway

    def validate(self):
        self.validate_required(self.customer_gateway, 'customer_gateway')
        if self.customer_gateway:
            for k in self.customer_gateway:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['CustomerGateway'] = []
        if self.customer_gateway is not None:
            for k in self.customer_gateway:
                result['CustomerGateway'].append(k.to_map() if k else None)
        else:
            result['CustomerGateway'] = None
        return result

    def from_map(self, map={}):
        self.customer_gateway = []
        if map.get('CustomerGateway') is not None:
            for k in map.get('CustomerGateway'):
                temp_model = DescribeCustomerGatewaysResponseCustomerGatewaysCustomerGateway()
                self.customer_gateway.append(temp_model.from_map(k))
        else:
            self.customer_gateway = None
        return self


class DescribeCustomerGatewayRequest(TeaModel):
    def __init__(self, region_id=None, customer_gateway_id=None):
        self.region_id = region_id
        self.customer_gateway_id = customer_gateway_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.customer_gateway_id, 'customer_gateway_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['CustomerGatewayId'] = self.customer_gateway_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.customer_gateway_id = map.get('CustomerGatewayId')
        return self


class DescribeCustomerGatewayResponse(TeaModel):
    def __init__(self, request_id=None, customer_gateway_id=None, ip_address=None, name=None, description=None,
                 create_time=None, asn=None):
        self.request_id = request_id
        self.customer_gateway_id = customer_gateway_id
        self.ip_address = ip_address
        self.name = name
        self.description = description
        self.create_time = create_time
        self.asn = asn

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.customer_gateway_id, 'customer_gateway_id')
        self.validate_required(self.ip_address, 'ip_address')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.asn, 'asn')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['CustomerGatewayId'] = self.customer_gateway_id
        result['IpAddress'] = self.ip_address
        result['Name'] = self.name
        result['Description'] = self.description
        result['CreateTime'] = self.create_time
        result['Asn'] = self.asn
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.customer_gateway_id = map.get('CustomerGatewayId')
        self.ip_address = map.get('IpAddress')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.create_time = map.get('CreateTime')
        self.asn = map.get('Asn')
        return self


class DeleteVpnGatewayRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, vpn_gateway_id=None):
        self.region_id = region_id
        self.client_token = client_token
        self.vpn_gateway_id = vpn_gateway_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['VpnGatewayId'] = self.vpn_gateway_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        return self


class DeleteVpnGatewayResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteVpnConnectionRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, vpn_connection_id=None):
        self.region_id = region_id
        self.client_token = client_token
        self.vpn_connection_id = vpn_connection_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpn_connection_id, 'vpn_connection_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['VpnConnectionId'] = self.vpn_connection_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.vpn_connection_id = map.get('VpnConnectionId')
        return self


class DeleteVpnConnectionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteCustomerGatewayRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, customer_gateway_id=None):
        self.region_id = region_id
        self.client_token = client_token
        self.customer_gateway_id = customer_gateway_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.customer_gateway_id, 'customer_gateway_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['CustomerGatewayId'] = self.customer_gateway_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.customer_gateway_id = map.get('CustomerGatewayId')
        return self


class DeleteCustomerGatewayResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateVpnConnectionRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, customer_gateway_id=None, vpn_gateway_id=None, name=None,
                 local_subnet=None, remote_subnet=None, effect_immediately=None, ike_config=None, ipsec_config=None,
                 health_check_config=None, auto_config_route=None, enable_dpd=None, enable_nat_traversal=None, bgp_config=None):
        self.region_id = region_id
        self.client_token = client_token
        self.customer_gateway_id = customer_gateway_id
        self.vpn_gateway_id = vpn_gateway_id
        self.name = name
        self.local_subnet = local_subnet
        self.remote_subnet = remote_subnet
        self.effect_immediately = effect_immediately
        self.ike_config = ike_config
        self.ipsec_config = ipsec_config
        self.health_check_config = health_check_config
        self.auto_config_route = auto_config_route
        self.enable_dpd = enable_dpd
        self.enable_nat_traversal = enable_nat_traversal
        self.bgp_config = bgp_config

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.customer_gateway_id, 'customer_gateway_id')
        self.validate_required(self.vpn_gateway_id, 'vpn_gateway_id')
        self.validate_required(self.local_subnet, 'local_subnet')
        self.validate_required(self.remote_subnet, 'remote_subnet')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['CustomerGatewayId'] = self.customer_gateway_id
        result['VpnGatewayId'] = self.vpn_gateway_id
        result['Name'] = self.name
        result['LocalSubnet'] = self.local_subnet
        result['RemoteSubnet'] = self.remote_subnet
        result['EffectImmediately'] = self.effect_immediately
        result['IkeConfig'] = self.ike_config
        result['IpsecConfig'] = self.ipsec_config
        result['HealthCheckConfig'] = self.health_check_config
        result['AutoConfigRoute'] = self.auto_config_route
        result['EnableDpd'] = self.enable_dpd
        result['EnableNatTraversal'] = self.enable_nat_traversal
        result['BgpConfig'] = self.bgp_config
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.customer_gateway_id = map.get('CustomerGatewayId')
        self.vpn_gateway_id = map.get('VpnGatewayId')
        self.name = map.get('Name')
        self.local_subnet = map.get('LocalSubnet')
        self.remote_subnet = map.get('RemoteSubnet')
        self.effect_immediately = map.get('EffectImmediately')
        self.ike_config = map.get('IkeConfig')
        self.ipsec_config = map.get('IpsecConfig')
        self.health_check_config = map.get('HealthCheckConfig')
        self.auto_config_route = map.get('AutoConfigRoute')
        self.enable_dpd = map.get('EnableDpd')
        self.enable_nat_traversal = map.get('EnableNatTraversal')
        self.bgp_config = map.get('BgpConfig')
        return self


class CreateVpnConnectionResponse(TeaModel):
    def __init__(self, request_id=None, vpn_connection_id=None, name=None, create_time=None):
        self.request_id = request_id
        self.vpn_connection_id = vpn_connection_id
        self.name = name
        self.create_time = create_time

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.vpn_connection_id, 'vpn_connection_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.create_time, 'create_time')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['VpnConnectionId'] = self.vpn_connection_id
        result['Name'] = self.name
        result['CreateTime'] = self.create_time
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.vpn_connection_id = map.get('VpnConnectionId')
        self.name = map.get('Name')
        self.create_time = map.get('CreateTime')
        return self


class CreateCustomerGatewayRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, ip_address=None, name=None, description=None, asn=None):
        self.region_id = region_id
        self.client_token = client_token
        self.ip_address = ip_address
        self.name = name
        self.description = description
        self.asn = asn

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ip_address, 'ip_address')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['IpAddress'] = self.ip_address
        result['Name'] = self.name
        result['Description'] = self.description
        result['Asn'] = self.asn
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.ip_address = map.get('IpAddress')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.asn = map.get('Asn')
        return self


class CreateCustomerGatewayResponse(TeaModel):
    def __init__(self, request_id=None, customer_gateway_id=None, ip_address=None, name=None, description=None,
                 create_time=None):
        self.request_id = request_id
        self.customer_gateway_id = customer_gateway_id
        self.ip_address = ip_address
        self.name = name
        self.description = description
        self.create_time = create_time

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.customer_gateway_id, 'customer_gateway_id')
        self.validate_required(self.ip_address, 'ip_address')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.create_time, 'create_time')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['CustomerGatewayId'] = self.customer_gateway_id
        result['IpAddress'] = self.ip_address
        result['Name'] = self.name
        result['Description'] = self.description
        result['CreateTime'] = self.create_time
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.customer_gateway_id = map.get('CustomerGatewayId')
        self.ip_address = map.get('IpAddress')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.create_time = map.get('CreateTime')
        return self


class ModifyBgpGroupAttributeRequest(TeaModel):
    def __init__(self, region_id=None, bgp_group_id=None, name=None, description=None, local_asn=None, peer_asn=None,
                 auth_key=None, is_fake_asn=None, client_token=None):
        self.region_id = region_id
        self.bgp_group_id = bgp_group_id
        self.name = name
        self.description = description
        self.local_asn = local_asn
        self.peer_asn = peer_asn
        self.auth_key = auth_key
        self.is_fake_asn = is_fake_asn
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bgp_group_id, 'bgp_group_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['BgpGroupId'] = self.bgp_group_id
        result['Name'] = self.name
        result['Description'] = self.description
        result['LocalAsn'] = self.local_asn
        result['PeerAsn'] = self.peer_asn
        result['AuthKey'] = self.auth_key
        result['IsFakeAsn'] = self.is_fake_asn
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.bgp_group_id = map.get('BgpGroupId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.local_asn = map.get('LocalAsn')
        self.peer_asn = map.get('PeerAsn')
        self.auth_key = map.get('AuthKey')
        self.is_fake_asn = map.get('IsFakeAsn')
        self.client_token = map.get('ClientToken')
        return self


class ModifyBgpGroupAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeBgpPeersRequest(TeaModel):
    def __init__(self, router_id=None, bgp_peer_id=None, bgp_group_id=None, region_id=None, is_default=None,
                 page_number=None, page_size=None):
        self.router_id = router_id
        self.bgp_peer_id = bgp_peer_id
        self.bgp_group_id = bgp_group_id
        self.region_id = region_id
        self.is_default = is_default
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RouterId'] = self.router_id
        result['BgpPeerId'] = self.bgp_peer_id
        result['BgpGroupId'] = self.bgp_group_id
        result['RegionId'] = self.region_id
        result['IsDefault'] = self.is_default
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.router_id = map.get('RouterId')
        self.bgp_peer_id = map.get('BgpPeerId')
        self.bgp_group_id = map.get('BgpGroupId')
        self.region_id = map.get('RegionId')
        self.is_default = map.get('IsDefault')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeBgpPeersResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, bgp_peers=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.bgp_peers = bgp_peers  # type: DescribeBgpPeersResponseBgpPeers

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.bgp_peers, 'bgp_peers')
        if self.bgp_peers:
            self.bgp_peers.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.bgp_peers is not None:
            result['BgpPeers'] = self.bgp_peers.to_map()
        else:
            result['BgpPeers'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('BgpPeers') is not None:
            temp_model = DescribeBgpPeersResponseBgpPeers()
            self.bgp_peers = temp_model.from_map(map['BgpPeers'])
        else:
            self.bgp_peers = None
        return self


class DescribeBgpPeersResponseBgpPeersBgpPeer(TeaModel):
    def __init__(self, name=None, description=None, bgp_peer_id=None, bgp_group_id=None, peer_ip_address=None,
                 peer_asn=None, auth_key=None, router_id=None, bgp_status=None, status=None, keepalive=None, local_asn=None,
                 hold=None, is_fake=None, route_limit=None, region_id=None, enable_bfd=None, ip_version=None,
                 bfd_multi_hop=None):
        self.name = name
        self.description = description
        self.bgp_peer_id = bgp_peer_id
        self.bgp_group_id = bgp_group_id
        self.peer_ip_address = peer_ip_address
        self.peer_asn = peer_asn
        self.auth_key = auth_key
        self.router_id = router_id
        self.bgp_status = bgp_status
        self.status = status
        self.keepalive = keepalive
        self.local_asn = local_asn
        self.hold = hold
        self.is_fake = is_fake
        self.route_limit = route_limit
        self.region_id = region_id
        self.enable_bfd = enable_bfd
        self.ip_version = ip_version
        self.bfd_multi_hop = bfd_multi_hop

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.bgp_peer_id, 'bgp_peer_id')
        self.validate_required(self.bgp_group_id, 'bgp_group_id')
        self.validate_required(self.peer_ip_address, 'peer_ip_address')
        self.validate_required(self.peer_asn, 'peer_asn')
        self.validate_required(self.auth_key, 'auth_key')
        self.validate_required(self.router_id, 'router_id')
        self.validate_required(self.bgp_status, 'bgp_status')
        self.validate_required(self.status, 'status')
        self.validate_required(self.keepalive, 'keepalive')
        self.validate_required(self.local_asn, 'local_asn')
        self.validate_required(self.hold, 'hold')
        self.validate_required(self.is_fake, 'is_fake')
        self.validate_required(self.route_limit, 'route_limit')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.enable_bfd, 'enable_bfd')
        self.validate_required(self.ip_version, 'ip_version')
        self.validate_required(self.bfd_multi_hop, 'bfd_multi_hop')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Description'] = self.description
        result['BgpPeerId'] = self.bgp_peer_id
        result['BgpGroupId'] = self.bgp_group_id
        result['PeerIpAddress'] = self.peer_ip_address
        result['PeerAsn'] = self.peer_asn
        result['AuthKey'] = self.auth_key
        result['RouterId'] = self.router_id
        result['BgpStatus'] = self.bgp_status
        result['Status'] = self.status
        result['Keepalive'] = self.keepalive
        result['LocalAsn'] = self.local_asn
        result['Hold'] = self.hold
        result['IsFake'] = self.is_fake
        result['RouteLimit'] = self.route_limit
        result['RegionId'] = self.region_id
        result['EnableBfd'] = self.enable_bfd
        result['IpVersion'] = self.ip_version
        result['BfdMultiHop'] = self.bfd_multi_hop
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.bgp_peer_id = map.get('BgpPeerId')
        self.bgp_group_id = map.get('BgpGroupId')
        self.peer_ip_address = map.get('PeerIpAddress')
        self.peer_asn = map.get('PeerAsn')
        self.auth_key = map.get('AuthKey')
        self.router_id = map.get('RouterId')
        self.bgp_status = map.get('BgpStatus')
        self.status = map.get('Status')
        self.keepalive = map.get('Keepalive')
        self.local_asn = map.get('LocalAsn')
        self.hold = map.get('Hold')
        self.is_fake = map.get('IsFake')
        self.route_limit = map.get('RouteLimit')
        self.region_id = map.get('RegionId')
        self.enable_bfd = map.get('EnableBfd')
        self.ip_version = map.get('IpVersion')
        self.bfd_multi_hop = map.get('BfdMultiHop')
        return self


class DescribeBgpPeersResponseBgpPeers(TeaModel):
    def __init__(self, bgp_peer=None):
        self.bgp_peer = bgp_peer

    def validate(self):
        self.validate_required(self.bgp_peer, 'bgp_peer')
        if self.bgp_peer:
            for k in self.bgp_peer:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['BgpPeer'] = []
        if self.bgp_peer is not None:
            for k in self.bgp_peer:
                result['BgpPeer'].append(k.to_map() if k else None)
        else:
            result['BgpPeer'] = None
        return result

    def from_map(self, map={}):
        self.bgp_peer = []
        if map.get('BgpPeer') is not None:
            for k in map.get('BgpPeer'):
                temp_model = DescribeBgpPeersResponseBgpPeersBgpPeer()
                self.bgp_peer.append(temp_model.from_map(k))
        else:
            self.bgp_peer = None
        return self


class DescribeBgpGroupsRequest(TeaModel):
    def __init__(self, router_id=None, bgp_group_id=None, region_id=None, is_default=None, page_number=None,
                 page_size=None):
        self.router_id = router_id
        self.bgp_group_id = bgp_group_id
        self.region_id = region_id
        self.is_default = is_default
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RouterId'] = self.router_id
        result['BgpGroupId'] = self.bgp_group_id
        result['RegionId'] = self.region_id
        result['IsDefault'] = self.is_default
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.router_id = map.get('RouterId')
        self.bgp_group_id = map.get('BgpGroupId')
        self.region_id = map.get('RegionId')
        self.is_default = map.get('IsDefault')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeBgpGroupsResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, bgp_groups=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.bgp_groups = bgp_groups  # type: DescribeBgpGroupsResponseBgpGroups

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.bgp_groups, 'bgp_groups')
        if self.bgp_groups:
            self.bgp_groups.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.bgp_groups is not None:
            result['BgpGroups'] = self.bgp_groups.to_map()
        else:
            result['BgpGroups'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('BgpGroups') is not None:
            temp_model = DescribeBgpGroupsResponseBgpGroups()
            self.bgp_groups = temp_model.from_map(map['BgpGroups'])
        else:
            self.bgp_groups = None
        return self


class DescribeBgpGroupsResponseBgpGroupsBgpGroup(TeaModel):
    def __init__(self, name=None, description=None, bgp_group_id=None, peer_asn=None, auth_key=None, router_id=None,
                 status=None, keepalive=None, local_asn=None, hold=None, is_fake=None, route_limit=None, region_id=None,
                 ip_version=None):
        self.name = name
        self.description = description
        self.bgp_group_id = bgp_group_id
        self.peer_asn = peer_asn
        self.auth_key = auth_key
        self.router_id = router_id
        self.status = status
        self.keepalive = keepalive
        self.local_asn = local_asn
        self.hold = hold
        self.is_fake = is_fake
        self.route_limit = route_limit
        self.region_id = region_id
        self.ip_version = ip_version

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.bgp_group_id, 'bgp_group_id')
        self.validate_required(self.peer_asn, 'peer_asn')
        self.validate_required(self.auth_key, 'auth_key')
        self.validate_required(self.router_id, 'router_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.keepalive, 'keepalive')
        self.validate_required(self.local_asn, 'local_asn')
        self.validate_required(self.hold, 'hold')
        self.validate_required(self.is_fake, 'is_fake')
        self.validate_required(self.route_limit, 'route_limit')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ip_version, 'ip_version')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Description'] = self.description
        result['BgpGroupId'] = self.bgp_group_id
        result['PeerAsn'] = self.peer_asn
        result['AuthKey'] = self.auth_key
        result['RouterId'] = self.router_id
        result['Status'] = self.status
        result['Keepalive'] = self.keepalive
        result['LocalAsn'] = self.local_asn
        result['Hold'] = self.hold
        result['IsFake'] = self.is_fake
        result['RouteLimit'] = self.route_limit
        result['RegionId'] = self.region_id
        result['IpVersion'] = self.ip_version
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.bgp_group_id = map.get('BgpGroupId')
        self.peer_asn = map.get('PeerAsn')
        self.auth_key = map.get('AuthKey')
        self.router_id = map.get('RouterId')
        self.status = map.get('Status')
        self.keepalive = map.get('Keepalive')
        self.local_asn = map.get('LocalAsn')
        self.hold = map.get('Hold')
        self.is_fake = map.get('IsFake')
        self.route_limit = map.get('RouteLimit')
        self.region_id = map.get('RegionId')
        self.ip_version = map.get('IpVersion')
        return self


class DescribeBgpGroupsResponseBgpGroups(TeaModel):
    def __init__(self, bgp_group=None):
        self.bgp_group = bgp_group

    def validate(self):
        self.validate_required(self.bgp_group, 'bgp_group')
        if self.bgp_group:
            for k in self.bgp_group:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['BgpGroup'] = []
        if self.bgp_group is not None:
            for k in self.bgp_group:
                result['BgpGroup'].append(k.to_map() if k else None)
        else:
            result['BgpGroup'] = None
        return result

    def from_map(self, map={}):
        self.bgp_group = []
        if map.get('BgpGroup') is not None:
            for k in map.get('BgpGroup'):
                temp_model = DescribeBgpGroupsResponseBgpGroupsBgpGroup()
                self.bgp_group.append(temp_model.from_map(k))
        else:
            self.bgp_group = None
        return self


class DeleteBgpPeerRequest(TeaModel):
    def __init__(self, region_id=None, bgp_peer_id=None, client_token=None):
        self.region_id = region_id
        self.bgp_peer_id = bgp_peer_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bgp_peer_id, 'bgp_peer_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['BgpPeerId'] = self.bgp_peer_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.bgp_peer_id = map.get('BgpPeerId')
        self.client_token = map.get('ClientToken')
        return self


class DeleteBgpPeerResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteBgpNetworkRequest(TeaModel):
    def __init__(self, region_id=None, dst_cidr_block=None, router_id=None, client_token=None):
        self.region_id = region_id
        self.dst_cidr_block = dst_cidr_block
        self.router_id = router_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.dst_cidr_block, 'dst_cidr_block')
        self.validate_required(self.router_id, 'router_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DstCidrBlock'] = self.dst_cidr_block
        result['RouterId'] = self.router_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dst_cidr_block = map.get('DstCidrBlock')
        self.router_id = map.get('RouterId')
        self.client_token = map.get('ClientToken')
        return self


class DeleteBgpNetworkResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteBgpGroupRequest(TeaModel):
    def __init__(self, region_id=None, bgp_group_id=None, client_token=None):
        self.region_id = region_id
        self.bgp_group_id = bgp_group_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bgp_group_id, 'bgp_group_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['BgpGroupId'] = self.bgp_group_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.bgp_group_id = map.get('BgpGroupId')
        self.client_token = map.get('ClientToken')
        return self


class DeleteBgpGroupResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateBgpPeerRequest(TeaModel):
    def __init__(self, region_id=None, bgp_group_id=None, peer_ip_address=None, enable_bfd=None, client_token=None,
                 ip_version=None, bfd_multi_hop=None):
        self.region_id = region_id
        self.bgp_group_id = bgp_group_id
        self.peer_ip_address = peer_ip_address
        self.enable_bfd = enable_bfd
        self.client_token = client_token
        self.ip_version = ip_version
        self.bfd_multi_hop = bfd_multi_hop

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bgp_group_id, 'bgp_group_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['BgpGroupId'] = self.bgp_group_id
        result['PeerIpAddress'] = self.peer_ip_address
        result['EnableBfd'] = self.enable_bfd
        result['ClientToken'] = self.client_token
        result['IpVersion'] = self.ip_version
        result['BfdMultiHop'] = self.bfd_multi_hop
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.bgp_group_id = map.get('BgpGroupId')
        self.peer_ip_address = map.get('PeerIpAddress')
        self.enable_bfd = map.get('EnableBfd')
        self.client_token = map.get('ClientToken')
        self.ip_version = map.get('IpVersion')
        self.bfd_multi_hop = map.get('BfdMultiHop')
        return self


class CreateBgpPeerResponse(TeaModel):
    def __init__(self, request_id=None, bgp_peer_id=None):
        self.request_id = request_id
        self.bgp_peer_id = bgp_peer_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.bgp_peer_id, 'bgp_peer_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['BgpPeerId'] = self.bgp_peer_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.bgp_peer_id = map.get('BgpPeerId')
        return self


class CreateBgpGroupRequest(TeaModel):
    def __init__(self, region_id=None, router_id=None, name=None, description=None, local_asn=None, peer_asn=None,
                 auth_key=None, is_fake_asn=None, client_token=None, ip_version=None):
        self.region_id = region_id
        self.router_id = router_id
        self.name = name
        self.description = description
        self.local_asn = local_asn
        self.peer_asn = peer_asn
        self.auth_key = auth_key
        self.is_fake_asn = is_fake_asn
        self.client_token = client_token
        self.ip_version = ip_version

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.router_id, 'router_id')
        self.validate_required(self.peer_asn, 'peer_asn')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['RouterId'] = self.router_id
        result['Name'] = self.name
        result['Description'] = self.description
        result['LocalAsn'] = self.local_asn
        result['PeerAsn'] = self.peer_asn
        result['AuthKey'] = self.auth_key
        result['IsFakeAsn'] = self.is_fake_asn
        result['ClientToken'] = self.client_token
        result['IpVersion'] = self.ip_version
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.router_id = map.get('RouterId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.local_asn = map.get('LocalAsn')
        self.peer_asn = map.get('PeerAsn')
        self.auth_key = map.get('AuthKey')
        self.is_fake_asn = map.get('IsFakeAsn')
        self.client_token = map.get('ClientToken')
        self.ip_version = map.get('IpVersion')
        return self


class CreateBgpGroupResponse(TeaModel):
    def __init__(self, request_id=None, bgp_group_id=None):
        self.request_id = request_id
        self.bgp_group_id = bgp_group_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.bgp_group_id, 'bgp_group_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['BgpGroupId'] = self.bgp_group_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.bgp_group_id = map.get('BgpGroupId')
        return self


class AddBgpNetworkRequest(TeaModel):
    def __init__(self, region_id=None, dst_cidr_block=None, vpc_id=None, router_id=None, client_token=None):
        self.region_id = region_id
        self.dst_cidr_block = dst_cidr_block
        self.vpc_id = vpc_id
        self.router_id = router_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.dst_cidr_block, 'dst_cidr_block')
        self.validate_required(self.router_id, 'router_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DstCidrBlock'] = self.dst_cidr_block
        result['VpcId'] = self.vpc_id
        result['RouterId'] = self.router_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dst_cidr_block = map.get('DstCidrBlock')
        self.vpc_id = map.get('VpcId')
        self.router_id = map.get('RouterId')
        self.client_token = map.get('ClientToken')
        return self


class AddBgpNetworkResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class EnableVpcClassicLinkRequest(TeaModel):
    def __init__(self, region_id=None, vpc_id=None, client_token=None):
        self.region_id = region_id
        self.vpc_id = vpc_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpc_id, 'vpc_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VpcId'] = self.vpc_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vpc_id = map.get('VpcId')
        self.client_token = map.get('ClientToken')
        return self


class EnableVpcClassicLinkResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DisableVpcClassicLinkRequest(TeaModel):
    def __init__(self, region_id=None, vpc_id=None, client_token=None):
        self.region_id = region_id
        self.vpc_id = vpc_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpc_id, 'vpc_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VpcId'] = self.vpc_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vpc_id = map.get('VpcId')
        self.client_token = map.get('ClientToken')
        return self


class DisableVpcClassicLinkResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeVpcAttributeRequest(TeaModel):
    def __init__(self, vpc_id=None, region_id=None, dry_run=None, is_default=None):
        self.vpc_id = vpc_id
        self.region_id = region_id
        self.dry_run = dry_run
        self.is_default = is_default

    def validate(self):
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['VpcId'] = self.vpc_id
        result['RegionId'] = self.region_id
        result['DryRun'] = self.dry_run
        result['IsDefault'] = self.is_default
        return result

    def from_map(self, map={}):
        self.vpc_id = map.get('VpcId')
        self.region_id = map.get('RegionId')
        self.dry_run = map.get('DryRun')
        self.is_default = map.get('IsDefault')
        return self


class DescribeVpcAttributeResponse(TeaModel):
    def __init__(self, request_id=None, vpc_id=None, region_id=None, status=None, vpc_name=None, creation_time=None,
                 cidr_block=None, ipv_6cidr_block=None, vrouter_id=None, description=None, is_default=None,
                 classic_link_enabled=None, resource_group_id=None, network_acl_num=None, owner_id=None, dhcp_options_set_id=None,
                 dhcp_options_set_status=None, associated_cens=None, cloud_resources=None, v_switch_ids=None, user_cidrs=None,
                 secondary_cidr_blocks=None):
        self.request_id = request_id
        self.vpc_id = vpc_id
        self.region_id = region_id
        self.status = status
        self.vpc_name = vpc_name
        self.creation_time = creation_time
        self.cidr_block = cidr_block
        self.ipv_6cidr_block = ipv_6cidr_block
        self.vrouter_id = vrouter_id
        self.description = description
        self.is_default = is_default
        self.classic_link_enabled = classic_link_enabled
        self.resource_group_id = resource_group_id
        self.network_acl_num = network_acl_num
        self.owner_id = owner_id
        self.dhcp_options_set_id = dhcp_options_set_id
        self.dhcp_options_set_status = dhcp_options_set_status
        self.associated_cens = associated_cens  # type: DescribeVpcAttributeResponseAssociatedCens
        self.cloud_resources = cloud_resources  # type: DescribeVpcAttributeResponseCloudResources
        self.v_switch_ids = v_switch_ids  # type: DescribeVpcAttributeResponseVSwitchIds
        self.user_cidrs = user_cidrs  # type: DescribeVpcAttributeResponseUserCidrs
        self.secondary_cidr_blocks = secondary_cidr_blocks  # type: DescribeVpcAttributeResponseSecondaryCidrBlocks

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.vpc_name, 'vpc_name')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.cidr_block, 'cidr_block')
        self.validate_required(self.ipv_6cidr_block, 'ipv_6cidr_block')
        self.validate_required(self.vrouter_id, 'vrouter_id')
        self.validate_required(self.description, 'description')
        self.validate_required(self.is_default, 'is_default')
        self.validate_required(self.classic_link_enabled, 'classic_link_enabled')
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.network_acl_num, 'network_acl_num')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.dhcp_options_set_id, 'dhcp_options_set_id')
        self.validate_required(self.dhcp_options_set_status, 'dhcp_options_set_status')
        self.validate_required(self.associated_cens, 'associated_cens')
        if self.associated_cens:
            self.associated_cens.validate()
        self.validate_required(self.cloud_resources, 'cloud_resources')
        if self.cloud_resources:
            self.cloud_resources.validate()
        self.validate_required(self.v_switch_ids, 'v_switch_ids')
        if self.v_switch_ids:
            self.v_switch_ids.validate()
        self.validate_required(self.user_cidrs, 'user_cidrs')
        if self.user_cidrs:
            self.user_cidrs.validate()
        self.validate_required(self.secondary_cidr_blocks, 'secondary_cidr_blocks')
        if self.secondary_cidr_blocks:
            self.secondary_cidr_blocks.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['VpcId'] = self.vpc_id
        result['RegionId'] = self.region_id
        result['Status'] = self.status
        result['VpcName'] = self.vpc_name
        result['CreationTime'] = self.creation_time
        result['CidrBlock'] = self.cidr_block
        result['Ipv6CidrBlock'] = self.ipv_6cidr_block
        result['VRouterId'] = self.vrouter_id
        result['Description'] = self.description
        result['IsDefault'] = self.is_default
        result['ClassicLinkEnabled'] = self.classic_link_enabled
        result['ResourceGroupId'] = self.resource_group_id
        result['NetworkAclNum'] = self.network_acl_num
        result['OwnerId'] = self.owner_id
        result['DhcpOptionsSetId'] = self.dhcp_options_set_id
        result['DhcpOptionsSetStatus'] = self.dhcp_options_set_status
        if self.associated_cens is not None:
            result['AssociatedCens'] = self.associated_cens.to_map()
        else:
            result['AssociatedCens'] = None
        if self.cloud_resources is not None:
            result['CloudResources'] = self.cloud_resources.to_map()
        else:
            result['CloudResources'] = None
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids.to_map()
        else:
            result['VSwitchIds'] = None
        if self.user_cidrs is not None:
            result['UserCidrs'] = self.user_cidrs.to_map()
        else:
            result['UserCidrs'] = None
        if self.secondary_cidr_blocks is not None:
            result['SecondaryCidrBlocks'] = self.secondary_cidr_blocks.to_map()
        else:
            result['SecondaryCidrBlocks'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.vpc_id = map.get('VpcId')
        self.region_id = map.get('RegionId')
        self.status = map.get('Status')
        self.vpc_name = map.get('VpcName')
        self.creation_time = map.get('CreationTime')
        self.cidr_block = map.get('CidrBlock')
        self.ipv_6cidr_block = map.get('Ipv6CidrBlock')
        self.vrouter_id = map.get('VRouterId')
        self.description = map.get('Description')
        self.is_default = map.get('IsDefault')
        self.classic_link_enabled = map.get('ClassicLinkEnabled')
        self.resource_group_id = map.get('ResourceGroupId')
        self.network_acl_num = map.get('NetworkAclNum')
        self.owner_id = map.get('OwnerId')
        self.dhcp_options_set_id = map.get('DhcpOptionsSetId')
        self.dhcp_options_set_status = map.get('DhcpOptionsSetStatus')
        if map.get('AssociatedCens') is not None:
            temp_model = DescribeVpcAttributeResponseAssociatedCens()
            self.associated_cens = temp_model.from_map(map['AssociatedCens'])
        else:
            self.associated_cens = None
        if map.get('CloudResources') is not None:
            temp_model = DescribeVpcAttributeResponseCloudResources()
            self.cloud_resources = temp_model.from_map(map['CloudResources'])
        else:
            self.cloud_resources = None
        if map.get('VSwitchIds') is not None:
            temp_model = DescribeVpcAttributeResponseVSwitchIds()
            self.v_switch_ids = temp_model.from_map(map['VSwitchIds'])
        else:
            self.v_switch_ids = None
        if map.get('UserCidrs') is not None:
            temp_model = DescribeVpcAttributeResponseUserCidrs()
            self.user_cidrs = temp_model.from_map(map['UserCidrs'])
        else:
            self.user_cidrs = None
        if map.get('SecondaryCidrBlocks') is not None:
            temp_model = DescribeVpcAttributeResponseSecondaryCidrBlocks()
            self.secondary_cidr_blocks = temp_model.from_map(map['SecondaryCidrBlocks'])
        else:
            self.secondary_cidr_blocks = None
        return self


class DescribeVpcAttributeResponseAssociatedCensAssociatedCen(TeaModel):
    def __init__(self, cen_id=None, cen_owner_id=None, cen_status=None):
        self.cen_id = cen_id
        self.cen_owner_id = cen_owner_id
        self.cen_status = cen_status

    def validate(self):
        self.validate_required(self.cen_id, 'cen_id')
        self.validate_required(self.cen_owner_id, 'cen_owner_id')
        self.validate_required(self.cen_status, 'cen_status')

    def to_map(self):
        result = {}
        result['CenId'] = self.cen_id
        result['CenOwnerId'] = self.cen_owner_id
        result['CenStatus'] = self.cen_status
        return result

    def from_map(self, map={}):
        self.cen_id = map.get('CenId')
        self.cen_owner_id = map.get('CenOwnerId')
        self.cen_status = map.get('CenStatus')
        return self


class DescribeVpcAttributeResponseAssociatedCens(TeaModel):
    def __init__(self, associated_cen=None):
        self.associated_cen = associated_cen

    def validate(self):
        self.validate_required(self.associated_cen, 'associated_cen')
        if self.associated_cen:
            for k in self.associated_cen:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['AssociatedCen'] = []
        if self.associated_cen is not None:
            for k in self.associated_cen:
                result['AssociatedCen'].append(k.to_map() if k else None)
        else:
            result['AssociatedCen'] = None
        return result

    def from_map(self, map={}):
        self.associated_cen = []
        if map.get('AssociatedCen') is not None:
            for k in map.get('AssociatedCen'):
                temp_model = DescribeVpcAttributeResponseAssociatedCensAssociatedCen()
                self.associated_cen.append(temp_model.from_map(k))
        else:
            self.associated_cen = None
        return self


class DescribeVpcAttributeResponseCloudResourcesCloudResourceSetType(TeaModel):
    def __init__(self, resource_type=None, resource_count=None):
        self.resource_type = resource_type
        self.resource_count = resource_count

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_count, 'resource_count')

    def to_map(self):
        result = {}
        result['ResourceType'] = self.resource_type
        result['ResourceCount'] = self.resource_count
        return result

    def from_map(self, map={}):
        self.resource_type = map.get('ResourceType')
        self.resource_count = map.get('ResourceCount')
        return self


class DescribeVpcAttributeResponseCloudResources(TeaModel):
    def __init__(self, cloud_resource_set_type=None):
        self.cloud_resource_set_type = cloud_resource_set_type

    def validate(self):
        self.validate_required(self.cloud_resource_set_type, 'cloud_resource_set_type')
        if self.cloud_resource_set_type:
            for k in self.cloud_resource_set_type:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['CloudResourceSetType'] = []
        if self.cloud_resource_set_type is not None:
            for k in self.cloud_resource_set_type:
                result['CloudResourceSetType'].append(k.to_map() if k else None)
        else:
            result['CloudResourceSetType'] = None
        return result

    def from_map(self, map={}):
        self.cloud_resource_set_type = []
        if map.get('CloudResourceSetType') is not None:
            for k in map.get('CloudResourceSetType'):
                temp_model = DescribeVpcAttributeResponseCloudResourcesCloudResourceSetType()
                self.cloud_resource_set_type.append(temp_model.from_map(k))
        else:
            self.cloud_resource_set_type = None
        return self


class DescribeVpcAttributeResponseVSwitchIds(TeaModel):
    def __init__(self, v_switch_id=None):
        self.v_switch_id = v_switch_id

    def validate(self):
        self.validate_required(self.v_switch_id, 'v_switch_id')

    def to_map(self):
        result = {}
        result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, map={}):
        self.v_switch_id = map.get('VSwitchId')
        return self


class DescribeVpcAttributeResponseUserCidrs(TeaModel):
    def __init__(self, user_cidr=None):
        self.user_cidr = user_cidr

    def validate(self):
        self.validate_required(self.user_cidr, 'user_cidr')

    def to_map(self):
        result = {}
        result['UserCidr'] = self.user_cidr
        return result

    def from_map(self, map={}):
        self.user_cidr = map.get('UserCidr')
        return self


class DescribeVpcAttributeResponseSecondaryCidrBlocks(TeaModel):
    def __init__(self, secondary_cidr_block=None):
        self.secondary_cidr_block = secondary_cidr_block

    def validate(self):
        self.validate_required(self.secondary_cidr_block, 'secondary_cidr_block')

    def to_map(self):
        result = {}
        result['SecondaryCidrBlock'] = self.secondary_cidr_block
        return result

    def from_map(self, map={}):
        self.secondary_cidr_block = map.get('SecondaryCidrBlock')
        return self


class UnassociatePhysicalConnectionFromVirtualBorderRouterRequest(TeaModel):
    def __init__(self, region_id=None, vbr_id=None, physical_connection_id=None, client_token=None):
        self.region_id = region_id
        self.vbr_id = vbr_id
        self.physical_connection_id = physical_connection_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vbr_id, 'vbr_id')
        self.validate_required(self.physical_connection_id, 'physical_connection_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VbrId'] = self.vbr_id
        result['PhysicalConnectionId'] = self.physical_connection_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vbr_id = map.get('VbrId')
        self.physical_connection_id = map.get('PhysicalConnectionId')
        self.client_token = map.get('ClientToken')
        return self


class UnassociatePhysicalConnectionFromVirtualBorderRouterResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AssociatePhysicalConnectionToVirtualBorderRouterRequest(TeaModel):
    def __init__(self, region_id=None, vbr_id=None, physical_connection_id=None, vlan_id=None, circuit_code=None,
                 local_gateway_ip=None, peer_gateway_ip=None, peering_subnet_mask=None, client_token=None,
                 local_ipv_6gateway_ip=None, peer_ipv_6gateway_ip=None, peering_ipv_6subnet_mask=None, enable_ipv_6=None):
        self.region_id = region_id
        self.vbr_id = vbr_id
        self.physical_connection_id = physical_connection_id
        self.vlan_id = vlan_id
        self.circuit_code = circuit_code
        self.local_gateway_ip = local_gateway_ip
        self.peer_gateway_ip = peer_gateway_ip
        self.peering_subnet_mask = peering_subnet_mask
        self.client_token = client_token
        self.local_ipv_6gateway_ip = local_ipv_6gateway_ip
        self.peer_ipv_6gateway_ip = peer_ipv_6gateway_ip
        self.peering_ipv_6subnet_mask = peering_ipv_6subnet_mask
        self.enable_ipv_6 = enable_ipv_6

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vbr_id, 'vbr_id')
        self.validate_required(self.physical_connection_id, 'physical_connection_id')
        self.validate_required(self.vlan_id, 'vlan_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VbrId'] = self.vbr_id
        result['PhysicalConnectionId'] = self.physical_connection_id
        result['VlanId'] = self.vlan_id
        result['CircuitCode'] = self.circuit_code
        result['LocalGatewayIp'] = self.local_gateway_ip
        result['PeerGatewayIp'] = self.peer_gateway_ip
        result['PeeringSubnetMask'] = self.peering_subnet_mask
        result['ClientToken'] = self.client_token
        result['LocalIpv6GatewayIp'] = self.local_ipv_6gateway_ip
        result['PeerIpv6GatewayIp'] = self.peer_ipv_6gateway_ip
        result['PeeringIpv6SubnetMask'] = self.peering_ipv_6subnet_mask
        result['EnableIpv6'] = self.enable_ipv_6
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vbr_id = map.get('VbrId')
        self.physical_connection_id = map.get('PhysicalConnectionId')
        self.vlan_id = map.get('VlanId')
        self.circuit_code = map.get('CircuitCode')
        self.local_gateway_ip = map.get('LocalGatewayIp')
        self.peer_gateway_ip = map.get('PeerGatewayIp')
        self.peering_subnet_mask = map.get('PeeringSubnetMask')
        self.client_token = map.get('ClientToken')
        self.local_ipv_6gateway_ip = map.get('LocalIpv6GatewayIp')
        self.peer_ipv_6gateway_ip = map.get('PeerIpv6GatewayIp')
        self.peering_ipv_6subnet_mask = map.get('PeeringIpv6SubnetMask')
        self.enable_ipv_6 = map.get('EnableIpv6')
        return self


class AssociatePhysicalConnectionToVirtualBorderRouterResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifySnatEntryRequest(TeaModel):
    def __init__(self, region_id=None, snat_table_id=None, snat_entry_id=None, snat_ip=None, snat_entry_name=None,
                 client_token=None):
        self.region_id = region_id
        self.snat_table_id = snat_table_id
        self.snat_entry_id = snat_entry_id
        self.snat_ip = snat_ip
        self.snat_entry_name = snat_entry_name
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.snat_table_id, 'snat_table_id')
        self.validate_required(self.snat_entry_id, 'snat_entry_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['SnatTableId'] = self.snat_table_id
        result['SnatEntryId'] = self.snat_entry_id
        result['SnatIp'] = self.snat_ip
        result['SnatEntryName'] = self.snat_entry_name
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.snat_table_id = map.get('SnatTableId')
        self.snat_entry_id = map.get('SnatEntryId')
        self.snat_ip = map.get('SnatIp')
        self.snat_entry_name = map.get('SnatEntryName')
        self.client_token = map.get('ClientToken')
        return self


class ModifySnatEntryResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyNatGatewaySpecRequest(TeaModel):
    def __init__(self, region_id=None, nat_gateway_id=None, spec=None, auto_pay=None, client_token=None):
        self.region_id = region_id
        self.nat_gateway_id = nat_gateway_id
        self.spec = spec
        self.auto_pay = auto_pay
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.nat_gateway_id, 'nat_gateway_id')
        self.validate_required(self.spec, 'spec')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['NatGatewayId'] = self.nat_gateway_id
        result['Spec'] = self.spec
        result['AutoPay'] = self.auto_pay
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.nat_gateway_id = map.get('NatGatewayId')
        self.spec = map.get('Spec')
        self.auto_pay = map.get('AutoPay')
        self.client_token = map.get('ClientToken')
        return self


class ModifyNatGatewaySpecResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyNatGatewayAttributeRequest(TeaModel):
    def __init__(self, region_id=None, nat_gateway_id=None, name=None, description=None):
        self.region_id = region_id
        self.nat_gateway_id = nat_gateway_id
        self.name = name
        self.description = description

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.nat_gateway_id, 'nat_gateway_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['NatGatewayId'] = self.nat_gateway_id
        result['Name'] = self.name
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.nat_gateway_id = map.get('NatGatewayId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        return self


class ModifyNatGatewayAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyBandwidthPackageAttributeRequest(TeaModel):
    def __init__(self, region_id=None, bandwidth_package_id=None, name=None, description=None):
        self.region_id = region_id
        self.bandwidth_package_id = bandwidth_package_id
        self.name = name
        self.description = description

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bandwidth_package_id, 'bandwidth_package_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['BandwidthPackageId'] = self.bandwidth_package_id
        result['Name'] = self.name
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        return self


class ModifyBandwidthPackageAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeSnatTableEntriesRequest(TeaModel):
    def __init__(self, region_id=None, snat_table_id=None, snat_entry_id=None, source_vswitch_id=None,
                 source_cidr=None, snat_ip=None, snat_entry_name=None, page_number=None, page_size=None):
        self.region_id = region_id
        self.snat_table_id = snat_table_id
        self.snat_entry_id = snat_entry_id
        self.source_vswitch_id = source_vswitch_id
        self.source_cidr = source_cidr
        self.snat_ip = snat_ip
        self.snat_entry_name = snat_entry_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.snat_table_id, 'snat_table_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['SnatTableId'] = self.snat_table_id
        result['SnatEntryId'] = self.snat_entry_id
        result['SourceVSwitchId'] = self.source_vswitch_id
        result['SourceCIDR'] = self.source_cidr
        result['SnatIp'] = self.snat_ip
        result['SnatEntryName'] = self.snat_entry_name
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.snat_table_id = map.get('SnatTableId')
        self.snat_entry_id = map.get('SnatEntryId')
        self.source_vswitch_id = map.get('SourceVSwitchId')
        self.source_cidr = map.get('SourceCIDR')
        self.snat_ip = map.get('SnatIp')
        self.snat_entry_name = map.get('SnatEntryName')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeSnatTableEntriesResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, snat_table_entries=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.snat_table_entries = snat_table_entries  # type: DescribeSnatTableEntriesResponseSnatTableEntries

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.snat_table_entries, 'snat_table_entries')
        if self.snat_table_entries:
            self.snat_table_entries.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.snat_table_entries is not None:
            result['SnatTableEntries'] = self.snat_table_entries.to_map()
        else:
            result['SnatTableEntries'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('SnatTableEntries') is not None:
            temp_model = DescribeSnatTableEntriesResponseSnatTableEntries()
            self.snat_table_entries = temp_model.from_map(map['SnatTableEntries'])
        else:
            self.snat_table_entries = None
        return self


class DescribeSnatTableEntriesResponseSnatTableEntriesSnatTableEntry(TeaModel):
    def __init__(self, snat_table_id=None, snat_entry_id=None, source_vswitch_id=None, source_cidr=None,
                 snat_ip=None, status=None, snat_entry_name=None):
        self.snat_table_id = snat_table_id
        self.snat_entry_id = snat_entry_id
        self.source_vswitch_id = source_vswitch_id
        self.source_cidr = source_cidr
        self.snat_ip = snat_ip
        self.status = status
        self.snat_entry_name = snat_entry_name

    def validate(self):
        self.validate_required(self.snat_table_id, 'snat_table_id')
        self.validate_required(self.snat_entry_id, 'snat_entry_id')
        self.validate_required(self.source_vswitch_id, 'source_vswitch_id')
        self.validate_required(self.source_cidr, 'source_cidr')
        self.validate_required(self.snat_ip, 'snat_ip')
        self.validate_required(self.status, 'status')
        self.validate_required(self.snat_entry_name, 'snat_entry_name')

    def to_map(self):
        result = {}
        result['SnatTableId'] = self.snat_table_id
        result['SnatEntryId'] = self.snat_entry_id
        result['SourceVSwitchId'] = self.source_vswitch_id
        result['SourceCIDR'] = self.source_cidr
        result['SnatIp'] = self.snat_ip
        result['Status'] = self.status
        result['SnatEntryName'] = self.snat_entry_name
        return result

    def from_map(self, map={}):
        self.snat_table_id = map.get('SnatTableId')
        self.snat_entry_id = map.get('SnatEntryId')
        self.source_vswitch_id = map.get('SourceVSwitchId')
        self.source_cidr = map.get('SourceCIDR')
        self.snat_ip = map.get('SnatIp')
        self.status = map.get('Status')
        self.snat_entry_name = map.get('SnatEntryName')
        return self


class DescribeSnatTableEntriesResponseSnatTableEntries(TeaModel):
    def __init__(self, snat_table_entry=None):
        self.snat_table_entry = snat_table_entry

    def validate(self):
        self.validate_required(self.snat_table_entry, 'snat_table_entry')
        if self.snat_table_entry:
            for k in self.snat_table_entry:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['SnatTableEntry'] = []
        if self.snat_table_entry is not None:
            for k in self.snat_table_entry:
                result['SnatTableEntry'].append(k.to_map() if k else None)
        else:
            result['SnatTableEntry'] = None
        return result

    def from_map(self, map={}):
        self.snat_table_entry = []
        if map.get('SnatTableEntry') is not None:
            for k in map.get('SnatTableEntry'):
                temp_model = DescribeSnatTableEntriesResponseSnatTableEntriesSnatTableEntry()
                self.snat_table_entry.append(temp_model.from_map(k))
        else:
            self.snat_table_entry = None
        return self


class DeleteSnatEntryRequest(TeaModel):
    def __init__(self, region_id=None, snat_table_id=None, snat_entry_id=None, client_token=None):
        self.region_id = region_id
        self.snat_table_id = snat_table_id
        self.snat_entry_id = snat_entry_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.snat_table_id, 'snat_table_id')
        self.validate_required(self.snat_entry_id, 'snat_entry_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['SnatTableId'] = self.snat_table_id
        result['SnatEntryId'] = self.snat_entry_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.snat_table_id = map.get('SnatTableId')
        self.snat_entry_id = map.get('SnatEntryId')
        self.client_token = map.get('ClientToken')
        return self


class DeleteSnatEntryResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateSnatEntryRequest(TeaModel):
    def __init__(self, region_id=None, snat_table_id=None, source_vswitch_id=None, source_cidr=None, snat_ip=None,
                 snat_entry_name=None, client_token=None):
        self.region_id = region_id
        self.snat_table_id = snat_table_id
        self.source_vswitch_id = source_vswitch_id
        self.source_cidr = source_cidr
        self.snat_ip = snat_ip
        self.snat_entry_name = snat_entry_name
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.snat_table_id, 'snat_table_id')
        self.validate_required(self.snat_ip, 'snat_ip')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['SnatTableId'] = self.snat_table_id
        result['SourceVSwitchId'] = self.source_vswitch_id
        result['SourceCIDR'] = self.source_cidr
        result['SnatIp'] = self.snat_ip
        result['SnatEntryName'] = self.snat_entry_name
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.snat_table_id = map.get('SnatTableId')
        self.source_vswitch_id = map.get('SourceVSwitchId')
        self.source_cidr = map.get('SourceCIDR')
        self.snat_ip = map.get('SnatIp')
        self.snat_entry_name = map.get('SnatEntryName')
        self.client_token = map.get('ClientToken')
        return self


class CreateSnatEntryResponse(TeaModel):
    def __init__(self, request_id=None, snat_entry_id=None):
        self.request_id = request_id
        self.snat_entry_id = snat_entry_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.snat_entry_id, 'snat_entry_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['SnatEntryId'] = self.snat_entry_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.snat_entry_id = map.get('SnatEntryId')
        return self


class CreateBandwidthPackageRequest(TeaModel):
    def __init__(self, region_id=None, nat_gateway_id=None, name=None, description=None, client_token=None,
                 ip_count=None, bandwidth=None, isp=None, zone=None, internet_charge_type=None):
        self.region_id = region_id
        self.nat_gateway_id = nat_gateway_id
        self.name = name
        self.description = description
        self.client_token = client_token
        self.ip_count = ip_count
        self.bandwidth = bandwidth
        self.isp = isp
        self.zone = zone
        self.internet_charge_type = internet_charge_type

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.nat_gateway_id, 'nat_gateway_id')
        self.validate_required(self.ip_count, 'ip_count')
        self.validate_required(self.bandwidth, 'bandwidth')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['NatGatewayId'] = self.nat_gateway_id
        result['Name'] = self.name
        result['Description'] = self.description
        result['ClientToken'] = self.client_token
        result['IpCount'] = self.ip_count
        result['Bandwidth'] = self.bandwidth
        result['ISP'] = self.isp
        result['Zone'] = self.zone
        result['InternetChargeType'] = self.internet_charge_type
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.nat_gateway_id = map.get('NatGatewayId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.client_token = map.get('ClientToken')
        self.ip_count = map.get('IpCount')
        self.bandwidth = map.get('Bandwidth')
        self.isp = map.get('ISP')
        self.zone = map.get('Zone')
        self.internet_charge_type = map.get('InternetChargeType')
        return self


class CreateBandwidthPackageResponse(TeaModel):
    def __init__(self, request_id=None, bandwidth_package_id=None):
        self.request_id = request_id
        self.bandwidth_package_id = bandwidth_package_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.bandwidth_package_id, 'bandwidth_package_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['BandwidthPackageId'] = self.bandwidth_package_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        return self


class UnassociateHaVipRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, ha_vip_id=None, instance_id=None, force=None):
        self.client_token = client_token
        self.region_id = region_id
        self.ha_vip_id = ha_vip_id
        self.instance_id = instance_id
        self.force = force

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ha_vip_id, 'ha_vip_id')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['HaVipId'] = self.ha_vip_id
        result['InstanceId'] = self.instance_id
        result['Force'] = self.force
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.ha_vip_id = map.get('HaVipId')
        self.instance_id = map.get('InstanceId')
        self.force = map.get('Force')
        return self


class UnassociateHaVipResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class UnassociateEipAddressRequest(TeaModel):
    def __init__(self, force=None, region_id=None, allocation_id=None, instance_id=None, instance_type=None,
                 private_ip_address=None, client_token=None):
        self.force = force
        self.region_id = region_id
        self.allocation_id = allocation_id
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.private_ip_address = private_ip_address
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.allocation_id, 'allocation_id')

    def to_map(self):
        result = {}
        result['Force'] = self.force
        result['RegionId'] = self.region_id
        result['AllocationId'] = self.allocation_id
        result['InstanceId'] = self.instance_id
        result['InstanceType'] = self.instance_type
        result['PrivateIpAddress'] = self.private_ip_address
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.force = map.get('Force')
        self.region_id = map.get('RegionId')
        self.allocation_id = map.get('AllocationId')
        self.instance_id = map.get('InstanceId')
        self.instance_type = map.get('InstanceType')
        self.private_ip_address = map.get('PrivateIpAddress')
        self.client_token = map.get('ClientToken')
        return self


class UnassociateEipAddressResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class TerminateVirtualBorderRouterRequest(TeaModel):
    def __init__(self, region_id=None, vbr_id=None, client_token=None):
        self.region_id = region_id
        self.vbr_id = vbr_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vbr_id, 'vbr_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VbrId'] = self.vbr_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vbr_id = map.get('VbrId')
        self.client_token = map.get('ClientToken')
        return self


class TerminateVirtualBorderRouterResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class TerminatePhysicalConnectionRequest(TeaModel):
    def __init__(self, region_id=None, physical_connection_id=None, client_token=None):
        self.region_id = region_id
        self.physical_connection_id = physical_connection_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.physical_connection_id, 'physical_connection_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['PhysicalConnectionId'] = self.physical_connection_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.physical_connection_id = map.get('PhysicalConnectionId')
        self.client_token = map.get('ClientToken')
        return self


class TerminatePhysicalConnectionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class RemoveBandwidthPackageIpsRequest(TeaModel):
    def __init__(self, region_id=None, bandwidth_package_id=None, client_token=None, removed_ip_addresses=None):
        self.region_id = region_id
        self.bandwidth_package_id = bandwidth_package_id
        self.client_token = client_token
        self.removed_ip_addresses = removed_ip_addresses

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bandwidth_package_id, 'bandwidth_package_id')
        self.validate_required(self.removed_ip_addresses, 'removed_ip_addresses')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['BandwidthPackageId'] = self.bandwidth_package_id
        result['ClientToken'] = self.client_token
        result['RemovedIpAddresses'] = self.removed_ip_addresses
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        self.client_token = map.get('ClientToken')
        self.removed_ip_addresses = map.get('RemovedIpAddresses')
        return self


class RemoveBandwidthPackageIpsResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ReleaseEipAddressRequest(TeaModel):
    def __init__(self, region_id=None, allocation_id=None):
        self.region_id = region_id
        self.allocation_id = allocation_id

    def validate(self):
        self.validate_required(self.allocation_id, 'allocation_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['AllocationId'] = self.allocation_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.allocation_id = map.get('AllocationId')
        return self


class ReleaseEipAddressResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class RecoverVirtualBorderRouterRequest(TeaModel):
    def __init__(self, region_id=None, vbr_id=None, client_token=None):
        self.region_id = region_id
        self.vbr_id = vbr_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vbr_id, 'vbr_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VbrId'] = self.vbr_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vbr_id = map.get('VbrId')
        self.client_token = map.get('ClientToken')
        return self


class RecoverVirtualBorderRouterResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyVSwitchAttributeRequest(TeaModel):
    def __init__(self, v_switch_id=None, v_switch_name=None, region_id=None, description=None, ipv_6cidr_block=None):
        self.v_switch_id = v_switch_id
        self.v_switch_name = v_switch_name
        self.region_id = region_id
        self.description = description
        self.ipv_6cidr_block = ipv_6cidr_block

    def validate(self):
        self.validate_required(self.v_switch_id, 'v_switch_id')

    def to_map(self):
        result = {}
        result['VSwitchId'] = self.v_switch_id
        result['VSwitchName'] = self.v_switch_name
        result['RegionId'] = self.region_id
        result['Description'] = self.description
        result['Ipv6CidrBlock'] = self.ipv_6cidr_block
        return result

    def from_map(self, map={}):
        self.v_switch_id = map.get('VSwitchId')
        self.v_switch_name = map.get('VSwitchName')
        self.region_id = map.get('RegionId')
        self.description = map.get('Description')
        self.ipv_6cidr_block = map.get('Ipv6CidrBlock')
        return self


class ModifyVSwitchAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyVRouterAttributeRequest(TeaModel):
    def __init__(self, region_id=None, vrouter_id=None, vrouter_name=None, description=None):
        self.region_id = region_id
        self.vrouter_id = vrouter_id
        self.vrouter_name = vrouter_name
        self.description = description

    def validate(self):
        self.validate_required(self.vrouter_id, 'vrouter_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VRouterId'] = self.vrouter_id
        result['VRouterName'] = self.vrouter_name
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vrouter_id = map.get('VRouterId')
        self.vrouter_name = map.get('VRouterName')
        self.description = map.get('Description')
        return self


class ModifyVRouterAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyVpcAttributeRequest(TeaModel):
    def __init__(self, vpc_id=None, description=None, vpc_name=None, cidr_block=None, region_id=None,
                 enable_ipv_6=None, ipv_6cidr_block=None):
        self.vpc_id = vpc_id
        self.description = description
        self.vpc_name = vpc_name
        self.cidr_block = cidr_block
        self.region_id = region_id
        self.enable_ipv_6 = enable_ipv_6
        self.ipv_6cidr_block = ipv_6cidr_block

    def validate(self):
        self.validate_required(self.vpc_id, 'vpc_id')

    def to_map(self):
        result = {}
        result['VpcId'] = self.vpc_id
        result['Description'] = self.description
        result['VpcName'] = self.vpc_name
        result['CidrBlock'] = self.cidr_block
        result['RegionId'] = self.region_id
        result['EnableIPv6'] = self.enable_ipv_6
        result['Ipv6CidrBlock'] = self.ipv_6cidr_block
        return result

    def from_map(self, map={}):
        self.vpc_id = map.get('VpcId')
        self.description = map.get('Description')
        self.vpc_name = map.get('VpcName')
        self.cidr_block = map.get('CidrBlock')
        self.region_id = map.get('RegionId')
        self.enable_ipv_6 = map.get('EnableIPv6')
        self.ipv_6cidr_block = map.get('Ipv6CidrBlock')
        return self


class ModifyVpcAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyVirtualBorderRouterAttributeRequest(TeaModel):
    def __init__(self, region_id=None, vbr_id=None, vlan_id=None, circuit_code=None, local_gateway_ip=None,
                 peer_gateway_ip=None, peering_subnet_mask=None, min_tx_interval=None, min_rx_interval=None,
                 detect_multiplier=None, description=None, name=None, associated_physical_connections=None, client_token=None,
                 local_ipv_6gateway_ip=None, peer_ipv_6gateway_ip=None, peering_ipv_6subnet_mask=None, enable_ipv_6=None):
        self.region_id = region_id
        self.vbr_id = vbr_id
        self.vlan_id = vlan_id
        self.circuit_code = circuit_code
        self.local_gateway_ip = local_gateway_ip
        self.peer_gateway_ip = peer_gateway_ip
        self.peering_subnet_mask = peering_subnet_mask
        self.min_tx_interval = min_tx_interval
        self.min_rx_interval = min_rx_interval
        self.detect_multiplier = detect_multiplier
        self.description = description
        self.name = name
        self.associated_physical_connections = associated_physical_connections
        self.client_token = client_token
        self.local_ipv_6gateway_ip = local_ipv_6gateway_ip
        self.peer_ipv_6gateway_ip = peer_ipv_6gateway_ip
        self.peering_ipv_6subnet_mask = peering_ipv_6subnet_mask
        self.enable_ipv_6 = enable_ipv_6

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vbr_id, 'vbr_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VbrId'] = self.vbr_id
        result['VlanId'] = self.vlan_id
        result['CircuitCode'] = self.circuit_code
        result['LocalGatewayIp'] = self.local_gateway_ip
        result['PeerGatewayIp'] = self.peer_gateway_ip
        result['PeeringSubnetMask'] = self.peering_subnet_mask
        result['MinTxInterval'] = self.min_tx_interval
        result['MinRxInterval'] = self.min_rx_interval
        result['DetectMultiplier'] = self.detect_multiplier
        result['Description'] = self.description
        result['Name'] = self.name
        result['AssociatedPhysicalConnections'] = self.associated_physical_connections
        result['ClientToken'] = self.client_token
        result['LocalIpv6GatewayIp'] = self.local_ipv_6gateway_ip
        result['PeerIpv6GatewayIp'] = self.peer_ipv_6gateway_ip
        result['PeeringIpv6SubnetMask'] = self.peering_ipv_6subnet_mask
        result['EnableIpv6'] = self.enable_ipv_6
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vbr_id = map.get('VbrId')
        self.vlan_id = map.get('VlanId')
        self.circuit_code = map.get('CircuitCode')
        self.local_gateway_ip = map.get('LocalGatewayIp')
        self.peer_gateway_ip = map.get('PeerGatewayIp')
        self.peering_subnet_mask = map.get('PeeringSubnetMask')
        self.min_tx_interval = map.get('MinTxInterval')
        self.min_rx_interval = map.get('MinRxInterval')
        self.detect_multiplier = map.get('DetectMultiplier')
        self.description = map.get('Description')
        self.name = map.get('Name')
        self.associated_physical_connections = map.get('AssociatedPhysicalConnections')
        self.client_token = map.get('ClientToken')
        self.local_ipv_6gateway_ip = map.get('LocalIpv6GatewayIp')
        self.peer_ipv_6gateway_ip = map.get('PeerIpv6GatewayIp')
        self.peering_ipv_6subnet_mask = map.get('PeeringIpv6SubnetMask')
        self.enable_ipv_6 = map.get('EnableIpv6')
        return self


class ModifyVirtualBorderRouterAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyRouterInterfaceSpecRequest(TeaModel):
    def __init__(self, region_id=None, router_interface_id=None, spec=None, client_token=None):
        self.region_id = region_id
        self.router_interface_id = router_interface_id
        self.spec = spec
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.router_interface_id, 'router_interface_id')
        self.validate_required(self.spec, 'spec')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['RouterInterfaceId'] = self.router_interface_id
        result['Spec'] = self.spec
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.router_interface_id = map.get('RouterInterfaceId')
        self.spec = map.get('Spec')
        self.client_token = map.get('ClientToken')
        return self


class ModifyRouterInterfaceSpecResponse(TeaModel):
    def __init__(self, request_id=None, spec=None):
        self.request_id = request_id
        self.spec = spec

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.spec, 'spec')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Spec'] = self.spec
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.spec = map.get('Spec')
        return self


class ModifyRouterInterfaceAttributeRequest(TeaModel):
    def __init__(self, region_id=None, router_interface_id=None, name=None, description=None,
                 opposite_interface_id=None, opposite_router_id=None, opposite_router_type=None, opposite_interface_owner_id=None,
                 health_check_source_ip=None, health_check_target_ip=None, hc_threshold=None, hc_rate=None, delete_health_check_ip=None):
        self.region_id = region_id
        self.router_interface_id = router_interface_id
        self.name = name
        self.description = description
        self.opposite_interface_id = opposite_interface_id
        self.opposite_router_id = opposite_router_id
        self.opposite_router_type = opposite_router_type
        self.opposite_interface_owner_id = opposite_interface_owner_id
        self.health_check_source_ip = health_check_source_ip
        self.health_check_target_ip = health_check_target_ip
        self.hc_threshold = hc_threshold
        self.hc_rate = hc_rate
        self.delete_health_check_ip = delete_health_check_ip

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.router_interface_id, 'router_interface_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['RouterInterfaceId'] = self.router_interface_id
        result['Name'] = self.name
        result['Description'] = self.description
        result['OppositeInterfaceId'] = self.opposite_interface_id
        result['OppositeRouterId'] = self.opposite_router_id
        result['OppositeRouterType'] = self.opposite_router_type
        result['OppositeInterfaceOwnerId'] = self.opposite_interface_owner_id
        result['HealthCheckSourceIp'] = self.health_check_source_ip
        result['HealthCheckTargetIp'] = self.health_check_target_ip
        result['HcThreshold'] = self.hc_threshold
        result['HcRate'] = self.hc_rate
        result['DeleteHealthCheckIp'] = self.delete_health_check_ip
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.router_interface_id = map.get('RouterInterfaceId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.opposite_interface_id = map.get('OppositeInterfaceId')
        self.opposite_router_id = map.get('OppositeRouterId')
        self.opposite_router_type = map.get('OppositeRouterType')
        self.opposite_interface_owner_id = map.get('OppositeInterfaceOwnerId')
        self.health_check_source_ip = map.get('HealthCheckSourceIp')
        self.health_check_target_ip = map.get('HealthCheckTargetIp')
        self.hc_threshold = map.get('HcThreshold')
        self.hc_rate = map.get('HcRate')
        self.delete_health_check_ip = map.get('DeleteHealthCheckIp')
        return self


class ModifyRouterInterfaceAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyPhysicalConnectionAttributeRequest(TeaModel):
    def __init__(self, region_id=None, physical_connection_id=None, line_operator=None, bandwidth=None,
                 peer_location=None, port_type=None, redundant_physical_connection_id=None, description=None, name=None,
                 client_token=None, circuit_code=None):
        self.region_id = region_id
        self.physical_connection_id = physical_connection_id
        self.line_operator = line_operator
        self.bandwidth = bandwidth
        self.peer_location = peer_location
        self.port_type = port_type
        self.redundant_physical_connection_id = redundant_physical_connection_id
        self.description = description
        self.name = name
        self.client_token = client_token
        self.circuit_code = circuit_code

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.physical_connection_id, 'physical_connection_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['PhysicalConnectionId'] = self.physical_connection_id
        result['LineOperator'] = self.line_operator
        result['bandwidth'] = self.bandwidth
        result['PeerLocation'] = self.peer_location
        result['PortType'] = self.port_type
        result['RedundantPhysicalConnectionId'] = self.redundant_physical_connection_id
        result['Description'] = self.description
        result['Name'] = self.name
        result['ClientToken'] = self.client_token
        result['CircuitCode'] = self.circuit_code
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.physical_connection_id = map.get('PhysicalConnectionId')
        self.line_operator = map.get('LineOperator')
        self.bandwidth = map.get('bandwidth')
        self.peer_location = map.get('PeerLocation')
        self.port_type = map.get('PortType')
        self.redundant_physical_connection_id = map.get('RedundantPhysicalConnectionId')
        self.description = map.get('Description')
        self.name = map.get('Name')
        self.client_token = map.get('ClientToken')
        self.circuit_code = map.get('CircuitCode')
        return self


class ModifyPhysicalConnectionAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyHaVipAttributeRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, ha_vip_id=None, description=None, name=None):
        self.client_token = client_token
        self.region_id = region_id
        self.ha_vip_id = ha_vip_id
        self.description = description
        self.name = name

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ha_vip_id, 'ha_vip_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['HaVipId'] = self.ha_vip_id
        result['Description'] = self.description
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.ha_vip_id = map.get('HaVipId')
        self.description = map.get('Description')
        self.name = map.get('Name')
        return self


class ModifyHaVipAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyForwardEntryRequest(TeaModel):
    def __init__(self, forward_table_id=None, forward_entry_id=None, external_ip=None, external_port=None,
                 internal_ip=None, internal_port=None, ip_protocol=None, forward_entry_name=None, region_id=None,
                 client_token=None, port_break=None):
        self.forward_table_id = forward_table_id
        self.forward_entry_id = forward_entry_id
        self.external_ip = external_ip
        self.external_port = external_port
        self.internal_ip = internal_ip
        self.internal_port = internal_port
        self.ip_protocol = ip_protocol
        self.forward_entry_name = forward_entry_name
        self.region_id = region_id
        self.client_token = client_token
        self.port_break = port_break

    def validate(self):
        self.validate_required(self.forward_table_id, 'forward_table_id')
        self.validate_required(self.forward_entry_id, 'forward_entry_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['ForwardTableId'] = self.forward_table_id
        result['ForwardEntryId'] = self.forward_entry_id
        result['ExternalIp'] = self.external_ip
        result['ExternalPort'] = self.external_port
        result['InternalIp'] = self.internal_ip
        result['InternalPort'] = self.internal_port
        result['IpProtocol'] = self.ip_protocol
        result['ForwardEntryName'] = self.forward_entry_name
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['PortBreak'] = self.port_break
        return result

    def from_map(self, map={}):
        self.forward_table_id = map.get('ForwardTableId')
        self.forward_entry_id = map.get('ForwardEntryId')
        self.external_ip = map.get('ExternalIp')
        self.external_port = map.get('ExternalPort')
        self.internal_ip = map.get('InternalIp')
        self.internal_port = map.get('InternalPort')
        self.ip_protocol = map.get('IpProtocol')
        self.forward_entry_name = map.get('ForwardEntryName')
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.port_break = map.get('PortBreak')
        return self


class ModifyForwardEntryResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyEipAddressAttributeRequest(TeaModel):
    def __init__(self, allocation_id=None, bandwidth=None, region_id=None, name=None, description=None):
        self.allocation_id = allocation_id
        self.bandwidth = bandwidth
        self.region_id = region_id
        self.name = name
        self.description = description

    def validate(self):
        self.validate_required(self.allocation_id, 'allocation_id')

    def to_map(self):
        result = {}
        result['AllocationId'] = self.allocation_id
        result['Bandwidth'] = self.bandwidth
        result['RegionId'] = self.region_id
        result['Name'] = self.name
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.allocation_id = map.get('AllocationId')
        self.bandwidth = map.get('Bandwidth')
        self.region_id = map.get('RegionId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        return self


class ModifyEipAddressAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyBandwidthPackageSpecRequest(TeaModel):
    def __init__(self, region_id=None, bandwidth_package_id=None, bandwidth=None):
        self.region_id = region_id
        self.bandwidth_package_id = bandwidth_package_id
        self.bandwidth = bandwidth

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bandwidth_package_id, 'bandwidth_package_id')
        self.validate_required(self.bandwidth, 'bandwidth')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['BandwidthPackageId'] = self.bandwidth_package_id
        result['Bandwidth'] = self.bandwidth
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        self.bandwidth = map.get('Bandwidth')
        return self


class ModifyBandwidthPackageSpecResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class EnablePhysicalConnectionRequest(TeaModel):
    def __init__(self, region_id=None, physical_connection_id=None, client_token=None):
        self.region_id = region_id
        self.physical_connection_id = physical_connection_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.physical_connection_id, 'physical_connection_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['PhysicalConnectionId'] = self.physical_connection_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.physical_connection_id = map.get('PhysicalConnectionId')
        self.client_token = map.get('ClientToken')
        return self


class EnablePhysicalConnectionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        return self


class DescribeZonesResponse(TeaModel):
    def __init__(self, request_id=None, zones=None):
        self.request_id = request_id
        self.zones = zones  # type: DescribeZonesResponseZones

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.zones, 'zones')
        if self.zones:
            self.zones.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        else:
            result['Zones'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Zones') is not None:
            temp_model = DescribeZonesResponseZones()
            self.zones = temp_model.from_map(map['Zones'])
        else:
            self.zones = None
        return self


class DescribeZonesResponseZonesZone(TeaModel):
    def __init__(self, zone_id=None, local_name=None):
        self.zone_id = zone_id
        self.local_name = local_name

    def validate(self):
        self.validate_required(self.zone_id, 'zone_id')
        self.validate_required(self.local_name, 'local_name')

    def to_map(self):
        result = {}
        result['ZoneId'] = self.zone_id
        result['LocalName'] = self.local_name
        return result

    def from_map(self, map={}):
        self.zone_id = map.get('ZoneId')
        self.local_name = map.get('LocalName')
        return self


class DescribeZonesResponseZones(TeaModel):
    def __init__(self, zone=None):
        self.zone = zone

    def validate(self):
        self.validate_required(self.zone, 'zone')
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        else:
            result['Zone'] = None
        return result

    def from_map(self, map={}):
        self.zone = []
        if map.get('Zone') is not None:
            for k in map.get('Zone'):
                temp_model = DescribeZonesResponseZonesZone()
                self.zone.append(temp_model.from_map(k))
        else:
            self.zone = None
        return self


class DescribeVSwitchesRequest(TeaModel):
    def __init__(self, vpc_id=None, v_switch_id=None, zone_id=None, region_id=None, v_switch_name=None, dry_run=None,
                 is_default=None, route_table_id=None, resource_group_id=None, page_number=None, page_size=None,
                 v_switch_owner_id=None):
        self.vpc_id = vpc_id
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id
        self.region_id = region_id
        self.v_switch_name = v_switch_name
        self.dry_run = dry_run
        self.is_default = is_default
        self.route_table_id = route_table_id
        self.resource_group_id = resource_group_id
        self.page_number = page_number
        self.page_size = page_size
        self.v_switch_owner_id = v_switch_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['VpcId'] = self.vpc_id
        result['VSwitchId'] = self.v_switch_id
        result['ZoneId'] = self.zone_id
        result['RegionId'] = self.region_id
        result['VSwitchName'] = self.v_switch_name
        result['DryRun'] = self.dry_run
        result['IsDefault'] = self.is_default
        result['RouteTableId'] = self.route_table_id
        result['ResourceGroupId'] = self.resource_group_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['VSwitchOwnerId'] = self.v_switch_owner_id
        return result

    def from_map(self, map={}):
        self.vpc_id = map.get('VpcId')
        self.v_switch_id = map.get('VSwitchId')
        self.zone_id = map.get('ZoneId')
        self.region_id = map.get('RegionId')
        self.v_switch_name = map.get('VSwitchName')
        self.dry_run = map.get('DryRun')
        self.is_default = map.get('IsDefault')
        self.route_table_id = map.get('RouteTableId')
        self.resource_group_id = map.get('ResourceGroupId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.v_switch_owner_id = map.get('VSwitchOwnerId')
        return self


class DescribeVSwitchesResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, v_switches=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.v_switches = v_switches  # type: DescribeVSwitchesResponseVSwitches

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.v_switches, 'v_switches')
        if self.v_switches:
            self.v_switches.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches.to_map()
        else:
            result['VSwitches'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('VSwitches') is not None:
            temp_model = DescribeVSwitchesResponseVSwitches()
            self.v_switches = temp_model.from_map(map['VSwitches'])
        else:
            self.v_switches = None
        return self


class DescribeVSwitchesResponseVSwitchesVSwitchTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class DescribeVSwitchesResponseVSwitchesVSwitchTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag

    def validate(self):
        self.validate_required(self.tag, 'tag')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        return result

    def from_map(self, map={}):
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = DescribeVSwitchesResponseVSwitchesVSwitchTagsTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        return self


class DescribeVSwitchesResponseVSwitchesVSwitchRouteTable(TeaModel):
    def __init__(self, route_table_id=None, route_table_type=None):
        self.route_table_id = route_table_id
        self.route_table_type = route_table_type

    def validate(self):
        self.validate_required(self.route_table_id, 'route_table_id')
        self.validate_required(self.route_table_type, 'route_table_type')

    def to_map(self):
        result = {}
        result['RouteTableId'] = self.route_table_id
        result['RouteTableType'] = self.route_table_type
        return result

    def from_map(self, map={}):
        self.route_table_id = map.get('RouteTableId')
        self.route_table_type = map.get('RouteTableType')
        return self


class DescribeVSwitchesResponseVSwitchesVSwitch(TeaModel):
    def __init__(self, v_switch_id=None, vpc_id=None, status=None, cidr_block=None, ipv_6cidr_block=None,
                 zone_id=None, available_ip_address_count=None, description=None, v_switch_name=None, creation_time=None,
                 is_default=None, resource_group_id=None, network_acl_id=None, owner_id=None, share_type=None, tags=None,
                 route_table=None):
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.status = status
        self.cidr_block = cidr_block
        self.ipv_6cidr_block = ipv_6cidr_block
        self.zone_id = zone_id
        self.available_ip_address_count = available_ip_address_count
        self.description = description
        self.v_switch_name = v_switch_name
        self.creation_time = creation_time
        self.is_default = is_default
        self.resource_group_id = resource_group_id
        self.network_acl_id = network_acl_id
        self.owner_id = owner_id
        self.share_type = share_type
        self.tags = tags  # type: DescribeVSwitchesResponseVSwitchesVSwitchTags
        self.route_table = route_table  # type: DescribeVSwitchesResponseVSwitchesVSwitchRouteTable

    def validate(self):
        self.validate_required(self.v_switch_id, 'v_switch_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.cidr_block, 'cidr_block')
        self.validate_required(self.ipv_6cidr_block, 'ipv_6cidr_block')
        self.validate_required(self.zone_id, 'zone_id')
        self.validate_required(self.available_ip_address_count, 'available_ip_address_count')
        self.validate_required(self.description, 'description')
        self.validate_required(self.v_switch_name, 'v_switch_name')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.is_default, 'is_default')
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.network_acl_id, 'network_acl_id')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.share_type, 'share_type')
        self.validate_required(self.tags, 'tags')
        if self.tags:
            self.tags.validate()
        self.validate_required(self.route_table, 'route_table')
        if self.route_table:
            self.route_table.validate()

    def to_map(self):
        result = {}
        result['VSwitchId'] = self.v_switch_id
        result['VpcId'] = self.vpc_id
        result['Status'] = self.status
        result['CidrBlock'] = self.cidr_block
        result['Ipv6CidrBlock'] = self.ipv_6cidr_block
        result['ZoneId'] = self.zone_id
        result['AvailableIpAddressCount'] = self.available_ip_address_count
        result['Description'] = self.description
        result['VSwitchName'] = self.v_switch_name
        result['CreationTime'] = self.creation_time
        result['IsDefault'] = self.is_default
        result['ResourceGroupId'] = self.resource_group_id
        result['NetworkAclId'] = self.network_acl_id
        result['OwnerId'] = self.owner_id
        result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        else:
            result['Tags'] = None
        if self.route_table is not None:
            result['RouteTable'] = self.route_table.to_map()
        else:
            result['RouteTable'] = None
        return result

    def from_map(self, map={}):
        self.v_switch_id = map.get('VSwitchId')
        self.vpc_id = map.get('VpcId')
        self.status = map.get('Status')
        self.cidr_block = map.get('CidrBlock')
        self.ipv_6cidr_block = map.get('Ipv6CidrBlock')
        self.zone_id = map.get('ZoneId')
        self.available_ip_address_count = map.get('AvailableIpAddressCount')
        self.description = map.get('Description')
        self.v_switch_name = map.get('VSwitchName')
        self.creation_time = map.get('CreationTime')
        self.is_default = map.get('IsDefault')
        self.resource_group_id = map.get('ResourceGroupId')
        self.network_acl_id = map.get('NetworkAclId')
        self.owner_id = map.get('OwnerId')
        self.share_type = map.get('ShareType')
        if map.get('Tags') is not None:
            temp_model = DescribeVSwitchesResponseVSwitchesVSwitchTags()
            self.tags = temp_model.from_map(map['Tags'])
        else:
            self.tags = None
        if map.get('RouteTable') is not None:
            temp_model = DescribeVSwitchesResponseVSwitchesVSwitchRouteTable()
            self.route_table = temp_model.from_map(map['RouteTable'])
        else:
            self.route_table = None
        return self


class DescribeVSwitchesResponseVSwitches(TeaModel):
    def __init__(self, v_switch=None):
        self.v_switch = v_switch

    def validate(self):
        self.validate_required(self.v_switch, 'v_switch')
        if self.v_switch:
            for k in self.v_switch:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['VSwitch'] = []
        if self.v_switch is not None:
            for k in self.v_switch:
                result['VSwitch'].append(k.to_map() if k else None)
        else:
            result['VSwitch'] = None
        return result

    def from_map(self, map={}):
        self.v_switch = []
        if map.get('VSwitch') is not None:
            for k in map.get('VSwitch'):
                temp_model = DescribeVSwitchesResponseVSwitchesVSwitch()
                self.v_switch.append(temp_model.from_map(k))
        else:
            self.v_switch = None
        return self


class DescribeVRoutersRequest(TeaModel):
    def __init__(self, vrouter_id=None, region_id=None, page_number=None, page_size=None):
        self.vrouter_id = vrouter_id
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['VRouterId'] = self.vrouter_id
        result['RegionId'] = self.region_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.vrouter_id = map.get('VRouterId')
        self.region_id = map.get('RegionId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeVRoutersResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, vrouters=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.vrouters = vrouters  # type: DescribeVRoutersResponseVRouters

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.vrouters, 'vrouters')
        if self.vrouters:
            self.vrouters.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.vrouters is not None:
            result['VRouters'] = self.vrouters.to_map()
        else:
            result['VRouters'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('VRouters') is not None:
            temp_model = DescribeVRoutersResponseVRouters()
            self.vrouters = temp_model.from_map(map['VRouters'])
        else:
            self.vrouters = None
        return self


class DescribeVRoutersResponseVRoutersVRouterRouteTableIds(TeaModel):
    def __init__(self, route_table_id=None):
        # RouteTableId
        self.route_table_id = route_table_id

    def validate(self):
        self.validate_required(self.route_table_id, 'route_table_id')

    def to_map(self):
        result = {}
        result['RouteTableId'] = self.route_table_id
        return result

    def from_map(self, map={}):
        self.route_table_id = map.get('RouteTableId')
        return self


class DescribeVRoutersResponseVRoutersVRouter(TeaModel):
    def __init__(self, region_id=None, vpc_id=None, vrouter_name=None, description=None, vrouter_id=None,
                 creation_time=None, route_table_ids=None):
        self.region_id = region_id
        self.vpc_id = vpc_id
        self.vrouter_name = vrouter_name
        self.description = description
        self.vrouter_id = vrouter_id
        self.creation_time = creation_time
        self.route_table_ids = route_table_ids  # type: DescribeVRoutersResponseVRoutersVRouterRouteTableIds

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.vrouter_name, 'vrouter_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.vrouter_id, 'vrouter_id')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.route_table_ids, 'route_table_ids')
        if self.route_table_ids:
            self.route_table_ids.validate()

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VpcId'] = self.vpc_id
        result['VRouterName'] = self.vrouter_name
        result['Description'] = self.description
        result['VRouterId'] = self.vrouter_id
        result['CreationTime'] = self.creation_time
        if self.route_table_ids is not None:
            result['RouteTableIds'] = self.route_table_ids.to_map()
        else:
            result['RouteTableIds'] = None
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vpc_id = map.get('VpcId')
        self.vrouter_name = map.get('VRouterName')
        self.description = map.get('Description')
        self.vrouter_id = map.get('VRouterId')
        self.creation_time = map.get('CreationTime')
        if map.get('RouteTableIds') is not None:
            temp_model = DescribeVRoutersResponseVRoutersVRouterRouteTableIds()
            self.route_table_ids = temp_model.from_map(map['RouteTableIds'])
        else:
            self.route_table_ids = None
        return self


class DescribeVRoutersResponseVRouters(TeaModel):
    def __init__(self, vrouter=None):
        self.vrouter = vrouter

    def validate(self):
        self.validate_required(self.vrouter, 'vrouter')
        if self.vrouter:
            for k in self.vrouter:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['VRouter'] = []
        if self.vrouter is not None:
            for k in self.vrouter:
                result['VRouter'].append(k.to_map() if k else None)
        else:
            result['VRouter'] = None
        return result

    def from_map(self, map={}):
        self.vrouter = []
        if map.get('VRouter') is not None:
            for k in map.get('VRouter'):
                temp_model = DescribeVRoutersResponseVRoutersVRouter()
                self.vrouter.append(temp_model.from_map(k))
        else:
            self.vrouter = None
        return self


class DescribeVpcsRequest(TeaModel):
    def __init__(self, vpc_id=None, region_id=None, vpc_name=None, is_default=None, dry_run=None,
                 resource_group_id=None, page_number=None, page_size=None, vpc_owner_id=None, dhcp_options_set_id=None):
        self.vpc_id = vpc_id
        self.region_id = region_id
        self.vpc_name = vpc_name
        self.is_default = is_default
        self.dry_run = dry_run
        self.resource_group_id = resource_group_id
        self.page_number = page_number
        self.page_size = page_size
        self.vpc_owner_id = vpc_owner_id
        self.dhcp_options_set_id = dhcp_options_set_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['VpcId'] = self.vpc_id
        result['RegionId'] = self.region_id
        result['VpcName'] = self.vpc_name
        result['IsDefault'] = self.is_default
        result['DryRun'] = self.dry_run
        result['ResourceGroupId'] = self.resource_group_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['VpcOwnerId'] = self.vpc_owner_id
        result['DhcpOptionsSetId'] = self.dhcp_options_set_id
        return result

    def from_map(self, map={}):
        self.vpc_id = map.get('VpcId')
        self.region_id = map.get('RegionId')
        self.vpc_name = map.get('VpcName')
        self.is_default = map.get('IsDefault')
        self.dry_run = map.get('DryRun')
        self.resource_group_id = map.get('ResourceGroupId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.vpc_owner_id = map.get('VpcOwnerId')
        self.dhcp_options_set_id = map.get('DhcpOptionsSetId')
        return self


class DescribeVpcsResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, vpcs=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.vpcs = vpcs  # type: DescribeVpcsResponseVpcs

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.vpcs, 'vpcs')
        if self.vpcs:
            self.vpcs.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.vpcs is not None:
            result['Vpcs'] = self.vpcs.to_map()
        else:
            result['Vpcs'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('Vpcs') is not None:
            temp_model = DescribeVpcsResponseVpcs()
            self.vpcs = temp_model.from_map(map['Vpcs'])
        else:
            self.vpcs = None
        return self


class DescribeVpcsResponseVpcsVpcTagsTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class DescribeVpcsResponseVpcsVpcTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag

    def validate(self):
        self.validate_required(self.tag, 'tag')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        return result

    def from_map(self, map={}):
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = DescribeVpcsResponseVpcsVpcTagsTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        return self


class DescribeVpcsResponseVpcsVpcVSwitchIds(TeaModel):
    def __init__(self, v_switch_id=None):
        # VSwitchId
        self.v_switch_id = v_switch_id

    def validate(self):
        self.validate_required(self.v_switch_id, 'v_switch_id')

    def to_map(self):
        result = {}
        result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, map={}):
        self.v_switch_id = map.get('VSwitchId')
        return self


class DescribeVpcsResponseVpcsVpcUserCidrs(TeaModel):
    def __init__(self, user_cidr=None):
        # UserCidr
        self.user_cidr = user_cidr

    def validate(self):
        self.validate_required(self.user_cidr, 'user_cidr')

    def to_map(self):
        result = {}
        result['UserCidr'] = self.user_cidr
        return result

    def from_map(self, map={}):
        self.user_cidr = map.get('UserCidr')
        return self


class DescribeVpcsResponseVpcsVpcNatGatewayIds(TeaModel):
    def __init__(self, nat_gateway_ids=None):
        # NatGatewayIds
        self.nat_gateway_ids = nat_gateway_ids

    def validate(self):
        self.validate_required(self.nat_gateway_ids, 'nat_gateway_ids')

    def to_map(self):
        result = {}
        result['NatGatewayIds'] = self.nat_gateway_ids
        return result

    def from_map(self, map={}):
        self.nat_gateway_ids = map.get('NatGatewayIds')
        return self


class DescribeVpcsResponseVpcsVpcRouterTableIds(TeaModel):
    def __init__(self, router_table_ids=None):
        # RouterTableIds
        self.router_table_ids = router_table_ids

    def validate(self):
        self.validate_required(self.router_table_ids, 'router_table_ids')

    def to_map(self):
        result = {}
        result['RouterTableIds'] = self.router_table_ids
        return result

    def from_map(self, map={}):
        self.router_table_ids = map.get('RouterTableIds')
        return self


class DescribeVpcsResponseVpcsVpcSecondaryCidrBlocks(TeaModel):
    def __init__(self, secondary_cidr_block=None):
        # SecondaryCidrBlock
        self.secondary_cidr_block = secondary_cidr_block

    def validate(self):
        self.validate_required(self.secondary_cidr_block, 'secondary_cidr_block')

    def to_map(self):
        result = {}
        result['SecondaryCidrBlock'] = self.secondary_cidr_block
        return result

    def from_map(self, map={}):
        self.secondary_cidr_block = map.get('SecondaryCidrBlock')
        return self


class DescribeVpcsResponseVpcsVpc(TeaModel):
    def __init__(self, vpc_id=None, region_id=None, status=None, vpc_name=None, creation_time=None, cidr_block=None,
                 ipv_6cidr_block=None, vrouter_id=None, description=None, is_default=None, network_acl_num=None,
                 resource_group_id=None, cen_status=None, owner_id=None, support_advanced_feature=None, advanced_resource=None,
                 dhcp_options_set_id=None, dhcp_options_set_status=None, tags=None, v_switch_ids=None, user_cidrs=None,
                 nat_gateway_ids=None, router_table_ids=None, secondary_cidr_blocks=None):
        self.vpc_id = vpc_id
        self.region_id = region_id
        self.status = status
        self.vpc_name = vpc_name
        self.creation_time = creation_time
        self.cidr_block = cidr_block
        self.ipv_6cidr_block = ipv_6cidr_block
        self.vrouter_id = vrouter_id
        self.description = description
        self.is_default = is_default
        self.network_acl_num = network_acl_num
        self.resource_group_id = resource_group_id
        self.cen_status = cen_status
        self.owner_id = owner_id
        self.support_advanced_feature = support_advanced_feature
        self.advanced_resource = advanced_resource
        self.dhcp_options_set_id = dhcp_options_set_id
        self.dhcp_options_set_status = dhcp_options_set_status
        self.tags = tags  # type: DescribeVpcsResponseVpcsVpcTags
        self.v_switch_ids = v_switch_ids  # type: DescribeVpcsResponseVpcsVpcVSwitchIds
        self.user_cidrs = user_cidrs  # type: DescribeVpcsResponseVpcsVpcUserCidrs
        self.nat_gateway_ids = nat_gateway_ids  # type: DescribeVpcsResponseVpcsVpcNatGatewayIds
        self.router_table_ids = router_table_ids  # type: DescribeVpcsResponseVpcsVpcRouterTableIds
        self.secondary_cidr_blocks = secondary_cidr_blocks  # type: DescribeVpcsResponseVpcsVpcSecondaryCidrBlocks

    def validate(self):
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.vpc_name, 'vpc_name')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.cidr_block, 'cidr_block')
        self.validate_required(self.ipv_6cidr_block, 'ipv_6cidr_block')
        self.validate_required(self.vrouter_id, 'vrouter_id')
        self.validate_required(self.description, 'description')
        self.validate_required(self.is_default, 'is_default')
        self.validate_required(self.network_acl_num, 'network_acl_num')
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.cen_status, 'cen_status')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.support_advanced_feature, 'support_advanced_feature')
        self.validate_required(self.advanced_resource, 'advanced_resource')
        self.validate_required(self.dhcp_options_set_id, 'dhcp_options_set_id')
        self.validate_required(self.dhcp_options_set_status, 'dhcp_options_set_status')
        self.validate_required(self.tags, 'tags')
        if self.tags:
            self.tags.validate()
        self.validate_required(self.v_switch_ids, 'v_switch_ids')
        if self.v_switch_ids:
            self.v_switch_ids.validate()
        self.validate_required(self.user_cidrs, 'user_cidrs')
        if self.user_cidrs:
            self.user_cidrs.validate()
        self.validate_required(self.nat_gateway_ids, 'nat_gateway_ids')
        if self.nat_gateway_ids:
            self.nat_gateway_ids.validate()
        self.validate_required(self.router_table_ids, 'router_table_ids')
        if self.router_table_ids:
            self.router_table_ids.validate()
        self.validate_required(self.secondary_cidr_blocks, 'secondary_cidr_blocks')
        if self.secondary_cidr_blocks:
            self.secondary_cidr_blocks.validate()

    def to_map(self):
        result = {}
        result['VpcId'] = self.vpc_id
        result['RegionId'] = self.region_id
        result['Status'] = self.status
        result['VpcName'] = self.vpc_name
        result['CreationTime'] = self.creation_time
        result['CidrBlock'] = self.cidr_block
        result['Ipv6CidrBlock'] = self.ipv_6cidr_block
        result['VRouterId'] = self.vrouter_id
        result['Description'] = self.description
        result['IsDefault'] = self.is_default
        result['NetworkAclNum'] = self.network_acl_num
        result['ResourceGroupId'] = self.resource_group_id
        result['CenStatus'] = self.cen_status
        result['OwnerId'] = self.owner_id
        result['SupportAdvancedFeature'] = self.support_advanced_feature
        result['AdvancedResource'] = self.advanced_resource
        result['DhcpOptionsSetId'] = self.dhcp_options_set_id
        result['DhcpOptionsSetStatus'] = self.dhcp_options_set_status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        else:
            result['Tags'] = None
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids.to_map()
        else:
            result['VSwitchIds'] = None
        if self.user_cidrs is not None:
            result['UserCidrs'] = self.user_cidrs.to_map()
        else:
            result['UserCidrs'] = None
        if self.nat_gateway_ids is not None:
            result['NatGatewayIds'] = self.nat_gateway_ids.to_map()
        else:
            result['NatGatewayIds'] = None
        if self.router_table_ids is not None:
            result['RouterTableIds'] = self.router_table_ids.to_map()
        else:
            result['RouterTableIds'] = None
        if self.secondary_cidr_blocks is not None:
            result['SecondaryCidrBlocks'] = self.secondary_cidr_blocks.to_map()
        else:
            result['SecondaryCidrBlocks'] = None
        return result

    def from_map(self, map={}):
        self.vpc_id = map.get('VpcId')
        self.region_id = map.get('RegionId')
        self.status = map.get('Status')
        self.vpc_name = map.get('VpcName')
        self.creation_time = map.get('CreationTime')
        self.cidr_block = map.get('CidrBlock')
        self.ipv_6cidr_block = map.get('Ipv6CidrBlock')
        self.vrouter_id = map.get('VRouterId')
        self.description = map.get('Description')
        self.is_default = map.get('IsDefault')
        self.network_acl_num = map.get('NetworkAclNum')
        self.resource_group_id = map.get('ResourceGroupId')
        self.cen_status = map.get('CenStatus')
        self.owner_id = map.get('OwnerId')
        self.support_advanced_feature = map.get('SupportAdvancedFeature')
        self.advanced_resource = map.get('AdvancedResource')
        self.dhcp_options_set_id = map.get('DhcpOptionsSetId')
        self.dhcp_options_set_status = map.get('DhcpOptionsSetStatus')
        if map.get('Tags') is not None:
            temp_model = DescribeVpcsResponseVpcsVpcTags()
            self.tags = temp_model.from_map(map['Tags'])
        else:
            self.tags = None
        if map.get('VSwitchIds') is not None:
            temp_model = DescribeVpcsResponseVpcsVpcVSwitchIds()
            self.v_switch_ids = temp_model.from_map(map['VSwitchIds'])
        else:
            self.v_switch_ids = None
        if map.get('UserCidrs') is not None:
            temp_model = DescribeVpcsResponseVpcsVpcUserCidrs()
            self.user_cidrs = temp_model.from_map(map['UserCidrs'])
        else:
            self.user_cidrs = None
        if map.get('NatGatewayIds') is not None:
            temp_model = DescribeVpcsResponseVpcsVpcNatGatewayIds()
            self.nat_gateway_ids = temp_model.from_map(map['NatGatewayIds'])
        else:
            self.nat_gateway_ids = None
        if map.get('RouterTableIds') is not None:
            temp_model = DescribeVpcsResponseVpcsVpcRouterTableIds()
            self.router_table_ids = temp_model.from_map(map['RouterTableIds'])
        else:
            self.router_table_ids = None
        if map.get('SecondaryCidrBlocks') is not None:
            temp_model = DescribeVpcsResponseVpcsVpcSecondaryCidrBlocks()
            self.secondary_cidr_blocks = temp_model.from_map(map['SecondaryCidrBlocks'])
        else:
            self.secondary_cidr_blocks = None
        return self


class DescribeVpcsResponseVpcs(TeaModel):
    def __init__(self, vpc=None):
        self.vpc = vpc

    def validate(self):
        self.validate_required(self.vpc, 'vpc')
        if self.vpc:
            for k in self.vpc:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Vpc'] = []
        if self.vpc is not None:
            for k in self.vpc:
                result['Vpc'].append(k.to_map() if k else None)
        else:
            result['Vpc'] = None
        return result

    def from_map(self, map={}):
        self.vpc = []
        if map.get('Vpc') is not None:
            for k in map.get('Vpc'):
                temp_model = DescribeVpcsResponseVpcsVpc()
                self.vpc.append(temp_model.from_map(k))
        else:
            self.vpc = None
        return self


class DescribeVirtualBorderRoutersForPhysicalConnectionRequest(TeaModel):
    def __init__(self, filter=None, region_id=None, physical_connection_id=None, page_number=None, page_size=None):
        self.filter = filter
        self.region_id = region_id
        self.physical_connection_id = physical_connection_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.physical_connection_id, 'physical_connection_id')

    def to_map(self):
        result = {}
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        else:
            result['Filter'] = None
        result['RegionId'] = self.region_id
        result['PhysicalConnectionId'] = self.physical_connection_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.filter = []
        if map.get('Filter') is not None:
            for k in map.get('Filter'):
                temp_model = DescribeVirtualBorderRoutersForPhysicalConnectionRequestFilter()
                self.filter.append(temp_model.from_map(k))
        else:
            self.filter = None
        self.region_id = map.get('RegionId')
        self.physical_connection_id = map.get('PhysicalConnectionId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeVirtualBorderRoutersForPhysicalConnectionRequestFilter(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class DescribeVirtualBorderRoutersForPhysicalConnectionResponse(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None,
                 virtual_border_router_for_physical_connection_set=None):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.virtual_border_router_for_physical_connection_set = virtual_border_router_for_physical_connection_set  # type: DescribeVirtualBorderRoutersForPhysicalConnectionResponseVirtualBorderRouterForPhysicalConnectionSet

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.virtual_border_router_for_physical_connection_set, 'virtual_border_router_for_physical_connection_set')
        if self.virtual_border_router_for_physical_connection_set:
            self.virtual_border_router_for_physical_connection_set.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        if self.virtual_border_router_for_physical_connection_set is not None:
            result['VirtualBorderRouterForPhysicalConnectionSet'] = self.virtual_border_router_for_physical_connection_set.to_map()
        else:
            result['VirtualBorderRouterForPhysicalConnectionSet'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        if map.get('VirtualBorderRouterForPhysicalConnectionSet') is not None:
            temp_model = DescribeVirtualBorderRoutersForPhysicalConnectionResponseVirtualBorderRouterForPhysicalConnectionSet()
            self.virtual_border_router_for_physical_connection_set = temp_model.from_map(map['VirtualBorderRouterForPhysicalConnectionSet'])
        else:
            self.virtual_border_router_for_physical_connection_set = None
        return self


class DescribeVirtualBorderRoutersForPhysicalConnectionResponseVirtualBorderRouterForPhysicalConnectionSetVirtualBorderRouterForPhysicalConnectionType(TeaModel):
    def __init__(self, vbr_id=None, vbr_owner_uid=None, ecc_id=None, type=None, creation_time=None,
                 activation_time=None, termination_time=None, recovery_time=None, vlan_id=None, status=None, circuit_code=None,
                 local_gateway_ip=None, peer_gateway_ip=None, peering_subnet_mask=None, pconn_vbr_charge_type=None,
                 pconn_vbr_expire_time=None, pconn_vbr_bussiness_status=None, bandwidth=None, local_ipv_6gateway_ip=None,
                 peer_ipv_6gateway_ip=None, peering_ipv_6subnet_mask=None, enable_ipv_6=None):
        self.vbr_id = vbr_id
        self.vbr_owner_uid = vbr_owner_uid
        self.ecc_id = ecc_id
        self.type = type
        self.creation_time = creation_time
        self.activation_time = activation_time
        self.termination_time = termination_time
        self.recovery_time = recovery_time
        self.vlan_id = vlan_id
        self.status = status
        self.circuit_code = circuit_code
        self.local_gateway_ip = local_gateway_ip
        self.peer_gateway_ip = peer_gateway_ip
        self.peering_subnet_mask = peering_subnet_mask
        self.pconn_vbr_charge_type = pconn_vbr_charge_type
        self.pconn_vbr_expire_time = pconn_vbr_expire_time
        self.pconn_vbr_bussiness_status = pconn_vbr_bussiness_status
        self.bandwidth = bandwidth
        self.local_ipv_6gateway_ip = local_ipv_6gateway_ip
        self.peer_ipv_6gateway_ip = peer_ipv_6gateway_ip
        self.peering_ipv_6subnet_mask = peering_ipv_6subnet_mask
        self.enable_ipv_6 = enable_ipv_6

    def validate(self):
        self.validate_required(self.vbr_id, 'vbr_id')
        self.validate_required(self.vbr_owner_uid, 'vbr_owner_uid')
        self.validate_required(self.ecc_id, 'ecc_id')
        self.validate_required(self.type, 'type')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.activation_time, 'activation_time')
        self.validate_required(self.termination_time, 'termination_time')
        self.validate_required(self.recovery_time, 'recovery_time')
        self.validate_required(self.vlan_id, 'vlan_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.circuit_code, 'circuit_code')
        self.validate_required(self.local_gateway_ip, 'local_gateway_ip')
        self.validate_required(self.peer_gateway_ip, 'peer_gateway_ip')
        self.validate_required(self.peering_subnet_mask, 'peering_subnet_mask')
        self.validate_required(self.pconn_vbr_charge_type, 'pconn_vbr_charge_type')
        self.validate_required(self.pconn_vbr_expire_time, 'pconn_vbr_expire_time')
        self.validate_required(self.pconn_vbr_bussiness_status, 'pconn_vbr_bussiness_status')
        self.validate_required(self.bandwidth, 'bandwidth')
        self.validate_required(self.local_ipv_6gateway_ip, 'local_ipv_6gateway_ip')
        self.validate_required(self.peer_ipv_6gateway_ip, 'peer_ipv_6gateway_ip')
        self.validate_required(self.peering_ipv_6subnet_mask, 'peering_ipv_6subnet_mask')
        self.validate_required(self.enable_ipv_6, 'enable_ipv_6')

    def to_map(self):
        result = {}
        result['VbrId'] = self.vbr_id
        result['VbrOwnerUid'] = self.vbr_owner_uid
        result['EccId'] = self.ecc_id
        result['Type'] = self.type
        result['CreationTime'] = self.creation_time
        result['ActivationTime'] = self.activation_time
        result['TerminationTime'] = self.termination_time
        result['RecoveryTime'] = self.recovery_time
        result['VlanId'] = self.vlan_id
        result['Status'] = self.status
        result['CircuitCode'] = self.circuit_code
        result['LocalGatewayIp'] = self.local_gateway_ip
        result['PeerGatewayIp'] = self.peer_gateway_ip
        result['PeeringSubnetMask'] = self.peering_subnet_mask
        result['PConnVbrChargeType'] = self.pconn_vbr_charge_type
        result['PConnVbrExpireTime'] = self.pconn_vbr_expire_time
        result['PConnVbrBussinessStatus'] = self.pconn_vbr_bussiness_status
        result['Bandwidth'] = self.bandwidth
        result['LocalIpv6GatewayIp'] = self.local_ipv_6gateway_ip
        result['PeerIpv6GatewayIp'] = self.peer_ipv_6gateway_ip
        result['PeeringIpv6SubnetMask'] = self.peering_ipv_6subnet_mask
        result['EnableIpv6'] = self.enable_ipv_6
        return result

    def from_map(self, map={}):
        self.vbr_id = map.get('VbrId')
        self.vbr_owner_uid = map.get('VbrOwnerUid')
        self.ecc_id = map.get('EccId')
        self.type = map.get('Type')
        self.creation_time = map.get('CreationTime')
        self.activation_time = map.get('ActivationTime')
        self.termination_time = map.get('TerminationTime')
        self.recovery_time = map.get('RecoveryTime')
        self.vlan_id = map.get('VlanId')
        self.status = map.get('Status')
        self.circuit_code = map.get('CircuitCode')
        self.local_gateway_ip = map.get('LocalGatewayIp')
        self.peer_gateway_ip = map.get('PeerGatewayIp')
        self.peering_subnet_mask = map.get('PeeringSubnetMask')
        self.pconn_vbr_charge_type = map.get('PConnVbrChargeType')
        self.pconn_vbr_expire_time = map.get('PConnVbrExpireTime')
        self.pconn_vbr_bussiness_status = map.get('PConnVbrBussinessStatus')
        self.bandwidth = map.get('Bandwidth')
        self.local_ipv_6gateway_ip = map.get('LocalIpv6GatewayIp')
        self.peer_ipv_6gateway_ip = map.get('PeerIpv6GatewayIp')
        self.peering_ipv_6subnet_mask = map.get('PeeringIpv6SubnetMask')
        self.enable_ipv_6 = map.get('EnableIpv6')
        return self


class DescribeVirtualBorderRoutersForPhysicalConnectionResponseVirtualBorderRouterForPhysicalConnectionSet(TeaModel):
    def __init__(self, virtual_border_router_for_physical_connection_type=None):
        self.virtual_border_router_for_physical_connection_type = virtual_border_router_for_physical_connection_type

    def validate(self):
        self.validate_required(self.virtual_border_router_for_physical_connection_type, 'virtual_border_router_for_physical_connection_type')
        if self.virtual_border_router_for_physical_connection_type:
            for k in self.virtual_border_router_for_physical_connection_type:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['VirtualBorderRouterForPhysicalConnectionType'] = []
        if self.virtual_border_router_for_physical_connection_type is not None:
            for k in self.virtual_border_router_for_physical_connection_type:
                result['VirtualBorderRouterForPhysicalConnectionType'].append(k.to_map() if k else None)
        else:
            result['VirtualBorderRouterForPhysicalConnectionType'] = None
        return result

    def from_map(self, map={}):
        self.virtual_border_router_for_physical_connection_type = []
        if map.get('VirtualBorderRouterForPhysicalConnectionType') is not None:
            for k in map.get('VirtualBorderRouterForPhysicalConnectionType'):
                temp_model = DescribeVirtualBorderRoutersForPhysicalConnectionResponseVirtualBorderRouterForPhysicalConnectionSetVirtualBorderRouterForPhysicalConnectionType()
                self.virtual_border_router_for_physical_connection_type.append(temp_model.from_map(k))
        else:
            self.virtual_border_router_for_physical_connection_type = None
        return self


class DescribeVirtualBorderRoutersRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None, filter=None):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.filter = filter

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        else:
            result['Filter'] = None
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.filter = []
        if map.get('Filter') is not None:
            for k in map.get('Filter'):
                temp_model = DescribeVirtualBorderRoutersRequestFilter()
                self.filter.append(temp_model.from_map(k))
        else:
            self.filter = None
        return self


class DescribeVirtualBorderRoutersRequestFilter(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class DescribeVirtualBorderRoutersResponse(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None,
                 virtual_border_router_set=None):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.virtual_border_router_set = virtual_border_router_set  # type: DescribeVirtualBorderRoutersResponseVirtualBorderRouterSet

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.virtual_border_router_set, 'virtual_border_router_set')
        if self.virtual_border_router_set:
            self.virtual_border_router_set.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        if self.virtual_border_router_set is not None:
            result['VirtualBorderRouterSet'] = self.virtual_border_router_set.to_map()
        else:
            result['VirtualBorderRouterSet'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        if map.get('VirtualBorderRouterSet') is not None:
            temp_model = DescribeVirtualBorderRoutersResponseVirtualBorderRouterSet()
            self.virtual_border_router_set = temp_model.from_map(map['VirtualBorderRouterSet'])
        else:
            self.virtual_border_router_set = None
        return self


class DescribeVirtualBorderRoutersResponseVirtualBorderRouterSetVirtualBorderRouterTypeAssociatedPhysicalConnectionsAssociatedPhysicalConnection(TeaModel):
    def __init__(self, circuit_code=None, vlan_interface_id=None, local_gateway_ip=None, peer_gateway_ip=None,
                 peering_subnet_mask=None, physical_connection_id=None, physical_connection_status=None,
                 physical_connection_business_status=None, physical_connection_owner_uid=None, vlan_id=None, local_ipv_6gateway_ip=None,
                 peer_ipv_6gateway_ip=None, peering_ipv_6subnet_mask=None, status=None, enable_ipv_6=None):
        self.circuit_code = circuit_code
        self.vlan_interface_id = vlan_interface_id
        self.local_gateway_ip = local_gateway_ip
        self.peer_gateway_ip = peer_gateway_ip
        self.peering_subnet_mask = peering_subnet_mask
        self.physical_connection_id = physical_connection_id
        self.physical_connection_status = physical_connection_status
        self.physical_connection_business_status = physical_connection_business_status
        self.physical_connection_owner_uid = physical_connection_owner_uid
        self.vlan_id = vlan_id
        self.local_ipv_6gateway_ip = local_ipv_6gateway_ip
        self.peer_ipv_6gateway_ip = peer_ipv_6gateway_ip
        self.peering_ipv_6subnet_mask = peering_ipv_6subnet_mask
        self.status = status
        self.enable_ipv_6 = enable_ipv_6

    def validate(self):
        self.validate_required(self.circuit_code, 'circuit_code')
        self.validate_required(self.vlan_interface_id, 'vlan_interface_id')
        self.validate_required(self.local_gateway_ip, 'local_gateway_ip')
        self.validate_required(self.peer_gateway_ip, 'peer_gateway_ip')
        self.validate_required(self.peering_subnet_mask, 'peering_subnet_mask')
        self.validate_required(self.physical_connection_id, 'physical_connection_id')
        self.validate_required(self.physical_connection_status, 'physical_connection_status')
        self.validate_required(self.physical_connection_business_status, 'physical_connection_business_status')
        self.validate_required(self.physical_connection_owner_uid, 'physical_connection_owner_uid')
        self.validate_required(self.vlan_id, 'vlan_id')
        self.validate_required(self.local_ipv_6gateway_ip, 'local_ipv_6gateway_ip')
        self.validate_required(self.peer_ipv_6gateway_ip, 'peer_ipv_6gateway_ip')
        self.validate_required(self.peering_ipv_6subnet_mask, 'peering_ipv_6subnet_mask')
        self.validate_required(self.status, 'status')
        self.validate_required(self.enable_ipv_6, 'enable_ipv_6')

    def to_map(self):
        result = {}
        result['CircuitCode'] = self.circuit_code
        result['VlanInterfaceId'] = self.vlan_interface_id
        result['LocalGatewayIp'] = self.local_gateway_ip
        result['PeerGatewayIp'] = self.peer_gateway_ip
        result['PeeringSubnetMask'] = self.peering_subnet_mask
        result['PhysicalConnectionId'] = self.physical_connection_id
        result['PhysicalConnectionStatus'] = self.physical_connection_status
        result['PhysicalConnectionBusinessStatus'] = self.physical_connection_business_status
        result['PhysicalConnectionOwnerUid'] = self.physical_connection_owner_uid
        result['VlanId'] = self.vlan_id
        result['LocalIpv6GatewayIp'] = self.local_ipv_6gateway_ip
        result['PeerIpv6GatewayIp'] = self.peer_ipv_6gateway_ip
        result['PeeringIpv6SubnetMask'] = self.peering_ipv_6subnet_mask
        result['Status'] = self.status
        result['EnableIpv6'] = self.enable_ipv_6
        return result

    def from_map(self, map={}):
        self.circuit_code = map.get('CircuitCode')
        self.vlan_interface_id = map.get('VlanInterfaceId')
        self.local_gateway_ip = map.get('LocalGatewayIp')
        self.peer_gateway_ip = map.get('PeerGatewayIp')
        self.peering_subnet_mask = map.get('PeeringSubnetMask')
        self.physical_connection_id = map.get('PhysicalConnectionId')
        self.physical_connection_status = map.get('PhysicalConnectionStatus')
        self.physical_connection_business_status = map.get('PhysicalConnectionBusinessStatus')
        self.physical_connection_owner_uid = map.get('PhysicalConnectionOwnerUid')
        self.vlan_id = map.get('VlanId')
        self.local_ipv_6gateway_ip = map.get('LocalIpv6GatewayIp')
        self.peer_ipv_6gateway_ip = map.get('PeerIpv6GatewayIp')
        self.peering_ipv_6subnet_mask = map.get('PeeringIpv6SubnetMask')
        self.status = map.get('Status')
        self.enable_ipv_6 = map.get('EnableIpv6')
        return self


class DescribeVirtualBorderRoutersResponseVirtualBorderRouterSetVirtualBorderRouterTypeAssociatedPhysicalConnections(TeaModel):
    def __init__(self, associated_physical_connection=None):
        self.associated_physical_connection = associated_physical_connection

    def validate(self):
        self.validate_required(self.associated_physical_connection, 'associated_physical_connection')
        if self.associated_physical_connection:
            for k in self.associated_physical_connection:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['AssociatedPhysicalConnection'] = []
        if self.associated_physical_connection is not None:
            for k in self.associated_physical_connection:
                result['AssociatedPhysicalConnection'].append(k.to_map() if k else None)
        else:
            result['AssociatedPhysicalConnection'] = None
        return result

    def from_map(self, map={}):
        self.associated_physical_connection = []
        if map.get('AssociatedPhysicalConnection') is not None:
            for k in map.get('AssociatedPhysicalConnection'):
                temp_model = DescribeVirtualBorderRoutersResponseVirtualBorderRouterSetVirtualBorderRouterTypeAssociatedPhysicalConnectionsAssociatedPhysicalConnection()
                self.associated_physical_connection.append(temp_model.from_map(k))
        else:
            self.associated_physical_connection = None
        return self


class DescribeVirtualBorderRoutersResponseVirtualBorderRouterSetVirtualBorderRouterTypeAssociatedCensAssociatedCen(TeaModel):
    def __init__(self, cen_id=None, cen_owner_id=None, cen_status=None):
        self.cen_id = cen_id
        self.cen_owner_id = cen_owner_id
        self.cen_status = cen_status

    def validate(self):
        self.validate_required(self.cen_id, 'cen_id')
        self.validate_required(self.cen_owner_id, 'cen_owner_id')
        self.validate_required(self.cen_status, 'cen_status')

    def to_map(self):
        result = {}
        result['CenId'] = self.cen_id
        result['CenOwnerId'] = self.cen_owner_id
        result['CenStatus'] = self.cen_status
        return result

    def from_map(self, map={}):
        self.cen_id = map.get('CenId')
        self.cen_owner_id = map.get('CenOwnerId')
        self.cen_status = map.get('CenStatus')
        return self


class DescribeVirtualBorderRoutersResponseVirtualBorderRouterSetVirtualBorderRouterTypeAssociatedCens(TeaModel):
    def __init__(self, associated_cen=None):
        self.associated_cen = associated_cen

    def validate(self):
        self.validate_required(self.associated_cen, 'associated_cen')
        if self.associated_cen:
            for k in self.associated_cen:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['AssociatedCen'] = []
        if self.associated_cen is not None:
            for k in self.associated_cen:
                result['AssociatedCen'].append(k.to_map() if k else None)
        else:
            result['AssociatedCen'] = None
        return result

    def from_map(self, map={}):
        self.associated_cen = []
        if map.get('AssociatedCen') is not None:
            for k in map.get('AssociatedCen'):
                temp_model = DescribeVirtualBorderRoutersResponseVirtualBorderRouterSetVirtualBorderRouterTypeAssociatedCensAssociatedCen()
                self.associated_cen.append(temp_model.from_map(k))
        else:
            self.associated_cen = None
        return self


class DescribeVirtualBorderRoutersResponseVirtualBorderRouterSetVirtualBorderRouterType(TeaModel):
    def __init__(self, vbr_id=None, creation_time=None, activation_time=None, termination_time=None,
                 recovery_time=None, status=None, vlan_id=None, circuit_code=None, route_table_id=None, vlan_interface_id=None,
                 local_gateway_ip=None, peer_gateway_ip=None, peering_subnet_mask=None, physical_connection_id=None,
                 physical_connection_status=None, physical_connection_business_status=None, physical_connection_owner_uid=None,
                 access_point_id=None, name=None, description=None, pconn_vbr_expire_time=None, ecc_id=None, type=None,
                 min_tx_interval=None, min_rx_interval=None, detect_multiplier=None, local_ipv_6gateway_ip=None,
                 peer_ipv_6gateway_ip=None, peering_ipv_6subnet_mask=None, enable_ipv_6=None, associated_physical_connections=None,
                 associated_cens=None):
        self.vbr_id = vbr_id
        self.creation_time = creation_time
        self.activation_time = activation_time
        self.termination_time = termination_time
        self.recovery_time = recovery_time
        self.status = status
        self.vlan_id = vlan_id
        self.circuit_code = circuit_code
        self.route_table_id = route_table_id
        self.vlan_interface_id = vlan_interface_id
        self.local_gateway_ip = local_gateway_ip
        self.peer_gateway_ip = peer_gateway_ip
        self.peering_subnet_mask = peering_subnet_mask
        self.physical_connection_id = physical_connection_id
        self.physical_connection_status = physical_connection_status
        self.physical_connection_business_status = physical_connection_business_status
        self.physical_connection_owner_uid = physical_connection_owner_uid
        self.access_point_id = access_point_id
        self.name = name
        self.description = description
        self.pconn_vbr_expire_time = pconn_vbr_expire_time
        self.ecc_id = ecc_id
        self.type = type
        self.min_tx_interval = min_tx_interval
        self.min_rx_interval = min_rx_interval
        self.detect_multiplier = detect_multiplier
        self.local_ipv_6gateway_ip = local_ipv_6gateway_ip
        self.peer_ipv_6gateway_ip = peer_ipv_6gateway_ip
        self.peering_ipv_6subnet_mask = peering_ipv_6subnet_mask
        self.enable_ipv_6 = enable_ipv_6
        self.associated_physical_connections = associated_physical_connections  # type: DescribeVirtualBorderRoutersResponseVirtualBorderRouterSetVirtualBorderRouterTypeAssociatedPhysicalConnections
        self.associated_cens = associated_cens  # type: DescribeVirtualBorderRoutersResponseVirtualBorderRouterSetVirtualBorderRouterTypeAssociatedCens

    def validate(self):
        self.validate_required(self.vbr_id, 'vbr_id')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.activation_time, 'activation_time')
        self.validate_required(self.termination_time, 'termination_time')
        self.validate_required(self.recovery_time, 'recovery_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.vlan_id, 'vlan_id')
        self.validate_required(self.circuit_code, 'circuit_code')
        self.validate_required(self.route_table_id, 'route_table_id')
        self.validate_required(self.vlan_interface_id, 'vlan_interface_id')
        self.validate_required(self.local_gateway_ip, 'local_gateway_ip')
        self.validate_required(self.peer_gateway_ip, 'peer_gateway_ip')
        self.validate_required(self.peering_subnet_mask, 'peering_subnet_mask')
        self.validate_required(self.physical_connection_id, 'physical_connection_id')
        self.validate_required(self.physical_connection_status, 'physical_connection_status')
        self.validate_required(self.physical_connection_business_status, 'physical_connection_business_status')
        self.validate_required(self.physical_connection_owner_uid, 'physical_connection_owner_uid')
        self.validate_required(self.access_point_id, 'access_point_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.pconn_vbr_expire_time, 'pconn_vbr_expire_time')
        self.validate_required(self.ecc_id, 'ecc_id')
        self.validate_required(self.type, 'type')
        self.validate_required(self.min_tx_interval, 'min_tx_interval')
        self.validate_required(self.min_rx_interval, 'min_rx_interval')
        self.validate_required(self.detect_multiplier, 'detect_multiplier')
        self.validate_required(self.local_ipv_6gateway_ip, 'local_ipv_6gateway_ip')
        self.validate_required(self.peer_ipv_6gateway_ip, 'peer_ipv_6gateway_ip')
        self.validate_required(self.peering_ipv_6subnet_mask, 'peering_ipv_6subnet_mask')
        self.validate_required(self.enable_ipv_6, 'enable_ipv_6')
        self.validate_required(self.associated_physical_connections, 'associated_physical_connections')
        if self.associated_physical_connections:
            self.associated_physical_connections.validate()
        self.validate_required(self.associated_cens, 'associated_cens')
        if self.associated_cens:
            self.associated_cens.validate()

    def to_map(self):
        result = {}
        result['VbrId'] = self.vbr_id
        result['CreationTime'] = self.creation_time
        result['ActivationTime'] = self.activation_time
        result['TerminationTime'] = self.termination_time
        result['RecoveryTime'] = self.recovery_time
        result['Status'] = self.status
        result['VlanId'] = self.vlan_id
        result['CircuitCode'] = self.circuit_code
        result['RouteTableId'] = self.route_table_id
        result['VlanInterfaceId'] = self.vlan_interface_id
        result['LocalGatewayIp'] = self.local_gateway_ip
        result['PeerGatewayIp'] = self.peer_gateway_ip
        result['PeeringSubnetMask'] = self.peering_subnet_mask
        result['PhysicalConnectionId'] = self.physical_connection_id
        result['PhysicalConnectionStatus'] = self.physical_connection_status
        result['PhysicalConnectionBusinessStatus'] = self.physical_connection_business_status
        result['PhysicalConnectionOwnerUid'] = self.physical_connection_owner_uid
        result['AccessPointId'] = self.access_point_id
        result['Name'] = self.name
        result['Description'] = self.description
        result['PConnVbrExpireTime'] = self.pconn_vbr_expire_time
        result['EccId'] = self.ecc_id
        result['Type'] = self.type
        result['MinTxInterval'] = self.min_tx_interval
        result['MinRxInterval'] = self.min_rx_interval
        result['DetectMultiplier'] = self.detect_multiplier
        result['LocalIpv6GatewayIp'] = self.local_ipv_6gateway_ip
        result['PeerIpv6GatewayIp'] = self.peer_ipv_6gateway_ip
        result['PeeringIpv6SubnetMask'] = self.peering_ipv_6subnet_mask
        result['EnableIpv6'] = self.enable_ipv_6
        if self.associated_physical_connections is not None:
            result['AssociatedPhysicalConnections'] = self.associated_physical_connections.to_map()
        else:
            result['AssociatedPhysicalConnections'] = None
        if self.associated_cens is not None:
            result['AssociatedCens'] = self.associated_cens.to_map()
        else:
            result['AssociatedCens'] = None
        return result

    def from_map(self, map={}):
        self.vbr_id = map.get('VbrId')
        self.creation_time = map.get('CreationTime')
        self.activation_time = map.get('ActivationTime')
        self.termination_time = map.get('TerminationTime')
        self.recovery_time = map.get('RecoveryTime')
        self.status = map.get('Status')
        self.vlan_id = map.get('VlanId')
        self.circuit_code = map.get('CircuitCode')
        self.route_table_id = map.get('RouteTableId')
        self.vlan_interface_id = map.get('VlanInterfaceId')
        self.local_gateway_ip = map.get('LocalGatewayIp')
        self.peer_gateway_ip = map.get('PeerGatewayIp')
        self.peering_subnet_mask = map.get('PeeringSubnetMask')
        self.physical_connection_id = map.get('PhysicalConnectionId')
        self.physical_connection_status = map.get('PhysicalConnectionStatus')
        self.physical_connection_business_status = map.get('PhysicalConnectionBusinessStatus')
        self.physical_connection_owner_uid = map.get('PhysicalConnectionOwnerUid')
        self.access_point_id = map.get('AccessPointId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.pconn_vbr_expire_time = map.get('PConnVbrExpireTime')
        self.ecc_id = map.get('EccId')
        self.type = map.get('Type')
        self.min_tx_interval = map.get('MinTxInterval')
        self.min_rx_interval = map.get('MinRxInterval')
        self.detect_multiplier = map.get('DetectMultiplier')
        self.local_ipv_6gateway_ip = map.get('LocalIpv6GatewayIp')
        self.peer_ipv_6gateway_ip = map.get('PeerIpv6GatewayIp')
        self.peering_ipv_6subnet_mask = map.get('PeeringIpv6SubnetMask')
        self.enable_ipv_6 = map.get('EnableIpv6')
        if map.get('AssociatedPhysicalConnections') is not None:
            temp_model = DescribeVirtualBorderRoutersResponseVirtualBorderRouterSetVirtualBorderRouterTypeAssociatedPhysicalConnections()
            self.associated_physical_connections = temp_model.from_map(map['AssociatedPhysicalConnections'])
        else:
            self.associated_physical_connections = None
        if map.get('AssociatedCens') is not None:
            temp_model = DescribeVirtualBorderRoutersResponseVirtualBorderRouterSetVirtualBorderRouterTypeAssociatedCens()
            self.associated_cens = temp_model.from_map(map['AssociatedCens'])
        else:
            self.associated_cens = None
        return self


class DescribeVirtualBorderRoutersResponseVirtualBorderRouterSet(TeaModel):
    def __init__(self, virtual_border_router_type=None):
        self.virtual_border_router_type = virtual_border_router_type

    def validate(self):
        self.validate_required(self.virtual_border_router_type, 'virtual_border_router_type')
        if self.virtual_border_router_type:
            for k in self.virtual_border_router_type:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['VirtualBorderRouterType'] = []
        if self.virtual_border_router_type is not None:
            for k in self.virtual_border_router_type:
                result['VirtualBorderRouterType'].append(k.to_map() if k else None)
        else:
            result['VirtualBorderRouterType'] = None
        return result

    def from_map(self, map={}):
        self.virtual_border_router_type = []
        if map.get('VirtualBorderRouterType') is not None:
            for k in map.get('VirtualBorderRouterType'):
                temp_model = DescribeVirtualBorderRoutersResponseVirtualBorderRouterSetVirtualBorderRouterType()
                self.virtual_border_router_type.append(temp_model.from_map(k))
        else:
            self.virtual_border_router_type = None
        return self


class DescribeRouteTablesRequest(TeaModel):
    def __init__(self, region_id=None, vrouter_id=None, route_table_id=None, router_type=None, router_id=None,
                 type=None, route_table_name=None, resource_group_id=None, page_number=None, page_size=None):
        self.region_id = region_id
        self.vrouter_id = vrouter_id
        self.route_table_id = route_table_id
        self.router_type = router_type
        self.router_id = router_id
        self.type = type
        self.route_table_name = route_table_name
        self.resource_group_id = resource_group_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VRouterId'] = self.vrouter_id
        result['RouteTableId'] = self.route_table_id
        result['RouterType'] = self.router_type
        result['RouterId'] = self.router_id
        result['Type'] = self.type
        result['RouteTableName'] = self.route_table_name
        result['ResourceGroupId'] = self.resource_group_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vrouter_id = map.get('VRouterId')
        self.route_table_id = map.get('RouteTableId')
        self.router_type = map.get('RouterType')
        self.router_id = map.get('RouterId')
        self.type = map.get('Type')
        self.route_table_name = map.get('RouteTableName')
        self.resource_group_id = map.get('ResourceGroupId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeRouteTablesResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, route_tables=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.route_tables = route_tables  # type: DescribeRouteTablesResponseRouteTables

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.route_tables, 'route_tables')
        if self.route_tables:
            self.route_tables.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.route_tables is not None:
            result['RouteTables'] = self.route_tables.to_map()
        else:
            result['RouteTables'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('RouteTables') is not None:
            temp_model = DescribeRouteTablesResponseRouteTables()
            self.route_tables = temp_model.from_map(map['RouteTables'])
        else:
            self.route_tables = None
        return self


class DescribeRouteTablesResponseRouteTablesRouteTableRouteEntrysRouteEntryNextHopsNextHop(TeaModel):
    def __init__(self, next_hop_type=None, next_hop_id=None, enabled=None, weight=None, next_hop_region_id=None,
                 next_hop_oppsite_type=None, next_hop_oppsite_instance_id=None, next_hop_oppsite_region_id=None):
        self.next_hop_type = next_hop_type
        self.next_hop_id = next_hop_id
        self.enabled = enabled
        self.weight = weight
        self.next_hop_region_id = next_hop_region_id
        self.next_hop_oppsite_type = next_hop_oppsite_type
        self.next_hop_oppsite_instance_id = next_hop_oppsite_instance_id
        self.next_hop_oppsite_region_id = next_hop_oppsite_region_id

    def validate(self):
        self.validate_required(self.next_hop_type, 'next_hop_type')
        self.validate_required(self.next_hop_id, 'next_hop_id')
        self.validate_required(self.enabled, 'enabled')
        self.validate_required(self.weight, 'weight')
        self.validate_required(self.next_hop_region_id, 'next_hop_region_id')
        self.validate_required(self.next_hop_oppsite_type, 'next_hop_oppsite_type')
        self.validate_required(self.next_hop_oppsite_instance_id, 'next_hop_oppsite_instance_id')
        self.validate_required(self.next_hop_oppsite_region_id, 'next_hop_oppsite_region_id')

    def to_map(self):
        result = {}
        result['NextHopType'] = self.next_hop_type
        result['NextHopId'] = self.next_hop_id
        result['Enabled'] = self.enabled
        result['Weight'] = self.weight
        result['NextHopRegionId'] = self.next_hop_region_id
        result['NextHopOppsiteType'] = self.next_hop_oppsite_type
        result['NextHopOppsiteInstanceId'] = self.next_hop_oppsite_instance_id
        result['NextHopOppsiteRegionId'] = self.next_hop_oppsite_region_id
        return result

    def from_map(self, map={}):
        self.next_hop_type = map.get('NextHopType')
        self.next_hop_id = map.get('NextHopId')
        self.enabled = map.get('Enabled')
        self.weight = map.get('Weight')
        self.next_hop_region_id = map.get('NextHopRegionId')
        self.next_hop_oppsite_type = map.get('NextHopOppsiteType')
        self.next_hop_oppsite_instance_id = map.get('NextHopOppsiteInstanceId')
        self.next_hop_oppsite_region_id = map.get('NextHopOppsiteRegionId')
        return self


class DescribeRouteTablesResponseRouteTablesRouteTableRouteEntrysRouteEntryNextHops(TeaModel):
    def __init__(self, next_hop=None):
        self.next_hop = next_hop

    def validate(self):
        self.validate_required(self.next_hop, 'next_hop')
        if self.next_hop:
            for k in self.next_hop:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['NextHop'] = []
        if self.next_hop is not None:
            for k in self.next_hop:
                result['NextHop'].append(k.to_map() if k else None)
        else:
            result['NextHop'] = None
        return result

    def from_map(self, map={}):
        self.next_hop = []
        if map.get('NextHop') is not None:
            for k in map.get('NextHop'):
                temp_model = DescribeRouteTablesResponseRouteTablesRouteTableRouteEntrysRouteEntryNextHopsNextHop()
                self.next_hop.append(temp_model.from_map(k))
        else:
            self.next_hop = None
        return self


class DescribeRouteTablesResponseRouteTablesRouteTableRouteEntrysRouteEntry(TeaModel):
    def __init__(self, route_table_id=None, destination_cidr_block=None, type=None, status=None, instance_id=None,
                 next_hop_type=None, route_entry_name=None, description=None, route_entry_id=None, next_hop_region_id=None,
                 next_hop_oppsite_type=None, next_hop_oppsite_instance_id=None, next_hop_oppsite_region_id=None,
                 private_ip_address=None, next_hops=None):
        self.route_table_id = route_table_id
        self.destination_cidr_block = destination_cidr_block
        self.type = type
        self.status = status
        self.instance_id = instance_id
        self.next_hop_type = next_hop_type
        self.route_entry_name = route_entry_name
        self.description = description
        self.route_entry_id = route_entry_id
        self.next_hop_region_id = next_hop_region_id
        self.next_hop_oppsite_type = next_hop_oppsite_type
        self.next_hop_oppsite_instance_id = next_hop_oppsite_instance_id
        self.next_hop_oppsite_region_id = next_hop_oppsite_region_id
        self.private_ip_address = private_ip_address
        self.next_hops = next_hops  # type: DescribeRouteTablesResponseRouteTablesRouteTableRouteEntrysRouteEntryNextHops

    def validate(self):
        self.validate_required(self.route_table_id, 'route_table_id')
        self.validate_required(self.destination_cidr_block, 'destination_cidr_block')
        self.validate_required(self.type, 'type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.next_hop_type, 'next_hop_type')
        self.validate_required(self.route_entry_name, 'route_entry_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.route_entry_id, 'route_entry_id')
        self.validate_required(self.next_hop_region_id, 'next_hop_region_id')
        self.validate_required(self.next_hop_oppsite_type, 'next_hop_oppsite_type')
        self.validate_required(self.next_hop_oppsite_instance_id, 'next_hop_oppsite_instance_id')
        self.validate_required(self.next_hop_oppsite_region_id, 'next_hop_oppsite_region_id')
        self.validate_required(self.private_ip_address, 'private_ip_address')
        self.validate_required(self.next_hops, 'next_hops')
        if self.next_hops:
            self.next_hops.validate()

    def to_map(self):
        result = {}
        result['RouteTableId'] = self.route_table_id
        result['DestinationCidrBlock'] = self.destination_cidr_block
        result['Type'] = self.type
        result['Status'] = self.status
        result['InstanceId'] = self.instance_id
        result['NextHopType'] = self.next_hop_type
        result['RouteEntryName'] = self.route_entry_name
        result['Description'] = self.description
        result['RouteEntryId'] = self.route_entry_id
        result['NextHopRegionId'] = self.next_hop_region_id
        result['NextHopOppsiteType'] = self.next_hop_oppsite_type
        result['NextHopOppsiteInstanceId'] = self.next_hop_oppsite_instance_id
        result['NextHopOppsiteRegionId'] = self.next_hop_oppsite_region_id
        result['PrivateIpAddress'] = self.private_ip_address
        if self.next_hops is not None:
            result['NextHops'] = self.next_hops.to_map()
        else:
            result['NextHops'] = None
        return result

    def from_map(self, map={}):
        self.route_table_id = map.get('RouteTableId')
        self.destination_cidr_block = map.get('DestinationCidrBlock')
        self.type = map.get('Type')
        self.status = map.get('Status')
        self.instance_id = map.get('InstanceId')
        self.next_hop_type = map.get('NextHopType')
        self.route_entry_name = map.get('RouteEntryName')
        self.description = map.get('Description')
        self.route_entry_id = map.get('RouteEntryId')
        self.next_hop_region_id = map.get('NextHopRegionId')
        self.next_hop_oppsite_type = map.get('NextHopOppsiteType')
        self.next_hop_oppsite_instance_id = map.get('NextHopOppsiteInstanceId')
        self.next_hop_oppsite_region_id = map.get('NextHopOppsiteRegionId')
        self.private_ip_address = map.get('PrivateIpAddress')
        if map.get('NextHops') is not None:
            temp_model = DescribeRouteTablesResponseRouteTablesRouteTableRouteEntrysRouteEntryNextHops()
            self.next_hops = temp_model.from_map(map['NextHops'])
        else:
            self.next_hops = None
        return self


class DescribeRouteTablesResponseRouteTablesRouteTableRouteEntrys(TeaModel):
    def __init__(self, route_entry=None):
        self.route_entry = route_entry

    def validate(self):
        self.validate_required(self.route_entry, 'route_entry')
        if self.route_entry:
            for k in self.route_entry:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RouteEntry'] = []
        if self.route_entry is not None:
            for k in self.route_entry:
                result['RouteEntry'].append(k.to_map() if k else None)
        else:
            result['RouteEntry'] = None
        return result

    def from_map(self, map={}):
        self.route_entry = []
        if map.get('RouteEntry') is not None:
            for k in map.get('RouteEntry'):
                temp_model = DescribeRouteTablesResponseRouteTablesRouteTableRouteEntrysRouteEntry()
                self.route_entry.append(temp_model.from_map(k))
        else:
            self.route_entry = None
        return self


class DescribeRouteTablesResponseRouteTablesRouteTableVSwitchIds(TeaModel):
    def __init__(self, v_switch_id=None):
        # VSwitchId
        self.v_switch_id = v_switch_id

    def validate(self):
        self.validate_required(self.v_switch_id, 'v_switch_id')

    def to_map(self):
        result = {}
        result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, map={}):
        self.v_switch_id = map.get('VSwitchId')
        return self


class DescribeRouteTablesResponseRouteTablesRouteTable(TeaModel):
    def __init__(self, vrouter_id=None, route_table_id=None, route_table_type=None, creation_time=None,
                 resource_group_id=None, status=None, route_entrys=None, v_switch_ids=None):
        self.vrouter_id = vrouter_id
        self.route_table_id = route_table_id
        self.route_table_type = route_table_type
        self.creation_time = creation_time
        self.resource_group_id = resource_group_id
        self.status = status
        self.route_entrys = route_entrys  # type: DescribeRouteTablesResponseRouteTablesRouteTableRouteEntrys
        self.v_switch_ids = v_switch_ids  # type: DescribeRouteTablesResponseRouteTablesRouteTableVSwitchIds

    def validate(self):
        self.validate_required(self.vrouter_id, 'vrouter_id')
        self.validate_required(self.route_table_id, 'route_table_id')
        self.validate_required(self.route_table_type, 'route_table_type')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.route_entrys, 'route_entrys')
        if self.route_entrys:
            self.route_entrys.validate()
        self.validate_required(self.v_switch_ids, 'v_switch_ids')
        if self.v_switch_ids:
            self.v_switch_ids.validate()

    def to_map(self):
        result = {}
        result['VRouterId'] = self.vrouter_id
        result['RouteTableId'] = self.route_table_id
        result['RouteTableType'] = self.route_table_type
        result['CreationTime'] = self.creation_time
        result['ResourceGroupId'] = self.resource_group_id
        result['Status'] = self.status
        if self.route_entrys is not None:
            result['RouteEntrys'] = self.route_entrys.to_map()
        else:
            result['RouteEntrys'] = None
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids.to_map()
        else:
            result['VSwitchIds'] = None
        return result

    def from_map(self, map={}):
        self.vrouter_id = map.get('VRouterId')
        self.route_table_id = map.get('RouteTableId')
        self.route_table_type = map.get('RouteTableType')
        self.creation_time = map.get('CreationTime')
        self.resource_group_id = map.get('ResourceGroupId')
        self.status = map.get('Status')
        if map.get('RouteEntrys') is not None:
            temp_model = DescribeRouteTablesResponseRouteTablesRouteTableRouteEntrys()
            self.route_entrys = temp_model.from_map(map['RouteEntrys'])
        else:
            self.route_entrys = None
        if map.get('VSwitchIds') is not None:
            temp_model = DescribeRouteTablesResponseRouteTablesRouteTableVSwitchIds()
            self.v_switch_ids = temp_model.from_map(map['VSwitchIds'])
        else:
            self.v_switch_ids = None
        return self


class DescribeRouteTablesResponseRouteTables(TeaModel):
    def __init__(self, route_table=None):
        self.route_table = route_table

    def validate(self):
        self.validate_required(self.route_table, 'route_table')
        if self.route_table:
            for k in self.route_table:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RouteTable'] = []
        if self.route_table is not None:
            for k in self.route_table:
                result['RouteTable'].append(k.to_map() if k else None)
        else:
            result['RouteTable'] = None
        return result

    def from_map(self, map={}):
        self.route_table = []
        if map.get('RouteTable') is not None:
            for k in map.get('RouteTable'):
                temp_model = DescribeRouteTablesResponseRouteTablesRouteTable()
                self.route_table.append(temp_model.from_map(k))
        else:
            self.route_table = None
        return self


class DescribeRouterInterfacesRequest(TeaModel):
    def __init__(self, region_id=None, include_reservation_data=None, page_number=None, page_size=None, filter=None):
        self.region_id = region_id
        self.include_reservation_data = include_reservation_data
        self.page_number = page_number
        self.page_size = page_size
        self.filter = filter

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['IncludeReservationData'] = self.include_reservation_data
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        else:
            result['Filter'] = None
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.include_reservation_data = map.get('IncludeReservationData')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.filter = []
        if map.get('Filter') is not None:
            for k in map.get('Filter'):
                temp_model = DescribeRouterInterfacesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        else:
            self.filter = None
        return self


class DescribeRouterInterfacesRequestFilter(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class DescribeRouterInterfacesResponse(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None,
                 router_interface_set=None):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.router_interface_set = router_interface_set  # type: DescribeRouterInterfacesResponseRouterInterfaceSet

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.router_interface_set, 'router_interface_set')
        if self.router_interface_set:
            self.router_interface_set.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        if self.router_interface_set is not None:
            result['RouterInterfaceSet'] = self.router_interface_set.to_map()
        else:
            result['RouterInterfaceSet'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        if map.get('RouterInterfaceSet') is not None:
            temp_model = DescribeRouterInterfacesResponseRouterInterfaceSet()
            self.router_interface_set = temp_model.from_map(map['RouterInterfaceSet'])
        else:
            self.router_interface_set = None
        return self


class DescribeRouterInterfacesResponseRouterInterfaceSetRouterInterfaceType(TeaModel):
    def __init__(self, router_interface_id=None, opposite_region_id=None, role=None, spec=None, name=None,
                 description=None, router_id=None, router_type=None, creation_time=None, end_time=None, charge_type=None,
                 status=None, business_status=None, connected_time=None, opposite_interface_id=None,
                 opposite_interface_spec=None, opposite_interface_status=None, opposite_interface_business_status=None,
                 opposite_router_id=None, opposite_router_type=None, opposite_interface_owner_id=None, access_point_id=None,
                 opposite_access_point_id=None, health_check_source_ip=None, health_check_target_ip=None, opposite_vpc_instance_id=None,
                 bandwidth=None, vpc_instance_id=None, opposite_bandwidth=None, has_reservation_data=None,
                 reservation_bandwidth=None, reservation_internet_charge_type=None, reservation_active_time=None,
                 reservation_order_type=None, cross_border=None, hc_threshold=None, hc_rate=None):
        self.router_interface_id = router_interface_id
        self.opposite_region_id = opposite_region_id
        self.role = role
        self.spec = spec
        self.name = name
        self.description = description
        self.router_id = router_id
        self.router_type = router_type
        self.creation_time = creation_time
        self.end_time = end_time
        self.charge_type = charge_type
        self.status = status
        self.business_status = business_status
        self.connected_time = connected_time
        self.opposite_interface_id = opposite_interface_id
        self.opposite_interface_spec = opposite_interface_spec
        self.opposite_interface_status = opposite_interface_status
        self.opposite_interface_business_status = opposite_interface_business_status
        self.opposite_router_id = opposite_router_id
        self.opposite_router_type = opposite_router_type
        self.opposite_interface_owner_id = opposite_interface_owner_id
        self.access_point_id = access_point_id
        self.opposite_access_point_id = opposite_access_point_id
        self.health_check_source_ip = health_check_source_ip
        self.health_check_target_ip = health_check_target_ip
        self.opposite_vpc_instance_id = opposite_vpc_instance_id
        self.bandwidth = bandwidth
        self.vpc_instance_id = vpc_instance_id
        self.opposite_bandwidth = opposite_bandwidth
        self.has_reservation_data = has_reservation_data
        self.reservation_bandwidth = reservation_bandwidth
        self.reservation_internet_charge_type = reservation_internet_charge_type
        self.reservation_active_time = reservation_active_time
        self.reservation_order_type = reservation_order_type
        self.cross_border = cross_border
        self.hc_threshold = hc_threshold
        self.hc_rate = hc_rate

    def validate(self):
        self.validate_required(self.router_interface_id, 'router_interface_id')
        self.validate_required(self.opposite_region_id, 'opposite_region_id')
        self.validate_required(self.role, 'role')
        self.validate_required(self.spec, 'spec')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.router_id, 'router_id')
        self.validate_required(self.router_type, 'router_type')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.charge_type, 'charge_type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.business_status, 'business_status')
        self.validate_required(self.connected_time, 'connected_time')
        self.validate_required(self.opposite_interface_id, 'opposite_interface_id')
        self.validate_required(self.opposite_interface_spec, 'opposite_interface_spec')
        self.validate_required(self.opposite_interface_status, 'opposite_interface_status')
        self.validate_required(self.opposite_interface_business_status, 'opposite_interface_business_status')
        self.validate_required(self.opposite_router_id, 'opposite_router_id')
        self.validate_required(self.opposite_router_type, 'opposite_router_type')
        self.validate_required(self.opposite_interface_owner_id, 'opposite_interface_owner_id')
        self.validate_required(self.access_point_id, 'access_point_id')
        self.validate_required(self.opposite_access_point_id, 'opposite_access_point_id')
        self.validate_required(self.health_check_source_ip, 'health_check_source_ip')
        self.validate_required(self.health_check_target_ip, 'health_check_target_ip')
        self.validate_required(self.opposite_vpc_instance_id, 'opposite_vpc_instance_id')
        self.validate_required(self.bandwidth, 'bandwidth')
        self.validate_required(self.vpc_instance_id, 'vpc_instance_id')
        self.validate_required(self.opposite_bandwidth, 'opposite_bandwidth')
        self.validate_required(self.has_reservation_data, 'has_reservation_data')
        self.validate_required(self.reservation_bandwidth, 'reservation_bandwidth')
        self.validate_required(self.reservation_internet_charge_type, 'reservation_internet_charge_type')
        self.validate_required(self.reservation_active_time, 'reservation_active_time')
        self.validate_required(self.reservation_order_type, 'reservation_order_type')
        self.validate_required(self.cross_border, 'cross_border')
        self.validate_required(self.hc_threshold, 'hc_threshold')
        self.validate_required(self.hc_rate, 'hc_rate')

    def to_map(self):
        result = {}
        result['RouterInterfaceId'] = self.router_interface_id
        result['OppositeRegionId'] = self.opposite_region_id
        result['Role'] = self.role
        result['Spec'] = self.spec
        result['Name'] = self.name
        result['Description'] = self.description
        result['RouterId'] = self.router_id
        result['RouterType'] = self.router_type
        result['CreationTime'] = self.creation_time
        result['EndTime'] = self.end_time
        result['ChargeType'] = self.charge_type
        result['Status'] = self.status
        result['BusinessStatus'] = self.business_status
        result['ConnectedTime'] = self.connected_time
        result['OppositeInterfaceId'] = self.opposite_interface_id
        result['OppositeInterfaceSpec'] = self.opposite_interface_spec
        result['OppositeInterfaceStatus'] = self.opposite_interface_status
        result['OppositeInterfaceBusinessStatus'] = self.opposite_interface_business_status
        result['OppositeRouterId'] = self.opposite_router_id
        result['OppositeRouterType'] = self.opposite_router_type
        result['OppositeInterfaceOwnerId'] = self.opposite_interface_owner_id
        result['AccessPointId'] = self.access_point_id
        result['OppositeAccessPointId'] = self.opposite_access_point_id
        result['HealthCheckSourceIp'] = self.health_check_source_ip
        result['HealthCheckTargetIp'] = self.health_check_target_ip
        result['OppositeVpcInstanceId'] = self.opposite_vpc_instance_id
        result['Bandwidth'] = self.bandwidth
        result['VpcInstanceId'] = self.vpc_instance_id
        result['OppositeBandwidth'] = self.opposite_bandwidth
        result['HasReservationData'] = self.has_reservation_data
        result['ReservationBandwidth'] = self.reservation_bandwidth
        result['ReservationInternetChargeType'] = self.reservation_internet_charge_type
        result['ReservationActiveTime'] = self.reservation_active_time
        result['ReservationOrderType'] = self.reservation_order_type
        result['CrossBorder'] = self.cross_border
        result['HcThreshold'] = self.hc_threshold
        result['HcRate'] = self.hc_rate
        return result

    def from_map(self, map={}):
        self.router_interface_id = map.get('RouterInterfaceId')
        self.opposite_region_id = map.get('OppositeRegionId')
        self.role = map.get('Role')
        self.spec = map.get('Spec')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.router_id = map.get('RouterId')
        self.router_type = map.get('RouterType')
        self.creation_time = map.get('CreationTime')
        self.end_time = map.get('EndTime')
        self.charge_type = map.get('ChargeType')
        self.status = map.get('Status')
        self.business_status = map.get('BusinessStatus')
        self.connected_time = map.get('ConnectedTime')
        self.opposite_interface_id = map.get('OppositeInterfaceId')
        self.opposite_interface_spec = map.get('OppositeInterfaceSpec')
        self.opposite_interface_status = map.get('OppositeInterfaceStatus')
        self.opposite_interface_business_status = map.get('OppositeInterfaceBusinessStatus')
        self.opposite_router_id = map.get('OppositeRouterId')
        self.opposite_router_type = map.get('OppositeRouterType')
        self.opposite_interface_owner_id = map.get('OppositeInterfaceOwnerId')
        self.access_point_id = map.get('AccessPointId')
        self.opposite_access_point_id = map.get('OppositeAccessPointId')
        self.health_check_source_ip = map.get('HealthCheckSourceIp')
        self.health_check_target_ip = map.get('HealthCheckTargetIp')
        self.opposite_vpc_instance_id = map.get('OppositeVpcInstanceId')
        self.bandwidth = map.get('Bandwidth')
        self.vpc_instance_id = map.get('VpcInstanceId')
        self.opposite_bandwidth = map.get('OppositeBandwidth')
        self.has_reservation_data = map.get('HasReservationData')
        self.reservation_bandwidth = map.get('ReservationBandwidth')
        self.reservation_internet_charge_type = map.get('ReservationInternetChargeType')
        self.reservation_active_time = map.get('ReservationActiveTime')
        self.reservation_order_type = map.get('ReservationOrderType')
        self.cross_border = map.get('CrossBorder')
        self.hc_threshold = map.get('HcThreshold')
        self.hc_rate = map.get('HcRate')
        return self


class DescribeRouterInterfacesResponseRouterInterfaceSet(TeaModel):
    def __init__(self, router_interface_type=None):
        self.router_interface_type = router_interface_type

    def validate(self):
        self.validate_required(self.router_interface_type, 'router_interface_type')
        if self.router_interface_type:
            for k in self.router_interface_type:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RouterInterfaceType'] = []
        if self.router_interface_type is not None:
            for k in self.router_interface_type:
                result['RouterInterfaceType'].append(k.to_map() if k else None)
        else:
            result['RouterInterfaceType'] = None
        return result

    def from_map(self, map={}):
        self.router_interface_type = []
        if map.get('RouterInterfaceType') is not None:
            for k in map.get('RouterInterfaceType'):
                temp_model = DescribeRouterInterfacesResponseRouterInterfaceSetRouterInterfaceType()
                self.router_interface_type.append(temp_model.from_map(k))
        else:
            self.router_interface_type = None
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, accept_language=None):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, map={}):
        self.accept_language = map.get('AcceptLanguage')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, request_id=None, regions=None):
        self.request_id = request_id
        self.regions = regions  # type: DescribeRegionsResponseRegions

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.regions, 'regions')
        if self.regions:
            self.regions.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        else:
            result['Regions'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Regions') is not None:
            temp_model = DescribeRegionsResponseRegions()
            self.regions = temp_model.from_map(map['Regions'])
        else:
            self.regions = None
        return self


class DescribeRegionsResponseRegionsRegion(TeaModel):
    def __init__(self, region_id=None, local_name=None, region_endpoint=None):
        self.region_id = region_id
        self.local_name = local_name
        self.region_endpoint = region_endpoint

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.local_name, 'local_name')
        self.validate_required(self.region_endpoint, 'region_endpoint')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['LocalName'] = self.local_name
        result['RegionEndpoint'] = self.region_endpoint
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.local_name = map.get('LocalName')
        self.region_endpoint = map.get('RegionEndpoint')
        return self


class DescribeRegionsResponseRegions(TeaModel):
    def __init__(self, region=None):
        self.region = region

    def validate(self):
        self.validate_required(self.region, 'region')
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        else:
            result['Region'] = None
        return result

    def from_map(self, map={}):
        self.region = []
        if map.get('Region') is not None:
            for k in map.get('Region'):
                temp_model = DescribeRegionsResponseRegionsRegion()
                self.region.append(temp_model.from_map(k))
        else:
            self.region = None
        return self


class DescribePhysicalConnectionsRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None, filter=None, include_reservation_data=None,
                 client_token=None):
        # description: The ID of the region where the leased line is deployed. You can obtain the region ID by calling the [DescribeRegions](~~36063~~); 
        self.region_id = region_id
        # description: Optional. The page number of the physical connection list. Default value: 1.; 
        self.page_number = page_number
        # description: Optional. The number of rows per page. Maximum value: 50. Default value: 10.; 
        self.page_size = page_size
        self.filter = filter
        # description: Optional. Indicates whether to return invalid orders.; 
        self.include_reservation_data = include_reservation_data
        # description: Optional. It is used to guarantee the idempotence of requests. This parameter is generated by clients. It must be unique for each request and must not exceed 64 ASCII characters in length.; 
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        else:
            result['Filter'] = None
        result['IncludeReservationData'] = self.include_reservation_data
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.filter = []
        if map.get('Filter') is not None:
            for k in map.get('Filter'):
                temp_model = DescribePhysicalConnectionsRequestFilter()
                self.filter.append(temp_model.from_map(k))
        else:
            self.filter = None
        self.include_reservation_data = map.get('IncludeReservationData')
        self.client_token = map.get('ClientToken')
        return self


class DescribePhysicalConnectionsRequestFilter(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class DescribePhysicalConnectionsResponse(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None,
                 physical_connection_set=None):
        # description: The ID of the request ; 
        self.request_id = request_id
        # description: The current page number ; 
        self.page_number = page_number
        # description: The number of items per page; 
        self.page_size = page_size
        # description: The number of items in a list; 
        self.total_count = total_count
        # description: Details of physical connections
        self.physical_connection_set = physical_connection_set  # type: DescribePhysicalConnectionsResponsePhysicalConnectionSet

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.physical_connection_set, 'physical_connection_set')
        if self.physical_connection_set:
            self.physical_connection_set.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        if self.physical_connection_set is not None:
            result['PhysicalConnectionSet'] = self.physical_connection_set.to_map()
        else:
            result['PhysicalConnectionSet'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        if map.get('PhysicalConnectionSet') is not None:
            temp_model = DescribePhysicalConnectionsResponsePhysicalConnectionSet()
            self.physical_connection_set = temp_model.from_map(map['PhysicalConnectionSet'])
        else:
            self.physical_connection_set = None
        return self


class DescribePhysicalConnectionsResponsePhysicalConnectionSetPhysicalConnectionType(TeaModel):
    def __init__(self, physical_connection_id=None, access_point_id=None, type=None, status=None,
                 business_status=None, creation_time=None, enabled_time=None, line_operator=None, spec=None, peer_location=None,
                 port_type=None, redundant_physical_connection_id=None, name=None, description=None, ad_location=None,
                 port_number=None, circuit_code=None, bandwidth=None, loa_status=None, has_reservation_data=None,
                 reservation_internet_charge_type=None, reservation_active_time=None, reservation_order_type=None, end_time=None, charge_type=None):
        # description: The ID of the physical connection; 
        self.physical_connection_id = physical_connection_id
        # description: The access point ID of the physical connection; 
        self.access_point_id = access_point_id
        # description: The type of the physical connection. Default value: **VPC**.; 
        self.type = type
        # description: The status of the physical connection. Valid values: * **Initial**: The physical connection has been applied for and is under review by Alibaba Cloud* **Approved**: The application is approved* **Allocating**: Resources* **Allocated**: The leased line is being installed.* **Confirmed**: The completed leased line installation needs to be confirmed by the customer.* **Enabled**: The physical connection interface is enabled.* **Rejected**: The application is rejected.* **Canceled**: The application is canceled.* **Allocation Failed**: Failed to allocate resources* **Terminated**: The physical connection is terminated; 
        self.status = status
        # description: The payment status of the physical connection. Valid values: * Normal * FinancialLocked: locked due to overdue payment* SecurityLocked: locked due to security reasons; 
        self.business_status = business_status
        # description: The time when the physical connection is established ; 
        self.creation_time = creation_time
        # description: The time when the physical connection is enabled ; 
        self.enabled_time = enabled_time
        # description: The service provider that provides the leased line. Valid values:* CT: China Telecom * CU: China Unicom* CM: China Mobile* CO: Other Chinese service providers* Equinix: Equinix * Other: Other service providers outside Mainland China; 
        self.line_operator = line_operator
        # description: The specification of the physical connection; 
        self.spec = spec
        # description: The location of the on-premises IDC; 
        self.peer_location = peer_location
        # description: The type of physical connection ports:* 100Base-T: 100M electrical ports * 1000Base-T (default value): Gigabit electrical ports * 1000Base-LX: Gigabit single-mode optical ports (10 km) * 10GBase-T: 10-GE electrical ports  * 10GBase-LR: 10-GE single-mode optical ports (10 km); 
        self.port_type = port_type
        # description: The ID of the redundant physical connection; 
        self.redundant_physical_connection_id = redundant_physical_connection_id
        # description: The name of the physical connection; 
        self.name = name
        # description: A description about the physical connection; 
        self.description = description
        # description: The location where the leased line is connected; 
        self.ad_location = ad_location
        # description: The port number of the physical connection device; 
        self.port_number = port_number
        # description: The number of the leased line from the service provider; 
        self.circuit_code = circuit_code
        # description: The bandwidth of the physical connection; 
        self.bandwidth = bandwidth
        # description: The status of the LOA ; 
        self.loa_status = loa_status
        # description: Indicates whether subscription messages are received; 
        self.has_reservation_data = has_reservation_data
        # description: The type of renewal ; 
        self.reservation_internet_charge_type = reservation_internet_charge_type
        # description: The effective time of a renewal; 
        self.reservation_active_time = reservation_active_time
        # description: The type of the renewal order ; 
        self.reservation_order_type = reservation_order_type
        # description: The time when the physical connection expires ; 
        self.end_time = end_time
        # description: The billing method of the physical connection; 
        self.charge_type = charge_type

    def validate(self):
        self.validate_required(self.physical_connection_id, 'physical_connection_id')
        self.validate_required(self.access_point_id, 'access_point_id')
        self.validate_required(self.type, 'type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.business_status, 'business_status')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.enabled_time, 'enabled_time')
        self.validate_required(self.line_operator, 'line_operator')
        self.validate_required(self.spec, 'spec')
        self.validate_required(self.peer_location, 'peer_location')
        self.validate_required(self.port_type, 'port_type')
        self.validate_required(self.redundant_physical_connection_id, 'redundant_physical_connection_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.ad_location, 'ad_location')
        self.validate_required(self.port_number, 'port_number')
        self.validate_required(self.circuit_code, 'circuit_code')
        self.validate_required(self.bandwidth, 'bandwidth')
        self.validate_required(self.loa_status, 'loa_status')
        self.validate_required(self.has_reservation_data, 'has_reservation_data')
        self.validate_required(self.reservation_internet_charge_type, 'reservation_internet_charge_type')
        self.validate_required(self.reservation_active_time, 'reservation_active_time')
        self.validate_required(self.reservation_order_type, 'reservation_order_type')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.charge_type, 'charge_type')

    def to_map(self):
        result = {}
        result['PhysicalConnectionId'] = self.physical_connection_id
        result['AccessPointId'] = self.access_point_id
        result['Type'] = self.type
        result['Status'] = self.status
        result['BusinessStatus'] = self.business_status
        result['CreationTime'] = self.creation_time
        result['EnabledTime'] = self.enabled_time
        result['LineOperator'] = self.line_operator
        result['Spec'] = self.spec
        result['PeerLocation'] = self.peer_location
        result['PortType'] = self.port_type
        result['RedundantPhysicalConnectionId'] = self.redundant_physical_connection_id
        result['Name'] = self.name
        result['Description'] = self.description
        result['AdLocation'] = self.ad_location
        result['PortNumber'] = self.port_number
        result['CircuitCode'] = self.circuit_code
        result['Bandwidth'] = self.bandwidth
        result['LoaStatus'] = self.loa_status
        result['HasReservationData'] = self.has_reservation_data
        result['ReservationInternetChargeType'] = self.reservation_internet_charge_type
        result['ReservationActiveTime'] = self.reservation_active_time
        result['ReservationOrderType'] = self.reservation_order_type
        result['EndTime'] = self.end_time
        result['ChargeType'] = self.charge_type
        return result

    def from_map(self, map={}):
        self.physical_connection_id = map.get('PhysicalConnectionId')
        self.access_point_id = map.get('AccessPointId')
        self.type = map.get('Type')
        self.status = map.get('Status')
        self.business_status = map.get('BusinessStatus')
        self.creation_time = map.get('CreationTime')
        self.enabled_time = map.get('EnabledTime')
        self.line_operator = map.get('LineOperator')
        self.spec = map.get('Spec')
        self.peer_location = map.get('PeerLocation')
        self.port_type = map.get('PortType')
        self.redundant_physical_connection_id = map.get('RedundantPhysicalConnectionId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.ad_location = map.get('AdLocation')
        self.port_number = map.get('PortNumber')
        self.circuit_code = map.get('CircuitCode')
        self.bandwidth = map.get('Bandwidth')
        self.loa_status = map.get('LoaStatus')
        self.has_reservation_data = map.get('HasReservationData')
        self.reservation_internet_charge_type = map.get('ReservationInternetChargeType')
        self.reservation_active_time = map.get('ReservationActiveTime')
        self.reservation_order_type = map.get('ReservationOrderType')
        self.end_time = map.get('EndTime')
        self.charge_type = map.get('ChargeType')
        return self


class DescribePhysicalConnectionsResponsePhysicalConnectionSet(TeaModel):
    def __init__(self, physical_connection_type=None):
        self.physical_connection_type = physical_connection_type

    def validate(self):
        self.validate_required(self.physical_connection_type, 'physical_connection_type')
        if self.physical_connection_type:
            for k in self.physical_connection_type:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PhysicalConnectionType'] = []
        if self.physical_connection_type is not None:
            for k in self.physical_connection_type:
                result['PhysicalConnectionType'].append(k.to_map() if k else None)
        else:
            result['PhysicalConnectionType'] = None
        return result

    def from_map(self, map={}):
        self.physical_connection_type = []
        if map.get('PhysicalConnectionType') is not None:
            for k in map.get('PhysicalConnectionType'):
                temp_model = DescribePhysicalConnectionsResponsePhysicalConnectionSetPhysicalConnectionType()
                self.physical_connection_type.append(temp_model.from_map(k))
        else:
            self.physical_connection_type = None
        return self


class DescribeNewProjectEipMonitorDataRequest(TeaModel):
    def __init__(self, region_id=None, allocation_id=None, start_time=None, end_time=None, period=None):
        self.region_id = region_id
        self.allocation_id = allocation_id
        self.start_time = start_time
        self.end_time = end_time
        self.period = period

    def validate(self):
        self.validate_required(self.allocation_id, 'allocation_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['AllocationId'] = self.allocation_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Period'] = self.period
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.allocation_id = map.get('AllocationId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.period = map.get('Period')
        return self


class DescribeNewProjectEipMonitorDataResponse(TeaModel):
    def __init__(self, request_id=None, eip_monitor_datas=None):
        self.request_id = request_id
        self.eip_monitor_datas = eip_monitor_datas  # type: DescribeNewProjectEipMonitorDataResponseEipMonitorDatas

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.eip_monitor_datas, 'eip_monitor_datas')
        if self.eip_monitor_datas:
            self.eip_monitor_datas.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.eip_monitor_datas is not None:
            result['EipMonitorDatas'] = self.eip_monitor_datas.to_map()
        else:
            result['EipMonitorDatas'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('EipMonitorDatas') is not None:
            temp_model = DescribeNewProjectEipMonitorDataResponseEipMonitorDatas()
            self.eip_monitor_datas = temp_model.from_map(map['EipMonitorDatas'])
        else:
            self.eip_monitor_datas = None
        return self


class DescribeNewProjectEipMonitorDataResponseEipMonitorDatasEipMonitorData(TeaModel):
    def __init__(self, eip_rx=None, eip_tx=None, eip_flow=None, eip_bandwidth=None, eip_packets=None,
                 time_stamp=None):
        self.eip_rx = eip_rx
        self.eip_tx = eip_tx
        self.eip_flow = eip_flow
        self.eip_bandwidth = eip_bandwidth
        self.eip_packets = eip_packets
        self.time_stamp = time_stamp

    def validate(self):
        self.validate_required(self.eip_rx, 'eip_rx')
        self.validate_required(self.eip_tx, 'eip_tx')
        self.validate_required(self.eip_flow, 'eip_flow')
        self.validate_required(self.eip_bandwidth, 'eip_bandwidth')
        self.validate_required(self.eip_packets, 'eip_packets')
        self.validate_required(self.time_stamp, 'time_stamp')

    def to_map(self):
        result = {}
        result['EipRX'] = self.eip_rx
        result['EipTX'] = self.eip_tx
        result['EipFlow'] = self.eip_flow
        result['EipBandwidth'] = self.eip_bandwidth
        result['EipPackets'] = self.eip_packets
        result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, map={}):
        self.eip_rx = map.get('EipRX')
        self.eip_tx = map.get('EipTX')
        self.eip_flow = map.get('EipFlow')
        self.eip_bandwidth = map.get('EipBandwidth')
        self.eip_packets = map.get('EipPackets')
        self.time_stamp = map.get('TimeStamp')
        return self


class DescribeNewProjectEipMonitorDataResponseEipMonitorDatas(TeaModel):
    def __init__(self, eip_monitor_data=None):
        self.eip_monitor_data = eip_monitor_data

    def validate(self):
        self.validate_required(self.eip_monitor_data, 'eip_monitor_data')
        if self.eip_monitor_data:
            for k in self.eip_monitor_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EipMonitorData'] = []
        if self.eip_monitor_data is not None:
            for k in self.eip_monitor_data:
                result['EipMonitorData'].append(k.to_map() if k else None)
        else:
            result['EipMonitorData'] = None
        return result

    def from_map(self, map={}):
        self.eip_monitor_data = []
        if map.get('EipMonitorData') is not None:
            for k in map.get('EipMonitorData'):
                temp_model = DescribeNewProjectEipMonitorDataResponseEipMonitorDatasEipMonitorData()
                self.eip_monitor_data.append(temp_model.from_map(k))
        else:
            self.eip_monitor_data = None
        return self


class DescribeNatGatewaysRequest(TeaModel):
    def __init__(self, region_id=None, nat_gateway_id=None, vpc_id=None, name=None, instance_charge_type=None,
                 spec=None, nat_type=None, resource_group_id=None, page_number=None, page_size=None, dry_run=None):
        self.region_id = region_id
        self.nat_gateway_id = nat_gateway_id
        self.vpc_id = vpc_id
        self.name = name
        self.instance_charge_type = instance_charge_type
        self.spec = spec
        self.nat_type = nat_type
        self.resource_group_id = resource_group_id
        self.page_number = page_number
        self.page_size = page_size
        self.dry_run = dry_run

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['NatGatewayId'] = self.nat_gateway_id
        result['VpcId'] = self.vpc_id
        result['Name'] = self.name
        result['InstanceChargeType'] = self.instance_charge_type
        result['Spec'] = self.spec
        result['NatType'] = self.nat_type
        result['ResourceGroupId'] = self.resource_group_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['DryRun'] = self.dry_run
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.nat_gateway_id = map.get('NatGatewayId')
        self.vpc_id = map.get('VpcId')
        self.name = map.get('Name')
        self.instance_charge_type = map.get('InstanceChargeType')
        self.spec = map.get('Spec')
        self.nat_type = map.get('NatType')
        self.resource_group_id = map.get('ResourceGroupId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.dry_run = map.get('DryRun')
        return self


class DescribeNatGatewaysResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, nat_gateways=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.nat_gateways = nat_gateways  # type: DescribeNatGatewaysResponseNatGateways

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.nat_gateways, 'nat_gateways')
        if self.nat_gateways:
            self.nat_gateways.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.nat_gateways is not None:
            result['NatGateways'] = self.nat_gateways.to_map()
        else:
            result['NatGateways'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('NatGateways') is not None:
            temp_model = DescribeNatGatewaysResponseNatGateways()
            self.nat_gateways = temp_model.from_map(map['NatGateways'])
        else:
            self.nat_gateways = None
        return self


class DescribeNatGatewaysResponseNatGatewaysNatGatewayIpListsIpList(TeaModel):
    def __init__(self, allocation_id=None, ip_address=None, using_status=None, ap_access_enabled=None,
                 snat_entry_enabled=None):
        self.allocation_id = allocation_id
        self.ip_address = ip_address
        self.using_status = using_status
        self.ap_access_enabled = ap_access_enabled
        self.snat_entry_enabled = snat_entry_enabled

    def validate(self):
        self.validate_required(self.allocation_id, 'allocation_id')
        self.validate_required(self.ip_address, 'ip_address')
        self.validate_required(self.using_status, 'using_status')
        self.validate_required(self.ap_access_enabled, 'ap_access_enabled')
        self.validate_required(self.snat_entry_enabled, 'snat_entry_enabled')

    def to_map(self):
        result = {}
        result['AllocationId'] = self.allocation_id
        result['IpAddress'] = self.ip_address
        result['UsingStatus'] = self.using_status
        result['ApAccessEnabled'] = self.ap_access_enabled
        result['SnatEntryEnabled'] = self.snat_entry_enabled
        return result

    def from_map(self, map={}):
        self.allocation_id = map.get('AllocationId')
        self.ip_address = map.get('IpAddress')
        self.using_status = map.get('UsingStatus')
        self.ap_access_enabled = map.get('ApAccessEnabled')
        self.snat_entry_enabled = map.get('SnatEntryEnabled')
        return self


class DescribeNatGatewaysResponseNatGatewaysNatGatewayIpLists(TeaModel):
    def __init__(self, ip_list=None):
        self.ip_list = ip_list

    def validate(self):
        self.validate_required(self.ip_list, 'ip_list')
        if self.ip_list:
            for k in self.ip_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['IpList'] = []
        if self.ip_list is not None:
            for k in self.ip_list:
                result['IpList'].append(k.to_map() if k else None)
        else:
            result['IpList'] = None
        return result

    def from_map(self, map={}):
        self.ip_list = []
        if map.get('IpList') is not None:
            for k in map.get('IpList'):
                temp_model = DescribeNatGatewaysResponseNatGatewaysNatGatewayIpListsIpList()
                self.ip_list.append(temp_model.from_map(k))
        else:
            self.ip_list = None
        return self


class DescribeNatGatewaysResponseNatGatewaysNatGatewayNatGatewayPrivateInfo(TeaModel):
    def __init__(self, eni_instance_id=None, private_ip_address=None, vswitch_id=None, iz_no=None,
                 max_bandwidth=None):
        self.eni_instance_id = eni_instance_id
        self.private_ip_address = private_ip_address
        self.vswitch_id = vswitch_id
        self.iz_no = iz_no
        self.max_bandwidth = max_bandwidth

    def validate(self):
        self.validate_required(self.eni_instance_id, 'eni_instance_id')
        self.validate_required(self.private_ip_address, 'private_ip_address')
        self.validate_required(self.vswitch_id, 'vswitch_id')
        self.validate_required(self.iz_no, 'iz_no')
        self.validate_required(self.max_bandwidth, 'max_bandwidth')

    def to_map(self):
        result = {}
        result['EniInstanceId'] = self.eni_instance_id
        result['PrivateIpAddress'] = self.private_ip_address
        result['VswitchId'] = self.vswitch_id
        result['IzNo'] = self.iz_no
        result['MaxBandwidth'] = self.max_bandwidth
        return result

    def from_map(self, map={}):
        self.eni_instance_id = map.get('EniInstanceId')
        self.private_ip_address = map.get('PrivateIpAddress')
        self.vswitch_id = map.get('VswitchId')
        self.iz_no = map.get('IzNo')
        self.max_bandwidth = map.get('MaxBandwidth')
        return self


class DescribeNatGatewaysResponseNatGatewaysNatGatewayForwardTableIds(TeaModel):
    def __init__(self, forward_table_id=None):
        # ForwardTableId
        self.forward_table_id = forward_table_id

    def validate(self):
        self.validate_required(self.forward_table_id, 'forward_table_id')

    def to_map(self):
        result = {}
        result['ForwardTableId'] = self.forward_table_id
        return result

    def from_map(self, map={}):
        self.forward_table_id = map.get('ForwardTableId')
        return self


class DescribeNatGatewaysResponseNatGatewaysNatGatewaySnatTableIds(TeaModel):
    def __init__(self, snat_table_id=None):
        # SnatTableId
        self.snat_table_id = snat_table_id

    def validate(self):
        self.validate_required(self.snat_table_id, 'snat_table_id')

    def to_map(self):
        result = {}
        result['SnatTableId'] = self.snat_table_id
        return result

    def from_map(self, map={}):
        self.snat_table_id = map.get('SnatTableId')
        return self


class DescribeNatGatewaysResponseNatGatewaysNatGatewayBandwidthPackageIds(TeaModel):
    def __init__(self, bandwidth_package_id=None):
        # BandwidthPackageId
        self.bandwidth_package_id = bandwidth_package_id

    def validate(self):
        self.validate_required(self.bandwidth_package_id, 'bandwidth_package_id')

    def to_map(self):
        result = {}
        result['BandwidthPackageId'] = self.bandwidth_package_id
        return result

    def from_map(self, map={}):
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        return self


class DescribeNatGatewaysResponseNatGatewaysNatGateway(TeaModel):
    def __init__(self, nat_gateway_id=None, region_id=None, name=None, description=None, vpc_id=None, spec=None,
                 instance_charge_type=None, expired_time=None, auto_pay=None, business_status=None, creation_time=None, status=None,
                 nat_type=None, internet_charge_type=None, resource_group_id=None, deletion_protection=None,
                 ecs_metric_enabled=None, ip_lists=None, nat_gateway_private_info=None, forward_table_ids=None, snat_table_ids=None,
                 bandwidth_package_ids=None):
        self.nat_gateway_id = nat_gateway_id
        self.region_id = region_id
        self.name = name
        self.description = description
        self.vpc_id = vpc_id
        self.spec = spec
        self.instance_charge_type = instance_charge_type
        self.expired_time = expired_time
        self.auto_pay = auto_pay
        self.business_status = business_status
        self.creation_time = creation_time
        self.status = status
        self.nat_type = nat_type
        self.internet_charge_type = internet_charge_type
        self.resource_group_id = resource_group_id
        self.deletion_protection = deletion_protection
        self.ecs_metric_enabled = ecs_metric_enabled
        self.ip_lists = ip_lists  # type: DescribeNatGatewaysResponseNatGatewaysNatGatewayIpLists
        self.nat_gateway_private_info = nat_gateway_private_info  # type: DescribeNatGatewaysResponseNatGatewaysNatGatewayNatGatewayPrivateInfo
        self.forward_table_ids = forward_table_ids  # type: DescribeNatGatewaysResponseNatGatewaysNatGatewayForwardTableIds
        self.snat_table_ids = snat_table_ids  # type: DescribeNatGatewaysResponseNatGatewaysNatGatewaySnatTableIds
        self.bandwidth_package_ids = bandwidth_package_ids  # type: DescribeNatGatewaysResponseNatGatewaysNatGatewayBandwidthPackageIds

    def validate(self):
        self.validate_required(self.nat_gateway_id, 'nat_gateway_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.spec, 'spec')
        self.validate_required(self.instance_charge_type, 'instance_charge_type')
        self.validate_required(self.expired_time, 'expired_time')
        self.validate_required(self.auto_pay, 'auto_pay')
        self.validate_required(self.business_status, 'business_status')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.nat_type, 'nat_type')
        self.validate_required(self.internet_charge_type, 'internet_charge_type')
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.deletion_protection, 'deletion_protection')
        self.validate_required(self.ecs_metric_enabled, 'ecs_metric_enabled')
        self.validate_required(self.ip_lists, 'ip_lists')
        if self.ip_lists:
            self.ip_lists.validate()
        self.validate_required(self.nat_gateway_private_info, 'nat_gateway_private_info')
        if self.nat_gateway_private_info:
            self.nat_gateway_private_info.validate()
        self.validate_required(self.forward_table_ids, 'forward_table_ids')
        if self.forward_table_ids:
            self.forward_table_ids.validate()
        self.validate_required(self.snat_table_ids, 'snat_table_ids')
        if self.snat_table_ids:
            self.snat_table_ids.validate()
        self.validate_required(self.bandwidth_package_ids, 'bandwidth_package_ids')
        if self.bandwidth_package_ids:
            self.bandwidth_package_ids.validate()

    def to_map(self):
        result = {}
        result['NatGatewayId'] = self.nat_gateway_id
        result['RegionId'] = self.region_id
        result['Name'] = self.name
        result['Description'] = self.description
        result['VpcId'] = self.vpc_id
        result['Spec'] = self.spec
        result['InstanceChargeType'] = self.instance_charge_type
        result['ExpiredTime'] = self.expired_time
        result['AutoPay'] = self.auto_pay
        result['BusinessStatus'] = self.business_status
        result['CreationTime'] = self.creation_time
        result['Status'] = self.status
        result['NatType'] = self.nat_type
        result['InternetChargeType'] = self.internet_charge_type
        result['ResourceGroupId'] = self.resource_group_id
        result['DeletionProtection'] = self.deletion_protection
        result['EcsMetricEnabled'] = self.ecs_metric_enabled
        if self.ip_lists is not None:
            result['IpLists'] = self.ip_lists.to_map()
        else:
            result['IpLists'] = None
        if self.nat_gateway_private_info is not None:
            result['NatGatewayPrivateInfo'] = self.nat_gateway_private_info.to_map()
        else:
            result['NatGatewayPrivateInfo'] = None
        if self.forward_table_ids is not None:
            result['ForwardTableIds'] = self.forward_table_ids.to_map()
        else:
            result['ForwardTableIds'] = None
        if self.snat_table_ids is not None:
            result['SnatTableIds'] = self.snat_table_ids.to_map()
        else:
            result['SnatTableIds'] = None
        if self.bandwidth_package_ids is not None:
            result['BandwidthPackageIds'] = self.bandwidth_package_ids.to_map()
        else:
            result['BandwidthPackageIds'] = None
        return result

    def from_map(self, map={}):
        self.nat_gateway_id = map.get('NatGatewayId')
        self.region_id = map.get('RegionId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.vpc_id = map.get('VpcId')
        self.spec = map.get('Spec')
        self.instance_charge_type = map.get('InstanceChargeType')
        self.expired_time = map.get('ExpiredTime')
        self.auto_pay = map.get('AutoPay')
        self.business_status = map.get('BusinessStatus')
        self.creation_time = map.get('CreationTime')
        self.status = map.get('Status')
        self.nat_type = map.get('NatType')
        self.internet_charge_type = map.get('InternetChargeType')
        self.resource_group_id = map.get('ResourceGroupId')
        self.deletion_protection = map.get('DeletionProtection')
        self.ecs_metric_enabled = map.get('EcsMetricEnabled')
        if map.get('IpLists') is not None:
            temp_model = DescribeNatGatewaysResponseNatGatewaysNatGatewayIpLists()
            self.ip_lists = temp_model.from_map(map['IpLists'])
        else:
            self.ip_lists = None
        if map.get('NatGatewayPrivateInfo') is not None:
            temp_model = DescribeNatGatewaysResponseNatGatewaysNatGatewayNatGatewayPrivateInfo()
            self.nat_gateway_private_info = temp_model.from_map(map['NatGatewayPrivateInfo'])
        else:
            self.nat_gateway_private_info = None
        if map.get('ForwardTableIds') is not None:
            temp_model = DescribeNatGatewaysResponseNatGatewaysNatGatewayForwardTableIds()
            self.forward_table_ids = temp_model.from_map(map['ForwardTableIds'])
        else:
            self.forward_table_ids = None
        if map.get('SnatTableIds') is not None:
            temp_model = DescribeNatGatewaysResponseNatGatewaysNatGatewaySnatTableIds()
            self.snat_table_ids = temp_model.from_map(map['SnatTableIds'])
        else:
            self.snat_table_ids = None
        if map.get('BandwidthPackageIds') is not None:
            temp_model = DescribeNatGatewaysResponseNatGatewaysNatGatewayBandwidthPackageIds()
            self.bandwidth_package_ids = temp_model.from_map(map['BandwidthPackageIds'])
        else:
            self.bandwidth_package_ids = None
        return self


class DescribeNatGatewaysResponseNatGateways(TeaModel):
    def __init__(self, nat_gateway=None):
        self.nat_gateway = nat_gateway

    def validate(self):
        self.validate_required(self.nat_gateway, 'nat_gateway')
        if self.nat_gateway:
            for k in self.nat_gateway:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['NatGateway'] = []
        if self.nat_gateway is not None:
            for k in self.nat_gateway:
                result['NatGateway'].append(k.to_map() if k else None)
        else:
            result['NatGateway'] = None
        return result

    def from_map(self, map={}):
        self.nat_gateway = []
        if map.get('NatGateway') is not None:
            for k in map.get('NatGateway'):
                temp_model = DescribeNatGatewaysResponseNatGatewaysNatGateway()
                self.nat_gateway.append(temp_model.from_map(k))
        else:
            self.nat_gateway = None
        return self


class DescribeHaVipsRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None, filter=None):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.filter = filter

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        else:
            result['Filter'] = None
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.filter = []
        if map.get('Filter') is not None:
            for k in map.get('Filter'):
                temp_model = DescribeHaVipsRequestFilter()
                self.filter.append(temp_model.from_map(k))
        else:
            self.filter = None
        return self


class DescribeHaVipsRequestFilter(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class DescribeHaVipsResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, ha_vips=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.ha_vips = ha_vips  # type: DescribeHaVipsResponseHaVips

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.ha_vips, 'ha_vips')
        if self.ha_vips:
            self.ha_vips.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.ha_vips is not None:
            result['HaVips'] = self.ha_vips.to_map()
        else:
            result['HaVips'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('HaVips') is not None:
            temp_model = DescribeHaVipsResponseHaVips()
            self.ha_vips = temp_model.from_map(map['HaVips'])
        else:
            self.ha_vips = None
        return self


class DescribeHaVipsResponseHaVipsHaVipAssociatedInstances(TeaModel):
    def __init__(self, associated_instance=None):
        # associatedInstance
        self.associated_instance = associated_instance

    def validate(self):
        self.validate_required(self.associated_instance, 'associated_instance')

    def to_map(self):
        result = {}
        result['associatedInstance'] = self.associated_instance
        return result

    def from_map(self, map={}):
        self.associated_instance = map.get('associatedInstance')
        return self


class DescribeHaVipsResponseHaVipsHaVipAssociatedEipAddresses(TeaModel):
    def __init__(self, associated_eip_addresse=None):
        # associatedEipAddresse
        self.associated_eip_addresse = associated_eip_addresse

    def validate(self):
        self.validate_required(self.associated_eip_addresse, 'associated_eip_addresse')

    def to_map(self):
        result = {}
        result['associatedEipAddresse'] = self.associated_eip_addresse
        return result

    def from_map(self, map={}):
        self.associated_eip_addresse = map.get('associatedEipAddresse')
        return self


class DescribeHaVipsResponseHaVipsHaVip(TeaModel):
    def __init__(self, ha_vip_id=None, region_id=None, vpc_id=None, v_switch_id=None, ip_address=None, status=None,
                 master_instance_id=None, description=None, name=None, charge_type=None, create_time=None, associated_instances=None,
                 associated_eip_addresses=None):
        self.ha_vip_id = ha_vip_id
        self.region_id = region_id
        self.vpc_id = vpc_id
        self.v_switch_id = v_switch_id
        self.ip_address = ip_address
        self.status = status
        self.master_instance_id = master_instance_id
        self.description = description
        self.name = name
        self.charge_type = charge_type
        self.create_time = create_time
        self.associated_instances = associated_instances  # type: DescribeHaVipsResponseHaVipsHaVipAssociatedInstances
        self.associated_eip_addresses = associated_eip_addresses  # type: DescribeHaVipsResponseHaVipsHaVipAssociatedEipAddresses

    def validate(self):
        self.validate_required(self.ha_vip_id, 'ha_vip_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.v_switch_id, 'v_switch_id')
        self.validate_required(self.ip_address, 'ip_address')
        self.validate_required(self.status, 'status')
        self.validate_required(self.master_instance_id, 'master_instance_id')
        self.validate_required(self.description, 'description')
        self.validate_required(self.name, 'name')
        self.validate_required(self.charge_type, 'charge_type')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.associated_instances, 'associated_instances')
        if self.associated_instances:
            self.associated_instances.validate()
        self.validate_required(self.associated_eip_addresses, 'associated_eip_addresses')
        if self.associated_eip_addresses:
            self.associated_eip_addresses.validate()

    def to_map(self):
        result = {}
        result['HaVipId'] = self.ha_vip_id
        result['RegionId'] = self.region_id
        result['VpcId'] = self.vpc_id
        result['VSwitchId'] = self.v_switch_id
        result['IpAddress'] = self.ip_address
        result['Status'] = self.status
        result['MasterInstanceId'] = self.master_instance_id
        result['Description'] = self.description
        result['Name'] = self.name
        result['ChargeType'] = self.charge_type
        result['CreateTime'] = self.create_time
        if self.associated_instances is not None:
            result['AssociatedInstances'] = self.associated_instances.to_map()
        else:
            result['AssociatedInstances'] = None
        if self.associated_eip_addresses is not None:
            result['AssociatedEipAddresses'] = self.associated_eip_addresses.to_map()
        else:
            result['AssociatedEipAddresses'] = None
        return result

    def from_map(self, map={}):
        self.ha_vip_id = map.get('HaVipId')
        self.region_id = map.get('RegionId')
        self.vpc_id = map.get('VpcId')
        self.v_switch_id = map.get('VSwitchId')
        self.ip_address = map.get('IpAddress')
        self.status = map.get('Status')
        self.master_instance_id = map.get('MasterInstanceId')
        self.description = map.get('Description')
        self.name = map.get('Name')
        self.charge_type = map.get('ChargeType')
        self.create_time = map.get('CreateTime')
        if map.get('AssociatedInstances') is not None:
            temp_model = DescribeHaVipsResponseHaVipsHaVipAssociatedInstances()
            self.associated_instances = temp_model.from_map(map['AssociatedInstances'])
        else:
            self.associated_instances = None
        if map.get('AssociatedEipAddresses') is not None:
            temp_model = DescribeHaVipsResponseHaVipsHaVipAssociatedEipAddresses()
            self.associated_eip_addresses = temp_model.from_map(map['AssociatedEipAddresses'])
        else:
            self.associated_eip_addresses = None
        return self


class DescribeHaVipsResponseHaVips(TeaModel):
    def __init__(self, ha_vip=None):
        self.ha_vip = ha_vip

    def validate(self):
        self.validate_required(self.ha_vip, 'ha_vip')
        if self.ha_vip:
            for k in self.ha_vip:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['HaVip'] = []
        if self.ha_vip is not None:
            for k in self.ha_vip:
                result['HaVip'].append(k.to_map() if k else None)
        else:
            result['HaVip'] = None
        return result

    def from_map(self, map={}):
        self.ha_vip = []
        if map.get('HaVip') is not None:
            for k in map.get('HaVip'):
                temp_model = DescribeHaVipsResponseHaVipsHaVip()
                self.ha_vip.append(temp_model.from_map(k))
        else:
            self.ha_vip = None
        return self


class DescribeForwardTableEntriesRequest(TeaModel):
    def __init__(self, region_id=None, forward_table_id=None, forward_entry_id=None, external_ip=None,
                 external_port=None, internal_ip=None, internal_port=None, ip_protocol=None, forward_entry_name=None,
                 page_number=None, page_size=None):
        self.region_id = region_id
        self.forward_table_id = forward_table_id
        self.forward_entry_id = forward_entry_id
        self.external_ip = external_ip
        self.external_port = external_port
        self.internal_ip = internal_ip
        self.internal_port = internal_port
        self.ip_protocol = ip_protocol
        self.forward_entry_name = forward_entry_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.forward_table_id, 'forward_table_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ForwardTableId'] = self.forward_table_id
        result['ForwardEntryId'] = self.forward_entry_id
        result['ExternalIp'] = self.external_ip
        result['ExternalPort'] = self.external_port
        result['InternalIp'] = self.internal_ip
        result['InternalPort'] = self.internal_port
        result['IpProtocol'] = self.ip_protocol
        result['ForwardEntryName'] = self.forward_entry_name
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.forward_table_id = map.get('ForwardTableId')
        self.forward_entry_id = map.get('ForwardEntryId')
        self.external_ip = map.get('ExternalIp')
        self.external_port = map.get('ExternalPort')
        self.internal_ip = map.get('InternalIp')
        self.internal_port = map.get('InternalPort')
        self.ip_protocol = map.get('IpProtocol')
        self.forward_entry_name = map.get('ForwardEntryName')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeForwardTableEntriesResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None,
                 forward_table_entries=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.forward_table_entries = forward_table_entries  # type: DescribeForwardTableEntriesResponseForwardTableEntries

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.forward_table_entries, 'forward_table_entries')
        if self.forward_table_entries:
            self.forward_table_entries.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.forward_table_entries is not None:
            result['ForwardTableEntries'] = self.forward_table_entries.to_map()
        else:
            result['ForwardTableEntries'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('ForwardTableEntries') is not None:
            temp_model = DescribeForwardTableEntriesResponseForwardTableEntries()
            self.forward_table_entries = temp_model.from_map(map['ForwardTableEntries'])
        else:
            self.forward_table_entries = None
        return self


class DescribeForwardTableEntriesResponseForwardTableEntriesForwardTableEntry(TeaModel):
    def __init__(self, forward_table_id=None, forward_entry_id=None, external_ip=None, external_port=None,
                 ip_protocol=None, internal_ip=None, internal_port=None, status=None, forward_entry_name=None):
        self.forward_table_id = forward_table_id
        self.forward_entry_id = forward_entry_id
        self.external_ip = external_ip
        self.external_port = external_port
        self.ip_protocol = ip_protocol
        self.internal_ip = internal_ip
        self.internal_port = internal_port
        self.status = status
        self.forward_entry_name = forward_entry_name

    def validate(self):
        self.validate_required(self.forward_table_id, 'forward_table_id')
        self.validate_required(self.forward_entry_id, 'forward_entry_id')
        self.validate_required(self.external_ip, 'external_ip')
        self.validate_required(self.external_port, 'external_port')
        self.validate_required(self.ip_protocol, 'ip_protocol')
        self.validate_required(self.internal_ip, 'internal_ip')
        self.validate_required(self.internal_port, 'internal_port')
        self.validate_required(self.status, 'status')
        self.validate_required(self.forward_entry_name, 'forward_entry_name')

    def to_map(self):
        result = {}
        result['ForwardTableId'] = self.forward_table_id
        result['ForwardEntryId'] = self.forward_entry_id
        result['ExternalIp'] = self.external_ip
        result['ExternalPort'] = self.external_port
        result['IpProtocol'] = self.ip_protocol
        result['InternalIp'] = self.internal_ip
        result['InternalPort'] = self.internal_port
        result['Status'] = self.status
        result['ForwardEntryName'] = self.forward_entry_name
        return result

    def from_map(self, map={}):
        self.forward_table_id = map.get('ForwardTableId')
        self.forward_entry_id = map.get('ForwardEntryId')
        self.external_ip = map.get('ExternalIp')
        self.external_port = map.get('ExternalPort')
        self.ip_protocol = map.get('IpProtocol')
        self.internal_ip = map.get('InternalIp')
        self.internal_port = map.get('InternalPort')
        self.status = map.get('Status')
        self.forward_entry_name = map.get('ForwardEntryName')
        return self


class DescribeForwardTableEntriesResponseForwardTableEntries(TeaModel):
    def __init__(self, forward_table_entry=None):
        self.forward_table_entry = forward_table_entry

    def validate(self):
        self.validate_required(self.forward_table_entry, 'forward_table_entry')
        if self.forward_table_entry:
            for k in self.forward_table_entry:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ForwardTableEntry'] = []
        if self.forward_table_entry is not None:
            for k in self.forward_table_entry:
                result['ForwardTableEntry'].append(k.to_map() if k else None)
        else:
            result['ForwardTableEntry'] = None
        return result

    def from_map(self, map={}):
        self.forward_table_entry = []
        if map.get('ForwardTableEntry') is not None:
            for k in map.get('ForwardTableEntry'):
                temp_model = DescribeForwardTableEntriesResponseForwardTableEntriesForwardTableEntry()
                self.forward_table_entry.append(temp_model.from_map(k))
        else:
            self.forward_table_entry = None
        return self


class DescribeEipMonitorDataRequest(TeaModel):
    def __init__(self, region_id=None, allocation_id=None, start_time=None, end_time=None, period=None):
        self.region_id = region_id
        self.allocation_id = allocation_id
        self.start_time = start_time
        self.end_time = end_time
        self.period = period

    def validate(self):
        self.validate_required(self.allocation_id, 'allocation_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['AllocationId'] = self.allocation_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Period'] = self.period
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.allocation_id = map.get('AllocationId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.period = map.get('Period')
        return self


class DescribeEipMonitorDataResponse(TeaModel):
    def __init__(self, request_id=None, eip_monitor_datas=None):
        self.request_id = request_id
        self.eip_monitor_datas = eip_monitor_datas  # type: DescribeEipMonitorDataResponseEipMonitorDatas

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.eip_monitor_datas, 'eip_monitor_datas')
        if self.eip_monitor_datas:
            self.eip_monitor_datas.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.eip_monitor_datas is not None:
            result['EipMonitorDatas'] = self.eip_monitor_datas.to_map()
        else:
            result['EipMonitorDatas'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('EipMonitorDatas') is not None:
            temp_model = DescribeEipMonitorDataResponseEipMonitorDatas()
            self.eip_monitor_datas = temp_model.from_map(map['EipMonitorDatas'])
        else:
            self.eip_monitor_datas = None
        return self


class DescribeEipMonitorDataResponseEipMonitorDatasEipMonitorData(TeaModel):
    def __init__(self, eip_rx=None, eip_tx=None, eip_flow=None, eip_bandwidth=None, eip_packets=None,
                 time_stamp=None):
        self.eip_rx = eip_rx
        self.eip_tx = eip_tx
        self.eip_flow = eip_flow
        self.eip_bandwidth = eip_bandwidth
        self.eip_packets = eip_packets
        self.time_stamp = time_stamp

    def validate(self):
        self.validate_required(self.eip_rx, 'eip_rx')
        self.validate_required(self.eip_tx, 'eip_tx')
        self.validate_required(self.eip_flow, 'eip_flow')
        self.validate_required(self.eip_bandwidth, 'eip_bandwidth')
        self.validate_required(self.eip_packets, 'eip_packets')
        self.validate_required(self.time_stamp, 'time_stamp')

    def to_map(self):
        result = {}
        result['EipRX'] = self.eip_rx
        result['EipTX'] = self.eip_tx
        result['EipFlow'] = self.eip_flow
        result['EipBandwidth'] = self.eip_bandwidth
        result['EipPackets'] = self.eip_packets
        result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, map={}):
        self.eip_rx = map.get('EipRX')
        self.eip_tx = map.get('EipTX')
        self.eip_flow = map.get('EipFlow')
        self.eip_bandwidth = map.get('EipBandwidth')
        self.eip_packets = map.get('EipPackets')
        self.time_stamp = map.get('TimeStamp')
        return self


class DescribeEipMonitorDataResponseEipMonitorDatas(TeaModel):
    def __init__(self, eip_monitor_data=None):
        self.eip_monitor_data = eip_monitor_data

    def validate(self):
        self.validate_required(self.eip_monitor_data, 'eip_monitor_data')
        if self.eip_monitor_data:
            for k in self.eip_monitor_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EipMonitorData'] = []
        if self.eip_monitor_data is not None:
            for k in self.eip_monitor_data:
                result['EipMonitorData'].append(k.to_map() if k else None)
        else:
            result['EipMonitorData'] = None
        return result

    def from_map(self, map={}):
        self.eip_monitor_data = []
        if map.get('EipMonitorData') is not None:
            for k in map.get('EipMonitorData'):
                temp_model = DescribeEipMonitorDataResponseEipMonitorDatasEipMonitorData()
                self.eip_monitor_data.append(temp_model.from_map(k))
        else:
            self.eip_monitor_data = None
        return self


class DescribeEipAddressesRequest(TeaModel):
    def __init__(self, region_id=None, include_reservation_data=None, status=None, eip_address=None,
                 allocation_id=None, segment_instance_id=None, resource_group_id=None, page_number=None, page_size=None, isp=None,
                 filter=None, lock_reason=None, associated_instance_type=None, associated_instance_id=None,
                 charge_type=None, dry_run=None):
        self.region_id = region_id
        self.include_reservation_data = include_reservation_data
        self.status = status
        self.eip_address = eip_address
        self.allocation_id = allocation_id
        self.segment_instance_id = segment_instance_id
        self.resource_group_id = resource_group_id
        self.page_number = page_number
        self.page_size = page_size
        self.isp = isp
        self.filter = filter
        self.lock_reason = lock_reason
        self.associated_instance_type = associated_instance_type
        self.associated_instance_id = associated_instance_id
        self.charge_type = charge_type
        self.dry_run = dry_run

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['IncludeReservationData'] = self.include_reservation_data
        result['Status'] = self.status
        result['EipAddress'] = self.eip_address
        result['AllocationId'] = self.allocation_id
        result['SegmentInstanceId'] = self.segment_instance_id
        result['ResourceGroupId'] = self.resource_group_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['ISP'] = self.isp
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        else:
            result['Filter'] = None
        result['LockReason'] = self.lock_reason
        result['AssociatedInstanceType'] = self.associated_instance_type
        result['AssociatedInstanceId'] = self.associated_instance_id
        result['ChargeType'] = self.charge_type
        result['DryRun'] = self.dry_run
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.include_reservation_data = map.get('IncludeReservationData')
        self.status = map.get('Status')
        self.eip_address = map.get('EipAddress')
        self.allocation_id = map.get('AllocationId')
        self.segment_instance_id = map.get('SegmentInstanceId')
        self.resource_group_id = map.get('ResourceGroupId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.isp = map.get('ISP')
        self.filter = []
        if map.get('Filter') is not None:
            for k in map.get('Filter'):
                temp_model = DescribeEipAddressesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        else:
            self.filter = None
        self.lock_reason = map.get('LockReason')
        self.associated_instance_type = map.get('AssociatedInstanceType')
        self.associated_instance_id = map.get('AssociatedInstanceId')
        self.charge_type = map.get('ChargeType')
        self.dry_run = map.get('DryRun')
        return self


class DescribeEipAddressesRequestFilter(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class DescribeEipAddressesResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, eip_addresses=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.eip_addresses = eip_addresses  # type: DescribeEipAddressesResponseEipAddresses

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.eip_addresses, 'eip_addresses')
        if self.eip_addresses:
            self.eip_addresses.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.eip_addresses is not None:
            result['EipAddresses'] = self.eip_addresses.to_map()
        else:
            result['EipAddresses'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('EipAddresses') is not None:
            temp_model = DescribeEipAddressesResponseEipAddresses()
            self.eip_addresses = temp_model.from_map(map['EipAddresses'])
        else:
            self.eip_addresses = None
        return self


class DescribeEipAddressesResponseEipAddressesEipAddressOperationLocksLockReason(TeaModel):
    def __init__(self, lock_reason=None):
        self.lock_reason = lock_reason

    def validate(self):
        self.validate_required(self.lock_reason, 'lock_reason')

    def to_map(self):
        result = {}
        result['LockReason'] = self.lock_reason
        return result

    def from_map(self, map={}):
        self.lock_reason = map.get('LockReason')
        return self


class DescribeEipAddressesResponseEipAddressesEipAddressOperationLocks(TeaModel):
    def __init__(self, lock_reason=None):
        self.lock_reason = lock_reason

    def validate(self):
        self.validate_required(self.lock_reason, 'lock_reason')
        if self.lock_reason:
            for k in self.lock_reason:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LockReason'] = []
        if self.lock_reason is not None:
            for k in self.lock_reason:
                result['LockReason'].append(k.to_map() if k else None)
        else:
            result['LockReason'] = None
        return result

    def from_map(self, map={}):
        self.lock_reason = []
        if map.get('LockReason') is not None:
            for k in map.get('LockReason'):
                temp_model = DescribeEipAddressesResponseEipAddressesEipAddressOperationLocksLockReason()
                self.lock_reason.append(temp_model.from_map(k))
        else:
            self.lock_reason = None
        return self


class DescribeEipAddressesResponseEipAddressesEipAddressAvailableRegions(TeaModel):
    def __init__(self, available_region=None):
        # AvailableRegion
        self.available_region = available_region

    def validate(self):
        self.validate_required(self.available_region, 'available_region')

    def to_map(self):
        result = {}
        result['AvailableRegion'] = self.available_region
        return result

    def from_map(self, map={}):
        self.available_region = map.get('AvailableRegion')
        return self


class DescribeEipAddressesResponseEipAddressesEipAddress(TeaModel):
    def __init__(self, region_id=None, ip_address=None, private_ip_address=None, allocation_id=None, status=None,
                 instance_id=None, bandwidth=None, eip_bandwidth=None, internet_charge_type=None, allocation_time=None,
                 instance_type=None, instance_region_id=None, charge_type=None, expired_time=None, hdmonitor_status=None,
                 name=None, isp=None, descritpion=None, bandwidth_package_id=None, bandwidth_package_type=None,
                 bandwidth_package_bandwidth=None, resource_group_id=None, has_reservation_data=None, reservation_bandwidth=None,
                 reservation_internet_charge_type=None, reservation_active_time=None, reservation_order_type=None, mode=None,
                 deletion_protection=None, second_limited=None, segment_instance_id=None, netmode=None, operation_locks=None,
                 available_regions=None):
        self.region_id = region_id
        self.ip_address = ip_address
        self.private_ip_address = private_ip_address
        self.allocation_id = allocation_id
        self.status = status
        self.instance_id = instance_id
        self.bandwidth = bandwidth
        self.eip_bandwidth = eip_bandwidth
        self.internet_charge_type = internet_charge_type
        self.allocation_time = allocation_time
        self.instance_type = instance_type
        self.instance_region_id = instance_region_id
        self.charge_type = charge_type
        self.expired_time = expired_time
        self.hdmonitor_status = hdmonitor_status
        self.name = name
        self.isp = isp
        self.descritpion = descritpion
        self.bandwidth_package_id = bandwidth_package_id
        self.bandwidth_package_type = bandwidth_package_type
        self.bandwidth_package_bandwidth = bandwidth_package_bandwidth
        self.resource_group_id = resource_group_id
        self.has_reservation_data = has_reservation_data
        self.reservation_bandwidth = reservation_bandwidth
        self.reservation_internet_charge_type = reservation_internet_charge_type
        self.reservation_active_time = reservation_active_time
        self.reservation_order_type = reservation_order_type
        self.mode = mode
        self.deletion_protection = deletion_protection
        self.second_limited = second_limited
        self.segment_instance_id = segment_instance_id
        self.netmode = netmode
        self.operation_locks = operation_locks  # type: DescribeEipAddressesResponseEipAddressesEipAddressOperationLocks
        self.available_regions = available_regions  # type: DescribeEipAddressesResponseEipAddressesEipAddressAvailableRegions

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ip_address, 'ip_address')
        self.validate_required(self.private_ip_address, 'private_ip_address')
        self.validate_required(self.allocation_id, 'allocation_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.bandwidth, 'bandwidth')
        self.validate_required(self.eip_bandwidth, 'eip_bandwidth')
        self.validate_required(self.internet_charge_type, 'internet_charge_type')
        self.validate_required(self.allocation_time, 'allocation_time')
        self.validate_required(self.instance_type, 'instance_type')
        self.validate_required(self.instance_region_id, 'instance_region_id')
        self.validate_required(self.charge_type, 'charge_type')
        self.validate_required(self.expired_time, 'expired_time')
        self.validate_required(self.hdmonitor_status, 'hdmonitor_status')
        self.validate_required(self.name, 'name')
        self.validate_required(self.isp, 'isp')
        self.validate_required(self.descritpion, 'descritpion')
        self.validate_required(self.bandwidth_package_id, 'bandwidth_package_id')
        self.validate_required(self.bandwidth_package_type, 'bandwidth_package_type')
        self.validate_required(self.bandwidth_package_bandwidth, 'bandwidth_package_bandwidth')
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.has_reservation_data, 'has_reservation_data')
        self.validate_required(self.reservation_bandwidth, 'reservation_bandwidth')
        self.validate_required(self.reservation_internet_charge_type, 'reservation_internet_charge_type')
        self.validate_required(self.reservation_active_time, 'reservation_active_time')
        self.validate_required(self.reservation_order_type, 'reservation_order_type')
        self.validate_required(self.mode, 'mode')
        self.validate_required(self.deletion_protection, 'deletion_protection')
        self.validate_required(self.second_limited, 'second_limited')
        self.validate_required(self.segment_instance_id, 'segment_instance_id')
        self.validate_required(self.netmode, 'netmode')
        self.validate_required(self.operation_locks, 'operation_locks')
        if self.operation_locks:
            self.operation_locks.validate()
        self.validate_required(self.available_regions, 'available_regions')
        if self.available_regions:
            self.available_regions.validate()

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['IpAddress'] = self.ip_address
        result['PrivateIpAddress'] = self.private_ip_address
        result['AllocationId'] = self.allocation_id
        result['Status'] = self.status
        result['InstanceId'] = self.instance_id
        result['Bandwidth'] = self.bandwidth
        result['EipBandwidth'] = self.eip_bandwidth
        result['InternetChargeType'] = self.internet_charge_type
        result['AllocationTime'] = self.allocation_time
        result['InstanceType'] = self.instance_type
        result['InstanceRegionId'] = self.instance_region_id
        result['ChargeType'] = self.charge_type
        result['ExpiredTime'] = self.expired_time
        result['HDMonitorStatus'] = self.hdmonitor_status
        result['Name'] = self.name
        result['ISP'] = self.isp
        result['Descritpion'] = self.descritpion
        result['BandwidthPackageId'] = self.bandwidth_package_id
        result['BandwidthPackageType'] = self.bandwidth_package_type
        result['BandwidthPackageBandwidth'] = self.bandwidth_package_bandwidth
        result['ResourceGroupId'] = self.resource_group_id
        result['HasReservationData'] = self.has_reservation_data
        result['ReservationBandwidth'] = self.reservation_bandwidth
        result['ReservationInternetChargeType'] = self.reservation_internet_charge_type
        result['ReservationActiveTime'] = self.reservation_active_time
        result['ReservationOrderType'] = self.reservation_order_type
        result['Mode'] = self.mode
        result['DeletionProtection'] = self.deletion_protection
        result['SecondLimited'] = self.second_limited
        result['SegmentInstanceId'] = self.segment_instance_id
        result['Netmode'] = self.netmode
        if self.operation_locks is not None:
            result['OperationLocks'] = self.operation_locks.to_map()
        else:
            result['OperationLocks'] = None
        if self.available_regions is not None:
            result['AvailableRegions'] = self.available_regions.to_map()
        else:
            result['AvailableRegions'] = None
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.ip_address = map.get('IpAddress')
        self.private_ip_address = map.get('PrivateIpAddress')
        self.allocation_id = map.get('AllocationId')
        self.status = map.get('Status')
        self.instance_id = map.get('InstanceId')
        self.bandwidth = map.get('Bandwidth')
        self.eip_bandwidth = map.get('EipBandwidth')
        self.internet_charge_type = map.get('InternetChargeType')
        self.allocation_time = map.get('AllocationTime')
        self.instance_type = map.get('InstanceType')
        self.instance_region_id = map.get('InstanceRegionId')
        self.charge_type = map.get('ChargeType')
        self.expired_time = map.get('ExpiredTime')
        self.hdmonitor_status = map.get('HDMonitorStatus')
        self.name = map.get('Name')
        self.isp = map.get('ISP')
        self.descritpion = map.get('Descritpion')
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        self.bandwidth_package_type = map.get('BandwidthPackageType')
        self.bandwidth_package_bandwidth = map.get('BandwidthPackageBandwidth')
        self.resource_group_id = map.get('ResourceGroupId')
        self.has_reservation_data = map.get('HasReservationData')
        self.reservation_bandwidth = map.get('ReservationBandwidth')
        self.reservation_internet_charge_type = map.get('ReservationInternetChargeType')
        self.reservation_active_time = map.get('ReservationActiveTime')
        self.reservation_order_type = map.get('ReservationOrderType')
        self.mode = map.get('Mode')
        self.deletion_protection = map.get('DeletionProtection')
        self.second_limited = map.get('SecondLimited')
        self.segment_instance_id = map.get('SegmentInstanceId')
        self.netmode = map.get('Netmode')
        if map.get('OperationLocks') is not None:
            temp_model = DescribeEipAddressesResponseEipAddressesEipAddressOperationLocks()
            self.operation_locks = temp_model.from_map(map['OperationLocks'])
        else:
            self.operation_locks = None
        if map.get('AvailableRegions') is not None:
            temp_model = DescribeEipAddressesResponseEipAddressesEipAddressAvailableRegions()
            self.available_regions = temp_model.from_map(map['AvailableRegions'])
        else:
            self.available_regions = None
        return self


class DescribeEipAddressesResponseEipAddresses(TeaModel):
    def __init__(self, eip_address=None):
        self.eip_address = eip_address

    def validate(self):
        self.validate_required(self.eip_address, 'eip_address')
        if self.eip_address:
            for k in self.eip_address:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EipAddress'] = []
        if self.eip_address is not None:
            for k in self.eip_address:
                result['EipAddress'].append(k.to_map() if k else None)
        else:
            result['EipAddress'] = None
        return result

    def from_map(self, map={}):
        self.eip_address = []
        if map.get('EipAddress') is not None:
            for k in map.get('EipAddress'):
                temp_model = DescribeEipAddressesResponseEipAddressesEipAddress()
                self.eip_address.append(temp_model.from_map(k))
        else:
            self.eip_address = None
        return self


class DescribeBandwidthPackagesRequest(TeaModel):
    def __init__(self, region_id=None, bandwidth_package_id=None, nat_gateway_id=None, page_number=None,
                 page_size=None):
        self.region_id = region_id
        self.bandwidth_package_id = bandwidth_package_id
        self.nat_gateway_id = nat_gateway_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['BandwidthPackageId'] = self.bandwidth_package_id
        result['NatGatewayId'] = self.nat_gateway_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        self.nat_gateway_id = map.get('NatGatewayId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeBandwidthPackagesResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, bandwidth_packages=None):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.bandwidth_packages = bandwidth_packages  # type: DescribeBandwidthPackagesResponseBandwidthPackages

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.bandwidth_packages, 'bandwidth_packages')
        if self.bandwidth_packages:
            self.bandwidth_packages.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.bandwidth_packages is not None:
            result['BandwidthPackages'] = self.bandwidth_packages.to_map()
        else:
            result['BandwidthPackages'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('BandwidthPackages') is not None:
            temp_model = DescribeBandwidthPackagesResponseBandwidthPackages()
            self.bandwidth_packages = temp_model.from_map(map['BandwidthPackages'])
        else:
            self.bandwidth_packages = None
        return self


class DescribeBandwidthPackagesResponseBandwidthPackagesBandwidthPackagePublicIpAddressesPublicIpAddresse(TeaModel):
    def __init__(self, allocation_id=None, ip_address=None, using_status=None, ap_access_enabled=None):
        self.allocation_id = allocation_id
        self.ip_address = ip_address
        self.using_status = using_status
        self.ap_access_enabled = ap_access_enabled

    def validate(self):
        self.validate_required(self.allocation_id, 'allocation_id')
        self.validate_required(self.ip_address, 'ip_address')
        self.validate_required(self.using_status, 'using_status')
        self.validate_required(self.ap_access_enabled, 'ap_access_enabled')

    def to_map(self):
        result = {}
        result['AllocationId'] = self.allocation_id
        result['IpAddress'] = self.ip_address
        result['UsingStatus'] = self.using_status
        result['ApAccessEnabled'] = self.ap_access_enabled
        return result

    def from_map(self, map={}):
        self.allocation_id = map.get('AllocationId')
        self.ip_address = map.get('IpAddress')
        self.using_status = map.get('UsingStatus')
        self.ap_access_enabled = map.get('ApAccessEnabled')
        return self


class DescribeBandwidthPackagesResponseBandwidthPackagesBandwidthPackagePublicIpAddresses(TeaModel):
    def __init__(self, public_ip_addresse=None):
        self.public_ip_addresse = public_ip_addresse

    def validate(self):
        self.validate_required(self.public_ip_addresse, 'public_ip_addresse')
        if self.public_ip_addresse:
            for k in self.public_ip_addresse:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PublicIpAddresse'] = []
        if self.public_ip_addresse is not None:
            for k in self.public_ip_addresse:
                result['PublicIpAddresse'].append(k.to_map() if k else None)
        else:
            result['PublicIpAddresse'] = None
        return result

    def from_map(self, map={}):
        self.public_ip_addresse = []
        if map.get('PublicIpAddresse') is not None:
            for k in map.get('PublicIpAddresse'):
                temp_model = DescribeBandwidthPackagesResponseBandwidthPackagesBandwidthPackagePublicIpAddressesPublicIpAddresse()
                self.public_ip_addresse.append(temp_model.from_map(k))
        else:
            self.public_ip_addresse = None
        return self


class DescribeBandwidthPackagesResponseBandwidthPackagesBandwidthPackage(TeaModel):
    def __init__(self, bandwidth_package_id=None, region_id=None, name=None, description=None, zone_id=None,
                 nat_gateway_id=None, bandwidth=None, instance_charge_type=None, internet_charge_type=None, business_status=None,
                 ip_count=None, creation_time=None, status=None, isp=None, public_ip_addresses=None):
        self.bandwidth_package_id = bandwidth_package_id
        self.region_id = region_id
        self.name = name
        self.description = description
        self.zone_id = zone_id
        self.nat_gateway_id = nat_gateway_id
        self.bandwidth = bandwidth
        self.instance_charge_type = instance_charge_type
        self.internet_charge_type = internet_charge_type
        self.business_status = business_status
        self.ip_count = ip_count
        self.creation_time = creation_time
        self.status = status
        self.isp = isp
        self.public_ip_addresses = public_ip_addresses  # type: DescribeBandwidthPackagesResponseBandwidthPackagesBandwidthPackagePublicIpAddresses

    def validate(self):
        self.validate_required(self.bandwidth_package_id, 'bandwidth_package_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.zone_id, 'zone_id')
        self.validate_required(self.nat_gateway_id, 'nat_gateway_id')
        self.validate_required(self.bandwidth, 'bandwidth')
        self.validate_required(self.instance_charge_type, 'instance_charge_type')
        self.validate_required(self.internet_charge_type, 'internet_charge_type')
        self.validate_required(self.business_status, 'business_status')
        self.validate_required(self.ip_count, 'ip_count')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.isp, 'isp')
        self.validate_required(self.public_ip_addresses, 'public_ip_addresses')
        if self.public_ip_addresses:
            self.public_ip_addresses.validate()

    def to_map(self):
        result = {}
        result['BandwidthPackageId'] = self.bandwidth_package_id
        result['RegionId'] = self.region_id
        result['Name'] = self.name
        result['Description'] = self.description
        result['ZoneId'] = self.zone_id
        result['NatGatewayId'] = self.nat_gateway_id
        result['Bandwidth'] = self.bandwidth
        result['InstanceChargeType'] = self.instance_charge_type
        result['InternetChargeType'] = self.internet_charge_type
        result['BusinessStatus'] = self.business_status
        result['IpCount'] = self.ip_count
        result['CreationTime'] = self.creation_time
        result['Status'] = self.status
        result['ISP'] = self.isp
        if self.public_ip_addresses is not None:
            result['PublicIpAddresses'] = self.public_ip_addresses.to_map()
        else:
            result['PublicIpAddresses'] = None
        return result

    def from_map(self, map={}):
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        self.region_id = map.get('RegionId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.zone_id = map.get('ZoneId')
        self.nat_gateway_id = map.get('NatGatewayId')
        self.bandwidth = map.get('Bandwidth')
        self.instance_charge_type = map.get('InstanceChargeType')
        self.internet_charge_type = map.get('InternetChargeType')
        self.business_status = map.get('BusinessStatus')
        self.ip_count = map.get('IpCount')
        self.creation_time = map.get('CreationTime')
        self.status = map.get('Status')
        self.isp = map.get('ISP')
        if map.get('PublicIpAddresses') is not None:
            temp_model = DescribeBandwidthPackagesResponseBandwidthPackagesBandwidthPackagePublicIpAddresses()
            self.public_ip_addresses = temp_model.from_map(map['PublicIpAddresses'])
        else:
            self.public_ip_addresses = None
        return self


class DescribeBandwidthPackagesResponseBandwidthPackages(TeaModel):
    def __init__(self, bandwidth_package=None):
        self.bandwidth_package = bandwidth_package

    def validate(self):
        self.validate_required(self.bandwidth_package, 'bandwidth_package')
        if self.bandwidth_package:
            for k in self.bandwidth_package:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['BandwidthPackage'] = []
        if self.bandwidth_package is not None:
            for k in self.bandwidth_package:
                result['BandwidthPackage'].append(k.to_map() if k else None)
        else:
            result['BandwidthPackage'] = None
        return result

    def from_map(self, map={}):
        self.bandwidth_package = []
        if map.get('BandwidthPackage') is not None:
            for k in map.get('BandwidthPackage'):
                temp_model = DescribeBandwidthPackagesResponseBandwidthPackagesBandwidthPackage()
                self.bandwidth_package.append(temp_model.from_map(k))
        else:
            self.bandwidth_package = None
        return self


class DescribeAccessPointsRequest(TeaModel):
    def __init__(self, region_id=None, page_number=None, page_size=None):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size

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


class DescribeAccessPointsResponse(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None, access_point_set=None):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.access_point_set = access_point_set  # type: DescribeAccessPointsResponseAccessPointSet

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.access_point_set, 'access_point_set')
        if self.access_point_set:
            self.access_point_set.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        if self.access_point_set is not None:
            result['AccessPointSet'] = self.access_point_set.to_map()
        else:
            result['AccessPointSet'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        if map.get('AccessPointSet') is not None:
            temp_model = DescribeAccessPointsResponseAccessPointSet()
            self.access_point_set = temp_model.from_map(map['AccessPointSet'])
        else:
            self.access_point_set = None
        return self


class DescribeAccessPointsResponseAccessPointSetAccessPointTypeAccessPointFeatureModelsAccessPointFeatureModel(TeaModel):
    def __init__(self, feature_key=None, feature_value=None):
        self.feature_key = feature_key
        self.feature_value = feature_value

    def validate(self):
        self.validate_required(self.feature_key, 'feature_key')
        self.validate_required(self.feature_value, 'feature_value')

    def to_map(self):
        result = {}
        result['FeatureKey'] = self.feature_key
        result['FeatureValue'] = self.feature_value
        return result

    def from_map(self, map={}):
        self.feature_key = map.get('FeatureKey')
        self.feature_value = map.get('FeatureValue')
        return self


class DescribeAccessPointsResponseAccessPointSetAccessPointTypeAccessPointFeatureModels(TeaModel):
    def __init__(self, access_point_feature_model=None):
        self.access_point_feature_model = access_point_feature_model

    def validate(self):
        self.validate_required(self.access_point_feature_model, 'access_point_feature_model')
        if self.access_point_feature_model:
            for k in self.access_point_feature_model:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['AccessPointFeatureModel'] = []
        if self.access_point_feature_model is not None:
            for k in self.access_point_feature_model:
                result['AccessPointFeatureModel'].append(k.to_map() if k else None)
        else:
            result['AccessPointFeatureModel'] = None
        return result

    def from_map(self, map={}):
        self.access_point_feature_model = []
        if map.get('AccessPointFeatureModel') is not None:
            for k in map.get('AccessPointFeatureModel'):
                temp_model = DescribeAccessPointsResponseAccessPointSetAccessPointTypeAccessPointFeatureModelsAccessPointFeatureModel()
                self.access_point_feature_model.append(temp_model.from_map(k))
        else:
            self.access_point_feature_model = None
        return self


class DescribeAccessPointsResponseAccessPointSetAccessPointType(TeaModel):
    def __init__(self, access_point_id=None, status=None, type=None, attached_region_no=None, location=None,
                 host_operator=None, name=None, description=None, access_point_feature_models=None):
        self.access_point_id = access_point_id
        self.status = status
        self.type = type
        self.attached_region_no = attached_region_no
        self.location = location
        self.host_operator = host_operator
        self.name = name
        self.description = description
        self.access_point_feature_models = access_point_feature_models  # type: DescribeAccessPointsResponseAccessPointSetAccessPointTypeAccessPointFeatureModels

    def validate(self):
        self.validate_required(self.access_point_id, 'access_point_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.type, 'type')
        self.validate_required(self.attached_region_no, 'attached_region_no')
        self.validate_required(self.location, 'location')
        self.validate_required(self.host_operator, 'host_operator')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.access_point_feature_models, 'access_point_feature_models')
        if self.access_point_feature_models:
            self.access_point_feature_models.validate()

    def to_map(self):
        result = {}
        result['AccessPointId'] = self.access_point_id
        result['Status'] = self.status
        result['Type'] = self.type
        result['AttachedRegionNo'] = self.attached_region_no
        result['Location'] = self.location
        result['HostOperator'] = self.host_operator
        result['Name'] = self.name
        result['Description'] = self.description
        if self.access_point_feature_models is not None:
            result['AccessPointFeatureModels'] = self.access_point_feature_models.to_map()
        else:
            result['AccessPointFeatureModels'] = None
        return result

    def from_map(self, map={}):
        self.access_point_id = map.get('AccessPointId')
        self.status = map.get('Status')
        self.type = map.get('Type')
        self.attached_region_no = map.get('AttachedRegionNo')
        self.location = map.get('Location')
        self.host_operator = map.get('HostOperator')
        self.name = map.get('Name')
        self.description = map.get('Description')
        if map.get('AccessPointFeatureModels') is not None:
            temp_model = DescribeAccessPointsResponseAccessPointSetAccessPointTypeAccessPointFeatureModels()
            self.access_point_feature_models = temp_model.from_map(map['AccessPointFeatureModels'])
        else:
            self.access_point_feature_models = None
        return self


class DescribeAccessPointsResponseAccessPointSet(TeaModel):
    def __init__(self, access_point_type=None):
        self.access_point_type = access_point_type

    def validate(self):
        self.validate_required(self.access_point_type, 'access_point_type')
        if self.access_point_type:
            for k in self.access_point_type:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['AccessPointType'] = []
        if self.access_point_type is not None:
            for k in self.access_point_type:
                result['AccessPointType'].append(k.to_map() if k else None)
        else:
            result['AccessPointType'] = None
        return result

    def from_map(self, map={}):
        self.access_point_type = []
        if map.get('AccessPointType') is not None:
            for k in map.get('AccessPointType'):
                temp_model = DescribeAccessPointsResponseAccessPointSetAccessPointType()
                self.access_point_type.append(temp_model.from_map(k))
        else:
            self.access_point_type = None
        return self


class DeleteVSwitchRequest(TeaModel):
    def __init__(self, v_switch_id=None, region_id=None):
        self.v_switch_id = v_switch_id
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.v_switch_id, 'v_switch_id')

    def to_map(self):
        result = {}
        result['VSwitchId'] = self.v_switch_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.v_switch_id = map.get('VSwitchId')
        self.region_id = map.get('RegionId')
        return self


class DeleteVSwitchResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteVpcRequest(TeaModel):
    def __init__(self, vpc_id=None, region_id=None):
        self.vpc_id = vpc_id
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.vpc_id, 'vpc_id')

    def to_map(self):
        result = {}
        result['VpcId'] = self.vpc_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.vpc_id = map.get('VpcId')
        self.region_id = map.get('RegionId')
        return self


class DeleteVpcResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteVirtualBorderRouterRequest(TeaModel):
    def __init__(self, region_id=None, vbr_id=None, client_token=None):
        self.region_id = region_id
        self.vbr_id = vbr_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vbr_id, 'vbr_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VbrId'] = self.vbr_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vbr_id = map.get('VbrId')
        self.client_token = map.get('ClientToken')
        return self


class DeleteVirtualBorderRouterResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteRouterInterfaceRequest(TeaModel):
    def __init__(self, region_id=None, router_interface_id=None, client_token=None):
        self.region_id = region_id
        self.router_interface_id = router_interface_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.router_interface_id, 'router_interface_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['RouterInterfaceId'] = self.router_interface_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.router_interface_id = map.get('RouterInterfaceId')
        self.client_token = map.get('ClientToken')
        return self


class DeleteRouterInterfaceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteRouteEntryRequest(TeaModel):
    def __init__(self, region_id=None, route_table_id=None, route_entry_id=None, destination_cidr_block=None,
                 next_hop_id=None, next_hop_list=None):
        self.region_id = region_id
        self.route_table_id = route_table_id
        self.route_entry_id = route_entry_id
        self.destination_cidr_block = destination_cidr_block
        self.next_hop_id = next_hop_id
        self.next_hop_list = next_hop_list

    def validate(self):
        if self.next_hop_list:
            for k in self.next_hop_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['RouteTableId'] = self.route_table_id
        result['RouteEntryId'] = self.route_entry_id
        result['DestinationCidrBlock'] = self.destination_cidr_block
        result['NextHopId'] = self.next_hop_id
        result['NextHopList'] = []
        if self.next_hop_list is not None:
            for k in self.next_hop_list:
                result['NextHopList'].append(k.to_map() if k else None)
        else:
            result['NextHopList'] = None
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.route_table_id = map.get('RouteTableId')
        self.route_entry_id = map.get('RouteEntryId')
        self.destination_cidr_block = map.get('DestinationCidrBlock')
        self.next_hop_id = map.get('NextHopId')
        self.next_hop_list = []
        if map.get('NextHopList') is not None:
            for k in map.get('NextHopList'):
                temp_model = DeleteRouteEntryRequestNextHopList()
                self.next_hop_list.append(temp_model.from_map(k))
        else:
            self.next_hop_list = None
        return self


class DeleteRouteEntryRequestNextHopList(TeaModel):
    def __init__(self, next_hop_type=None, next_hop_id=None):
        self.next_hop_type = next_hop_type
        self.next_hop_id = next_hop_id

    def validate(self):
        self.validate_required(self.next_hop_type, 'next_hop_type')
        self.validate_required(self.next_hop_id, 'next_hop_id')

    def to_map(self):
        result = {}
        result['NextHopType'] = self.next_hop_type
        result['NextHopId'] = self.next_hop_id
        return result

    def from_map(self, map={}):
        self.next_hop_type = map.get('NextHopType')
        self.next_hop_id = map.get('NextHopId')
        return self


class DeleteRouteEntryResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeletePhysicalConnectionRequest(TeaModel):
    def __init__(self, region_id=None, physical_connection_id=None, client_token=None):
        self.region_id = region_id
        self.physical_connection_id = physical_connection_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.physical_connection_id, 'physical_connection_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['PhysicalConnectionId'] = self.physical_connection_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.physical_connection_id = map.get('PhysicalConnectionId')
        self.client_token = map.get('ClientToken')
        return self


class DeletePhysicalConnectionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteNatGatewayRequest(TeaModel):
    def __init__(self, region_id=None, nat_gateway_id=None, force=None):
        self.region_id = region_id
        self.nat_gateway_id = nat_gateway_id
        self.force = force

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.nat_gateway_id, 'nat_gateway_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['NatGatewayId'] = self.nat_gateway_id
        result['Force'] = self.force
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.nat_gateway_id = map.get('NatGatewayId')
        self.force = map.get('Force')
        return self


class DeleteNatGatewayResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteHaVipRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, ha_vip_id=None):
        self.client_token = client_token
        self.region_id = region_id
        self.ha_vip_id = ha_vip_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ha_vip_id, 'ha_vip_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['HaVipId'] = self.ha_vip_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.ha_vip_id = map.get('HaVipId')
        return self


class DeleteHaVipResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteForwardEntryRequest(TeaModel):
    def __init__(self, region_id=None, forward_table_id=None, forward_entry_id=None, client_token=None):
        self.region_id = region_id
        self.forward_table_id = forward_table_id
        self.forward_entry_id = forward_entry_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.forward_table_id, 'forward_table_id')
        self.validate_required(self.forward_entry_id, 'forward_entry_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ForwardTableId'] = self.forward_table_id
        result['ForwardEntryId'] = self.forward_entry_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.forward_table_id = map.get('ForwardTableId')
        self.forward_entry_id = map.get('ForwardEntryId')
        self.client_token = map.get('ClientToken')
        return self


class DeleteForwardEntryResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteBandwidthPackageRequest(TeaModel):
    def __init__(self, region_id=None, bandwidth_package_id=None, force=None):
        self.region_id = region_id
        self.bandwidth_package_id = bandwidth_package_id
        self.force = force

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bandwidth_package_id, 'bandwidth_package_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['BandwidthPackageId'] = self.bandwidth_package_id
        result['Force'] = self.force
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        self.force = map.get('Force')
        return self


class DeleteBandwidthPackageResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeactivateRouterInterfaceRequest(TeaModel):
    def __init__(self, region_id=None, router_interface_id=None):
        self.region_id = region_id
        self.router_interface_id = router_interface_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.router_interface_id, 'router_interface_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['RouterInterfaceId'] = self.router_interface_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.router_interface_id = map.get('RouterInterfaceId')
        return self


class DeactivateRouterInterfaceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateVSwitchRequest(TeaModel):
    def __init__(self, zone_id=None, region_id=None, cidr_block=None, ipv_6cidr_block=None, vpc_id=None,
                 v_switch_name=None, description=None, client_token=None):
        self.zone_id = zone_id
        self.region_id = region_id
        self.cidr_block = cidr_block
        self.ipv_6cidr_block = ipv_6cidr_block
        self.vpc_id = vpc_id
        self.v_switch_name = v_switch_name
        self.description = description
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.zone_id, 'zone_id')
        self.validate_required(self.cidr_block, 'cidr_block')
        self.validate_required(self.vpc_id, 'vpc_id')

    def to_map(self):
        result = {}
        result['ZoneId'] = self.zone_id
        result['RegionId'] = self.region_id
        result['CidrBlock'] = self.cidr_block
        result['Ipv6CidrBlock'] = self.ipv_6cidr_block
        result['VpcId'] = self.vpc_id
        result['VSwitchName'] = self.v_switch_name
        result['Description'] = self.description
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.zone_id = map.get('ZoneId')
        self.region_id = map.get('RegionId')
        self.cidr_block = map.get('CidrBlock')
        self.ipv_6cidr_block = map.get('Ipv6CidrBlock')
        self.vpc_id = map.get('VpcId')
        self.v_switch_name = map.get('VSwitchName')
        self.description = map.get('Description')
        self.client_token = map.get('ClientToken')
        return self


class CreateVSwitchResponse(TeaModel):
    def __init__(self, request_id=None, v_switch_id=None):
        self.request_id = request_id
        self.v_switch_id = v_switch_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.v_switch_id, 'v_switch_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.v_switch_id = map.get('VSwitchId')
        return self


class CreateVpcRequest(TeaModel):
    def __init__(self, region_id=None, cidr_block=None, ipv_6cidr_block=None, enable_ipv_6=None, vpc_name=None,
                 description=None, resource_group_id=None, dry_run=None, user_cidr=None, client_token=None):
        self.region_id = region_id
        self.cidr_block = cidr_block
        self.ipv_6cidr_block = ipv_6cidr_block
        self.enable_ipv_6 = enable_ipv_6
        self.vpc_name = vpc_name
        self.description = description
        self.resource_group_id = resource_group_id
        self.dry_run = dry_run
        self.user_cidr = user_cidr
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['CidrBlock'] = self.cidr_block
        result['Ipv6CidrBlock'] = self.ipv_6cidr_block
        result['EnableIpv6'] = self.enable_ipv_6
        result['VpcName'] = self.vpc_name
        result['Description'] = self.description
        result['ResourceGroupId'] = self.resource_group_id
        result['DryRun'] = self.dry_run
        result['UserCidr'] = self.user_cidr
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.cidr_block = map.get('CidrBlock')
        self.ipv_6cidr_block = map.get('Ipv6CidrBlock')
        self.enable_ipv_6 = map.get('EnableIpv6')
        self.vpc_name = map.get('VpcName')
        self.description = map.get('Description')
        self.resource_group_id = map.get('ResourceGroupId')
        self.dry_run = map.get('DryRun')
        self.user_cidr = map.get('UserCidr')
        self.client_token = map.get('ClientToken')
        return self


class CreateVpcResponse(TeaModel):
    def __init__(self, request_id=None, vpc_id=None, vrouter_id=None, route_table_id=None, resource_group_id=None):
        self.request_id = request_id
        self.vpc_id = vpc_id
        self.vrouter_id = vrouter_id
        self.route_table_id = route_table_id
        self.resource_group_id = resource_group_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.vrouter_id, 'vrouter_id')
        self.validate_required(self.route_table_id, 'route_table_id')
        self.validate_required(self.resource_group_id, 'resource_group_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['VpcId'] = self.vpc_id
        result['VRouterId'] = self.vrouter_id
        result['RouteTableId'] = self.route_table_id
        result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.vpc_id = map.get('VpcId')
        self.vrouter_id = map.get('VRouterId')
        self.route_table_id = map.get('RouteTableId')
        self.resource_group_id = map.get('ResourceGroupId')
        return self


class CreateVirtualBorderRouterRequest(TeaModel):
    def __init__(self, region_id=None, physical_connection_id=None, vbr_owner_id=None, vlan_id=None,
                 circuit_code=None, local_gateway_ip=None, peer_gateway_ip=None, peering_subnet_mask=None, description=None,
                 name=None, client_token=None, local_ipv_6gateway_ip=None, peer_ipv_6gateway_ip=None,
                 peering_ipv_6subnet_mask=None, enable_ipv_6=None):
        self.region_id = region_id
        self.physical_connection_id = physical_connection_id
        self.vbr_owner_id = vbr_owner_id
        self.vlan_id = vlan_id
        self.circuit_code = circuit_code
        self.local_gateway_ip = local_gateway_ip
        self.peer_gateway_ip = peer_gateway_ip
        self.peering_subnet_mask = peering_subnet_mask
        self.description = description
        self.name = name
        self.client_token = client_token
        self.local_ipv_6gateway_ip = local_ipv_6gateway_ip
        self.peer_ipv_6gateway_ip = peer_ipv_6gateway_ip
        self.peering_ipv_6subnet_mask = peering_ipv_6subnet_mask
        self.enable_ipv_6 = enable_ipv_6

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.physical_connection_id, 'physical_connection_id')
        self.validate_required(self.vlan_id, 'vlan_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['PhysicalConnectionId'] = self.physical_connection_id
        result['VbrOwnerId'] = self.vbr_owner_id
        result['VlanId'] = self.vlan_id
        result['CircuitCode'] = self.circuit_code
        result['LocalGatewayIp'] = self.local_gateway_ip
        result['PeerGatewayIp'] = self.peer_gateway_ip
        result['PeeringSubnetMask'] = self.peering_subnet_mask
        result['Description'] = self.description
        result['Name'] = self.name
        result['ClientToken'] = self.client_token
        result['LocalIpv6GatewayIp'] = self.local_ipv_6gateway_ip
        result['PeerIpv6GatewayIp'] = self.peer_ipv_6gateway_ip
        result['PeeringIpv6SubnetMask'] = self.peering_ipv_6subnet_mask
        result['EnableIpv6'] = self.enable_ipv_6
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.physical_connection_id = map.get('PhysicalConnectionId')
        self.vbr_owner_id = map.get('VbrOwnerId')
        self.vlan_id = map.get('VlanId')
        self.circuit_code = map.get('CircuitCode')
        self.local_gateway_ip = map.get('LocalGatewayIp')
        self.peer_gateway_ip = map.get('PeerGatewayIp')
        self.peering_subnet_mask = map.get('PeeringSubnetMask')
        self.description = map.get('Description')
        self.name = map.get('Name')
        self.client_token = map.get('ClientToken')
        self.local_ipv_6gateway_ip = map.get('LocalIpv6GatewayIp')
        self.peer_ipv_6gateway_ip = map.get('PeerIpv6GatewayIp')
        self.peering_ipv_6subnet_mask = map.get('PeeringIpv6SubnetMask')
        self.enable_ipv_6 = map.get('EnableIpv6')
        return self


class CreateVirtualBorderRouterResponse(TeaModel):
    def __init__(self, request_id=None, vbr_id=None):
        self.request_id = request_id
        self.vbr_id = vbr_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.vbr_id, 'vbr_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['VbrId'] = self.vbr_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.vbr_id = map.get('VbrId')
        return self


class CreateRouterInterfaceRequest(TeaModel):
    def __init__(self, region_id=None, role=None, opposite_region_id=None, spec=None, router_type=None,
                 router_id=None, opposite_interface_id=None, opposite_router_id=None, opposite_router_type=None,
                 opposite_interface_owner_id=None, health_check_source_ip=None, health_check_target_ip=None, access_point_id=None,
                 opposite_access_point_id=None, description=None, name=None, period=None, instance_charge_type=None, auto_pay=None,
                 pricing_cycle=None, client_token=None):
        self.region_id = region_id
        self.role = role
        self.opposite_region_id = opposite_region_id
        self.spec = spec
        self.router_type = router_type
        self.router_id = router_id
        self.opposite_interface_id = opposite_interface_id
        self.opposite_router_id = opposite_router_id
        self.opposite_router_type = opposite_router_type
        self.opposite_interface_owner_id = opposite_interface_owner_id
        self.health_check_source_ip = health_check_source_ip
        self.health_check_target_ip = health_check_target_ip
        self.access_point_id = access_point_id
        self.opposite_access_point_id = opposite_access_point_id
        self.description = description
        self.name = name
        self.period = period
        self.instance_charge_type = instance_charge_type
        self.auto_pay = auto_pay
        self.pricing_cycle = pricing_cycle
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.role, 'role')
        self.validate_required(self.opposite_region_id, 'opposite_region_id')
        self.validate_required(self.spec, 'spec')
        self.validate_required(self.router_type, 'router_type')
        self.validate_required(self.router_id, 'router_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Role'] = self.role
        result['OppositeRegionId'] = self.opposite_region_id
        result['Spec'] = self.spec
        result['RouterType'] = self.router_type
        result['RouterId'] = self.router_id
        result['OppositeInterfaceId'] = self.opposite_interface_id
        result['OppositeRouterId'] = self.opposite_router_id
        result['OppositeRouterType'] = self.opposite_router_type
        result['OppositeInterfaceOwnerId'] = self.opposite_interface_owner_id
        result['HealthCheckSourceIp'] = self.health_check_source_ip
        result['HealthCheckTargetIp'] = self.health_check_target_ip
        result['AccessPointId'] = self.access_point_id
        result['OppositeAccessPointId'] = self.opposite_access_point_id
        result['Description'] = self.description
        result['Name'] = self.name
        result['Period'] = self.period
        result['InstanceChargeType'] = self.instance_charge_type
        result['AutoPay'] = self.auto_pay
        result['PricingCycle'] = self.pricing_cycle
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.role = map.get('Role')
        self.opposite_region_id = map.get('OppositeRegionId')
        self.spec = map.get('Spec')
        self.router_type = map.get('RouterType')
        self.router_id = map.get('RouterId')
        self.opposite_interface_id = map.get('OppositeInterfaceId')
        self.opposite_router_id = map.get('OppositeRouterId')
        self.opposite_router_type = map.get('OppositeRouterType')
        self.opposite_interface_owner_id = map.get('OppositeInterfaceOwnerId')
        self.health_check_source_ip = map.get('HealthCheckSourceIp')
        self.health_check_target_ip = map.get('HealthCheckTargetIp')
        self.access_point_id = map.get('AccessPointId')
        self.opposite_access_point_id = map.get('OppositeAccessPointId')
        self.description = map.get('Description')
        self.name = map.get('Name')
        self.period = map.get('Period')
        self.instance_charge_type = map.get('InstanceChargeType')
        self.auto_pay = map.get('AutoPay')
        self.pricing_cycle = map.get('PricingCycle')
        self.client_token = map.get('ClientToken')
        return self


class CreateRouterInterfaceResponse(TeaModel):
    def __init__(self, request_id=None, router_interface_id=None, order_id=None):
        self.request_id = request_id
        self.router_interface_id = router_interface_id
        self.order_id = order_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.router_interface_id, 'router_interface_id')
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['RouterInterfaceId'] = self.router_interface_id
        result['OrderId'] = self.order_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.router_interface_id = map.get('RouterInterfaceId')
        self.order_id = map.get('OrderId')
        return self


class CreateRouteEntryRequest(TeaModel):
    def __init__(self, region_id=None, route_table_id=None, destination_cidr_block=None, next_hop_id=None,
                 client_token=None, route_entry_name=None, description=None, next_hop_type=None, next_hop_list=None):
        self.region_id = region_id
        self.route_table_id = route_table_id
        self.destination_cidr_block = destination_cidr_block
        self.next_hop_id = next_hop_id
        self.client_token = client_token
        self.route_entry_name = route_entry_name
        self.description = description
        self.next_hop_type = next_hop_type
        self.next_hop_list = next_hop_list

    def validate(self):
        self.validate_required(self.route_table_id, 'route_table_id')
        self.validate_required(self.destination_cidr_block, 'destination_cidr_block')
        if self.next_hop_list:
            for k in self.next_hop_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['RouteTableId'] = self.route_table_id
        result['DestinationCidrBlock'] = self.destination_cidr_block
        result['NextHopId'] = self.next_hop_id
        result['ClientToken'] = self.client_token
        result['RouteEntryName'] = self.route_entry_name
        result['Description'] = self.description
        result['NextHopType'] = self.next_hop_type
        result['NextHopList'] = []
        if self.next_hop_list is not None:
            for k in self.next_hop_list:
                result['NextHopList'].append(k.to_map() if k else None)
        else:
            result['NextHopList'] = None
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.route_table_id = map.get('RouteTableId')
        self.destination_cidr_block = map.get('DestinationCidrBlock')
        self.next_hop_id = map.get('NextHopId')
        self.client_token = map.get('ClientToken')
        self.route_entry_name = map.get('RouteEntryName')
        self.description = map.get('Description')
        self.next_hop_type = map.get('NextHopType')
        self.next_hop_list = []
        if map.get('NextHopList') is not None:
            for k in map.get('NextHopList'):
                temp_model = CreateRouteEntryRequestNextHopList()
                self.next_hop_list.append(temp_model.from_map(k))
        else:
            self.next_hop_list = None
        return self


class CreateRouteEntryRequestNextHopList(TeaModel):
    def __init__(self, next_hop_type=None, next_hop_id=None, weight=None):
        self.next_hop_type = next_hop_type
        self.next_hop_id = next_hop_id
        self.weight = weight

    def validate(self):
        self.validate_required(self.next_hop_type, 'next_hop_type')
        self.validate_required(self.next_hop_id, 'next_hop_id')
        self.validate_required(self.weight, 'weight')

    def to_map(self):
        result = {}
        result['NextHopType'] = self.next_hop_type
        result['NextHopId'] = self.next_hop_id
        result['Weight'] = self.weight
        return result

    def from_map(self, map={}):
        self.next_hop_type = map.get('NextHopType')
        self.next_hop_id = map.get('NextHopId')
        self.weight = map.get('Weight')
        return self


class CreateRouteEntryResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreatePhysicalConnectionRequest(TeaModel):
    def __init__(self, region_id=None, access_point_id=None, type=None, line_operator=None, bandwidth=None,
                 peer_location=None, port_type=None, redundant_physical_connection_id=None, description=None, name=None,
                 circuit_code=None, client_token=None):
        self.region_id = region_id
        self.access_point_id = access_point_id
        self.type = type
        self.line_operator = line_operator
        self.bandwidth = bandwidth
        self.peer_location = peer_location
        self.port_type = port_type
        self.redundant_physical_connection_id = redundant_physical_connection_id
        self.description = description
        self.name = name
        self.circuit_code = circuit_code
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.access_point_id, 'access_point_id')
        self.validate_required(self.line_operator, 'line_operator')
        self.validate_required(self.peer_location, 'peer_location')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['AccessPointId'] = self.access_point_id
        result['Type'] = self.type
        result['LineOperator'] = self.line_operator
        result['bandwidth'] = self.bandwidth
        result['PeerLocation'] = self.peer_location
        result['PortType'] = self.port_type
        result['RedundantPhysicalConnectionId'] = self.redundant_physical_connection_id
        result['Description'] = self.description
        result['Name'] = self.name
        result['CircuitCode'] = self.circuit_code
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.access_point_id = map.get('AccessPointId')
        self.type = map.get('Type')
        self.line_operator = map.get('LineOperator')
        self.bandwidth = map.get('bandwidth')
        self.peer_location = map.get('PeerLocation')
        self.port_type = map.get('PortType')
        self.redundant_physical_connection_id = map.get('RedundantPhysicalConnectionId')
        self.description = map.get('Description')
        self.name = map.get('Name')
        self.circuit_code = map.get('CircuitCode')
        self.client_token = map.get('ClientToken')
        return self


class CreatePhysicalConnectionResponse(TeaModel):
    def __init__(self, request_id=None, physical_connection_id=None):
        self.request_id = request_id
        self.physical_connection_id = physical_connection_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.physical_connection_id, 'physical_connection_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PhysicalConnectionId'] = self.physical_connection_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.physical_connection_id = map.get('PhysicalConnectionId')
        return self


class CreateNatGatewayRequest(TeaModel):
    def __init__(self, region_id=None, vpc_id=None, name=None, description=None, client_token=None, spec=None,
                 bandwidth_package=None, instance_charge_type=None, pricing_cycle=None, duration=None, auto_pay=None,
                 v_switch_id=None, nat_type=None, internet_charge_type=None):
        self.region_id = region_id
        self.vpc_id = vpc_id
        self.name = name
        self.description = description
        self.client_token = client_token
        self.spec = spec
        self.bandwidth_package = bandwidth_package
        self.instance_charge_type = instance_charge_type
        self.pricing_cycle = pricing_cycle
        self.duration = duration
        self.auto_pay = auto_pay
        self.v_switch_id = v_switch_id
        self.nat_type = nat_type
        self.internet_charge_type = internet_charge_type

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        if self.bandwidth_package:
            for k in self.bandwidth_package:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['VpcId'] = self.vpc_id
        result['Name'] = self.name
        result['Description'] = self.description
        result['ClientToken'] = self.client_token
        result['Spec'] = self.spec
        result['BandwidthPackage'] = []
        if self.bandwidth_package is not None:
            for k in self.bandwidth_package:
                result['BandwidthPackage'].append(k.to_map() if k else None)
        else:
            result['BandwidthPackage'] = None
        result['InstanceChargeType'] = self.instance_charge_type
        result['PricingCycle'] = self.pricing_cycle
        result['Duration'] = self.duration
        result['AutoPay'] = self.auto_pay
        result['VSwitchId'] = self.v_switch_id
        result['NatType'] = self.nat_type
        result['InternetChargeType'] = self.internet_charge_type
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.vpc_id = map.get('VpcId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.client_token = map.get('ClientToken')
        self.spec = map.get('Spec')
        self.bandwidth_package = []
        if map.get('BandwidthPackage') is not None:
            for k in map.get('BandwidthPackage'):
                temp_model = CreateNatGatewayRequestBandwidthPackage()
                self.bandwidth_package.append(temp_model.from_map(k))
        else:
            self.bandwidth_package = None
        self.instance_charge_type = map.get('InstanceChargeType')
        self.pricing_cycle = map.get('PricingCycle')
        self.duration = map.get('Duration')
        self.auto_pay = map.get('AutoPay')
        self.v_switch_id = map.get('VSwitchId')
        self.nat_type = map.get('NatType')
        self.internet_charge_type = map.get('InternetChargeType')
        return self


class CreateNatGatewayRequestBandwidthPackage(TeaModel):
    def __init__(self, ip_count=None, bandwidth=None, zone=None, isp=None):
        self.ip_count = ip_count
        self.bandwidth = bandwidth
        self.zone = zone
        self.isp = isp

    def validate(self):
        self.validate_required(self.ip_count, 'ip_count')
        self.validate_required(self.bandwidth, 'bandwidth')
        self.validate_required(self.zone, 'zone')
        self.validate_required(self.isp, 'isp')

    def to_map(self):
        result = {}
        result['IpCount'] = self.ip_count
        result['Bandwidth'] = self.bandwidth
        result['Zone'] = self.zone
        result['ISP'] = self.isp
        return result

    def from_map(self, map={}):
        self.ip_count = map.get('IpCount')
        self.bandwidth = map.get('Bandwidth')
        self.zone = map.get('Zone')
        self.isp = map.get('ISP')
        return self


class CreateNatGatewayResponse(TeaModel):
    def __init__(self, request_id=None, nat_gateway_id=None, forward_table_ids=None, snat_table_ids=None,
                 bandwidth_package_ids=None):
        self.request_id = request_id
        self.nat_gateway_id = nat_gateway_id
        self.forward_table_ids = forward_table_ids  # type: CreateNatGatewayResponseForwardTableIds
        self.snat_table_ids = snat_table_ids  # type: CreateNatGatewayResponseSnatTableIds
        self.bandwidth_package_ids = bandwidth_package_ids  # type: CreateNatGatewayResponseBandwidthPackageIds

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.nat_gateway_id, 'nat_gateway_id')
        self.validate_required(self.forward_table_ids, 'forward_table_ids')
        if self.forward_table_ids:
            self.forward_table_ids.validate()
        self.validate_required(self.snat_table_ids, 'snat_table_ids')
        if self.snat_table_ids:
            self.snat_table_ids.validate()
        self.validate_required(self.bandwidth_package_ids, 'bandwidth_package_ids')
        if self.bandwidth_package_ids:
            self.bandwidth_package_ids.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['NatGatewayId'] = self.nat_gateway_id
        if self.forward_table_ids is not None:
            result['ForwardTableIds'] = self.forward_table_ids.to_map()
        else:
            result['ForwardTableIds'] = None
        if self.snat_table_ids is not None:
            result['SnatTableIds'] = self.snat_table_ids.to_map()
        else:
            result['SnatTableIds'] = None
        if self.bandwidth_package_ids is not None:
            result['BandwidthPackageIds'] = self.bandwidth_package_ids.to_map()
        else:
            result['BandwidthPackageIds'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.nat_gateway_id = map.get('NatGatewayId')
        if map.get('ForwardTableIds') is not None:
            temp_model = CreateNatGatewayResponseForwardTableIds()
            self.forward_table_ids = temp_model.from_map(map['ForwardTableIds'])
        else:
            self.forward_table_ids = None
        if map.get('SnatTableIds') is not None:
            temp_model = CreateNatGatewayResponseSnatTableIds()
            self.snat_table_ids = temp_model.from_map(map['SnatTableIds'])
        else:
            self.snat_table_ids = None
        if map.get('BandwidthPackageIds') is not None:
            temp_model = CreateNatGatewayResponseBandwidthPackageIds()
            self.bandwidth_package_ids = temp_model.from_map(map['BandwidthPackageIds'])
        else:
            self.bandwidth_package_ids = None
        return self


class CreateNatGatewayResponseForwardTableIds(TeaModel):
    def __init__(self, forward_table_id=None):
        self.forward_table_id = forward_table_id

    def validate(self):
        self.validate_required(self.forward_table_id, 'forward_table_id')

    def to_map(self):
        result = {}
        result['ForwardTableId'] = self.forward_table_id
        return result

    def from_map(self, map={}):
        self.forward_table_id = map.get('ForwardTableId')
        return self


class CreateNatGatewayResponseSnatTableIds(TeaModel):
    def __init__(self, snat_table_id=None):
        self.snat_table_id = snat_table_id

    def validate(self):
        self.validate_required(self.snat_table_id, 'snat_table_id')

    def to_map(self):
        result = {}
        result['SnatTableId'] = self.snat_table_id
        return result

    def from_map(self, map={}):
        self.snat_table_id = map.get('SnatTableId')
        return self


class CreateNatGatewayResponseBandwidthPackageIds(TeaModel):
    def __init__(self, bandwidth_package_id=None):
        self.bandwidth_package_id = bandwidth_package_id

    def validate(self):
        self.validate_required(self.bandwidth_package_id, 'bandwidth_package_id')

    def to_map(self):
        result = {}
        result['BandwidthPackageId'] = self.bandwidth_package_id
        return result

    def from_map(self, map={}):
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        return self


class CreateHaVipRequest(TeaModel):
    def __init__(self, name=None, client_token=None, region_id=None, v_switch_id=None, ip_address=None,
                 description=None):
        self.name = name
        self.client_token = client_token
        self.region_id = region_id
        self.v_switch_id = v_switch_id
        self.ip_address = ip_address
        self.description = description

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.v_switch_id, 'v_switch_id')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['VSwitchId'] = self.v_switch_id
        result['IpAddress'] = self.ip_address
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.v_switch_id = map.get('VSwitchId')
        self.ip_address = map.get('IpAddress')
        self.description = map.get('Description')
        return self


class CreateHaVipResponse(TeaModel):
    def __init__(self, request_id=None, ha_vip_id=None, ip_address=None):
        self.request_id = request_id
        self.ha_vip_id = ha_vip_id
        self.ip_address = ip_address

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.ha_vip_id, 'ha_vip_id')
        self.validate_required(self.ip_address, 'ip_address')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['HaVipId'] = self.ha_vip_id
        result['IpAddress'] = self.ip_address
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.ha_vip_id = map.get('HaVipId')
        self.ip_address = map.get('IpAddress')
        return self


class CreateForwardEntryRequest(TeaModel):
    def __init__(self, region_id=None, forward_table_id=None, external_ip=None, external_port=None,
                 internal_ip=None, internal_port=None, ip_protocol=None, forward_entry_name=None, client_token=None,
                 port_break=None):
        self.region_id = region_id
        self.forward_table_id = forward_table_id
        self.external_ip = external_ip
        self.external_port = external_port
        self.internal_ip = internal_ip
        self.internal_port = internal_port
        self.ip_protocol = ip_protocol
        self.forward_entry_name = forward_entry_name
        self.client_token = client_token
        self.port_break = port_break

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.forward_table_id, 'forward_table_id')
        self.validate_required(self.external_ip, 'external_ip')
        self.validate_required(self.external_port, 'external_port')
        self.validate_required(self.internal_ip, 'internal_ip')
        self.validate_required(self.internal_port, 'internal_port')
        self.validate_required(self.ip_protocol, 'ip_protocol')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ForwardTableId'] = self.forward_table_id
        result['ExternalIp'] = self.external_ip
        result['ExternalPort'] = self.external_port
        result['InternalIp'] = self.internal_ip
        result['InternalPort'] = self.internal_port
        result['IpProtocol'] = self.ip_protocol
        result['ForwardEntryName'] = self.forward_entry_name
        result['ClientToken'] = self.client_token
        result['PortBreak'] = self.port_break
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.forward_table_id = map.get('ForwardTableId')
        self.external_ip = map.get('ExternalIp')
        self.external_port = map.get('ExternalPort')
        self.internal_ip = map.get('InternalIp')
        self.internal_port = map.get('InternalPort')
        self.ip_protocol = map.get('IpProtocol')
        self.forward_entry_name = map.get('ForwardEntryName')
        self.client_token = map.get('ClientToken')
        self.port_break = map.get('PortBreak')
        return self


class CreateForwardEntryResponse(TeaModel):
    def __init__(self, request_id=None, forward_entry_id=None):
        self.request_id = request_id
        self.forward_entry_id = forward_entry_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.forward_entry_id, 'forward_entry_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ForwardEntryId'] = self.forward_entry_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.forward_entry_id = map.get('ForwardEntryId')
        return self


class ConnectRouterInterfaceRequest(TeaModel):
    def __init__(self, region_id=None, router_interface_id=None):
        self.region_id = region_id
        self.router_interface_id = router_interface_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.router_interface_id, 'router_interface_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['RouterInterfaceId'] = self.router_interface_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.router_interface_id = map.get('RouterInterfaceId')
        return self


class ConnectRouterInterfaceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CancelPhysicalConnectionRequest(TeaModel):
    def __init__(self, region_id=None, physical_connection_id=None, client_token=None):
        self.region_id = region_id
        self.physical_connection_id = physical_connection_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.physical_connection_id, 'physical_connection_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['PhysicalConnectionId'] = self.physical_connection_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.physical_connection_id = map.get('PhysicalConnectionId')
        self.client_token = map.get('ClientToken')
        return self


class CancelPhysicalConnectionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AssociateHaVipRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, ha_vip_id=None, instance_id=None):
        self.client_token = client_token
        self.region_id = region_id
        self.ha_vip_id = ha_vip_id
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ha_vip_id, 'ha_vip_id')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['HaVipId'] = self.ha_vip_id
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.ha_vip_id = map.get('HaVipId')
        self.instance_id = map.get('InstanceId')
        return self


class AssociateHaVipResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AssociateEipAddressRequest(TeaModel):
    def __init__(self, region_id=None, allocation_id=None, instance_id=None, instance_type=None,
                 instance_region_id=None, private_ip_address=None, mode=None, client_token=None):
        self.region_id = region_id
        self.allocation_id = allocation_id
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.instance_region_id = instance_region_id
        self.private_ip_address = private_ip_address
        self.mode = mode
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.allocation_id, 'allocation_id')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['AllocationId'] = self.allocation_id
        result['InstanceId'] = self.instance_id
        result['InstanceType'] = self.instance_type
        result['InstanceRegionId'] = self.instance_region_id
        result['PrivateIpAddress'] = self.private_ip_address
        result['Mode'] = self.mode
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.allocation_id = map.get('AllocationId')
        self.instance_id = map.get('InstanceId')
        self.instance_type = map.get('InstanceType')
        self.instance_region_id = map.get('InstanceRegionId')
        self.private_ip_address = map.get('PrivateIpAddress')
        self.mode = map.get('Mode')
        self.client_token = map.get('ClientToken')
        return self


class AssociateEipAddressResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AllocateEipAddressRequest(TeaModel):
    def __init__(self, region_id=None, bandwidth=None, period=None, isp=None, activity_id=None, netmode=None,
                 auto_pay=None, pricing_cycle=None, instance_charge_type=None, internet_charge_type=None,
                 resource_group_id=None, client_token=None):
        self.region_id = region_id
        self.bandwidth = bandwidth
        self.period = period
        self.isp = isp
        self.activity_id = activity_id
        self.netmode = netmode
        self.auto_pay = auto_pay
        self.pricing_cycle = pricing_cycle
        self.instance_charge_type = instance_charge_type
        self.internet_charge_type = internet_charge_type
        self.resource_group_id = resource_group_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Bandwidth'] = self.bandwidth
        result['Period'] = self.period
        result['ISP'] = self.isp
        result['ActivityId'] = self.activity_id
        result['Netmode'] = self.netmode
        result['AutoPay'] = self.auto_pay
        result['PricingCycle'] = self.pricing_cycle
        result['InstanceChargeType'] = self.instance_charge_type
        result['InternetChargeType'] = self.internet_charge_type
        result['ResourceGroupId'] = self.resource_group_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.bandwidth = map.get('Bandwidth')
        self.period = map.get('Period')
        self.isp = map.get('ISP')
        self.activity_id = map.get('ActivityId')
        self.netmode = map.get('Netmode')
        self.auto_pay = map.get('AutoPay')
        self.pricing_cycle = map.get('PricingCycle')
        self.instance_charge_type = map.get('InstanceChargeType')
        self.internet_charge_type = map.get('InternetChargeType')
        self.resource_group_id = map.get('ResourceGroupId')
        self.client_token = map.get('ClientToken')
        return self


class AllocateEipAddressResponse(TeaModel):
    def __init__(self, request_id=None, allocation_id=None, eip_address=None, order_id=None, resource_group_id=None):
        self.request_id = request_id
        self.allocation_id = allocation_id
        self.eip_address = eip_address
        self.order_id = order_id
        self.resource_group_id = resource_group_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.allocation_id, 'allocation_id')
        self.validate_required(self.eip_address, 'eip_address')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.resource_group_id, 'resource_group_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['AllocationId'] = self.allocation_id
        result['EipAddress'] = self.eip_address
        result['OrderId'] = self.order_id
        result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.allocation_id = map.get('AllocationId')
        self.eip_address = map.get('EipAddress')
        self.order_id = map.get('OrderId')
        self.resource_group_id = map.get('ResourceGroupId')
        return self


class AddBandwidthPackageIpsRequest(TeaModel):
    def __init__(self, region_id=None, bandwidth_package_id=None, ip_count=None, client_token=None):
        self.region_id = region_id
        self.bandwidth_package_id = bandwidth_package_id
        self.ip_count = ip_count
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bandwidth_package_id, 'bandwidth_package_id')
        self.validate_required(self.ip_count, 'ip_count')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['BandwidthPackageId'] = self.bandwidth_package_id
        result['IpCount'] = self.ip_count
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.bandwidth_package_id = map.get('BandwidthPackageId')
        self.ip_count = map.get('IpCount')
        self.client_token = map.get('ClientToken')
        return self


class AddBandwidthPackageIpsResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ActivateRouterInterfaceRequest(TeaModel):
    def __init__(self, region_id=None, router_interface_id=None):
        self.region_id = region_id
        self.router_interface_id = router_interface_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.router_interface_id, 'router_interface_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['RouterInterfaceId'] = self.router_interface_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.router_interface_id = map.get('RouterInterfaceId')
        return self


class ActivateRouterInterfaceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self
