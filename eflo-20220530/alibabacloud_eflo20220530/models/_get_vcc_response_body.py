# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class GetVccResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: main_models.GetVccResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Content') is not None:
            temp_model = main_models.GetVccResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetVccResponseBodyContent(DaraModel):
    def __init__(
        self,
        access_point_id: str = None,
        aliyun_router_info: List[main_models.GetVccResponseBodyContentAliyunRouterInfo] = None,
        attach_er_status: bool = None,
        bandwidth: int = None,
        bandwidth_str: str = None,
        bgp_asn: str = None,
        bgp_cidr: str = None,
        cen_id: str = None,
        cen_owner_id: str = None,
        cis_router_info: List[main_models.GetVccResponseBodyContentCisRouterInfo] = None,
        commodity_code: str = None,
        connection_type: str = None,
        create_time: str = None,
        current_node: str = None,
        duration: str = None,
        er_infos: List[main_models.GetVccResponseBodyContentErInfos] = None,
        expiration_date: str = None,
        gmt_modified: str = None,
        internet_charge_type: str = None,
        line_operator: str = None,
        message: str = None,
        pay_type: str = None,
        port_type: str = None,
        pricing_cycle: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        spec: str = None,
        status: str = None,
        tags: List[main_models.GetVccResponseBodyContentTags] = None,
        tenant_id: str = None,
        v_switch_id: str = None,
        vbr_infos: List[main_models.GetVccResponseBodyContentVbrInfos] = None,
        vcc_id: str = None,
        vcc_name: str = None,
        vpc_id: str = None,
        vpd_base_info: main_models.GetVccResponseBodyContentVpdBaseInfo = None,
        vpd_id: str = None,
        zone_id: str = None,
    ):
        # Express Connect circuit access point ID:
        # 
        # *   **ap-cn-wulanchabu-jn-ts-A**: Ulanqab-Jining-A
        # *   **ap-cn-heyuan-yc-ts-SA127**: Heyuan-Yuancheng-A
        self.access_point_id = access_point_id
        # Alibaba Cloud route information list
        self.aliyun_router_info = aliyun_router_info
        # Whether Lingjun HUB has been bound to a network instance
        # 
        # *   **true**: Bound
        # *   **false**: unbound
        self.attach_er_status = attach_er_status
        # bandwidth
        self.bandwidth = bandwidth
        # The bandwidth of the port.
        self.bandwidth_str = bandwidth_str
        # BGP AS number
        self.bgp_asn = bgp_asn
        # BGP CIDR block
        self.bgp_cidr = bgp_cidr
        # The ID of the CEN instance; [What is the CEN?](https://help.aliyun.com/document_detail/181681.html)
        # 
        # You can call the [DescribeCens](https://help.aliyun.com/document_detail/468215.htm) to query the information of CEN instances under the current Alibaba Cloud account.
        self.cen_id = cen_id
        # Account to which the CEN belongs
        self.cen_owner_id = cen_owner_id
        # Lingjun Network Routing Information List
        self.cis_router_info = cis_router_info
        # Commodity code
        self.commodity_code = commodity_code
        # The connection mode. Valid values:
        # 
        # *   **VPC**
        # *   **CENTR**
        self.connection_type = connection_type
        # The time when the data address was created.
        self.create_time = create_time
        # Current Node
        self.current_node = current_node
        # Cycle
        self.duration = duration
        # List of bound Lingjun HUB information
        self.er_infos = er_infos
        # The time when the application expired.
        self.expiration_date = expiration_date
        # The time when the agent was last modified.
        self.gmt_modified = gmt_modified
        # The billing method for network usage.
        # 
        # *   **PayByTraffic**: pay-by-traffic
        # *   **PayByBandwidth**: pay-by-bandwidth
        self.internet_charge_type = internet_charge_type
        # The connectivity provider of the Express Connect circuit. Valid values:
        # 
        # *   **CO**: other connectivity providers in the Chinese mainland
        self.line_operator = line_operator
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # The billing method of the instance. Valid values:
        # 
        # *   **PREPAY**: subscription
        # *   **POSTPAY**: pay-as-you-go
        self.pay_type = pay_type
        # The port type of the Express Connect circuit. Valid values:
        # 
        # *   **100GBase-LR**: 100,000 megabytes of single-mode optical port (10 km)
        self.port_type = port_type
        # The billing cycle. Valid values:
        # 
        # *   **Month**: Billed on a monthly basis
        # *   **Year**: Billed on an annual basis
        self.pricing_cycle = pricing_cycle
        # The region ID.
        self.region_id = region_id
        # The ID of your Alibaba Cloud resource group.
        # 
        # For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/94475.htm).
        self.resource_group_id = resource_group_id
        # Specification; value:
        # 
        # *   **Large**: Large
        self.spec = spec
        # The status of the cache reserve instance. Valid values:
        # 
        # *   **Available**: Normal.
        # *   **Not Available**: Not available.
        # *   **Executing**: The task is being executed.
        # *   **Deleting**: The account is being deleted
        self.status = status
        # The tag information.
        # 
        # You can specify up to 20 tags.
        self.tags = tags
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The ID of the vSwitch. [Virtual Private Cloud VSwitch](https://help.aliyun.com/document_detail/100380.html).
        # 
        # You can call the [DescribeVSwitches](https://help.aliyun.com/document_detail/35748.html) operation to query created vSwitches.
        self.v_switch_id = v_switch_id
        # Information list of border routers
        self.vbr_infos = vbr_infos
        # The ID of the Lingjun connection instance.
        self.vcc_id = vcc_id
        # The name of the Lingjun connection instance.
        self.vcc_name = vcc_name
        # Virtual Private Cloud IDs; [What is Virtual Private Cloud](https://help.aliyun.com/document_detail/34217.html)
        # 
        # You can call the [DescribeVpcs](https://help.aliyun.com/document_detail/35739.html#demo-0) operation to query the specified VPC.
        self.vpc_id = vpc_id
        # Lingjun network segment information (applicable to the scene where the old version of Lingjun connection is directly bound to Lingjun network segment)
        self.vpd_base_info = vpd_base_info
        # Lingjun CIDR block instance ID
        self.vpd_id = vpd_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.aliyun_router_info:
            for v1 in self.aliyun_router_info:
                 if v1:
                    v1.validate()
        if self.cis_router_info:
            for v1 in self.cis_router_info:
                 if v1:
                    v1.validate()
        if self.er_infos:
            for v1 in self.er_infos:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.vbr_infos:
            for v1 in self.vbr_infos:
                 if v1:
                    v1.validate()
        if self.vpd_base_info:
            self.vpd_base_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        result['AliyunRouterInfo'] = []
        if self.aliyun_router_info is not None:
            for k1 in self.aliyun_router_info:
                result['AliyunRouterInfo'].append(k1.to_map() if k1 else None)

        if self.attach_er_status is not None:
            result['AttachErStatus'] = self.attach_er_status

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.bandwidth_str is not None:
            result['BandwidthStr'] = self.bandwidth_str

        if self.bgp_asn is not None:
            result['BgpAsn'] = self.bgp_asn

        if self.bgp_cidr is not None:
            result['BgpCidr'] = self.bgp_cidr

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.cen_owner_id is not None:
            result['CenOwnerId'] = self.cen_owner_id

        result['CisRouterInfo'] = []
        if self.cis_router_info is not None:
            for k1 in self.cis_router_info:
                result['CisRouterInfo'].append(k1.to_map() if k1 else None)

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.current_node is not None:
            result['CurrentNode'] = self.current_node

        if self.duration is not None:
            result['Duration'] = self.duration

        result['ErInfos'] = []
        if self.er_infos is not None:
            for k1 in self.er_infos:
                result['ErInfos'].append(k1.to_map() if k1 else None)

        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.line_operator is not None:
            result['LineOperator'] = self.line_operator

        if self.message is not None:
            result['Message'] = self.message

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.port_type is not None:
            result['PortType'] = self.port_type

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        result['VbrInfos'] = []
        if self.vbr_infos is not None:
            for k1 in self.vbr_infos:
                result['VbrInfos'].append(k1.to_map() if k1 else None)

        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id

        if self.vcc_name is not None:
            result['VccName'] = self.vcc_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpd_base_info is not None:
            result['VpdBaseInfo'] = self.vpd_base_info.to_map()

        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        self.aliyun_router_info = []
        if m.get('AliyunRouterInfo') is not None:
            for k1 in m.get('AliyunRouterInfo'):
                temp_model = main_models.GetVccResponseBodyContentAliyunRouterInfo()
                self.aliyun_router_info.append(temp_model.from_map(k1))

        if m.get('AttachErStatus') is not None:
            self.attach_er_status = m.get('AttachErStatus')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BandwidthStr') is not None:
            self.bandwidth_str = m.get('BandwidthStr')

        if m.get('BgpAsn') is not None:
            self.bgp_asn = m.get('BgpAsn')

        if m.get('BgpCidr') is not None:
            self.bgp_cidr = m.get('BgpCidr')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CenOwnerId') is not None:
            self.cen_owner_id = m.get('CenOwnerId')

        self.cis_router_info = []
        if m.get('CisRouterInfo') is not None:
            for k1 in m.get('CisRouterInfo'):
                temp_model = main_models.GetVccResponseBodyContentCisRouterInfo()
                self.cis_router_info.append(temp_model.from_map(k1))

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CurrentNode') is not None:
            self.current_node = m.get('CurrentNode')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        self.er_infos = []
        if m.get('ErInfos') is not None:
            for k1 in m.get('ErInfos'):
                temp_model = main_models.GetVccResponseBodyContentErInfos()
                self.er_infos.append(temp_model.from_map(k1))

        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('LineOperator') is not None:
            self.line_operator = m.get('LineOperator')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PortType') is not None:
            self.port_type = m.get('PortType')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetVccResponseBodyContentTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        self.vbr_infos = []
        if m.get('VbrInfos') is not None:
            for k1 in m.get('VbrInfos'):
                temp_model = main_models.GetVccResponseBodyContentVbrInfos()
                self.vbr_infos.append(temp_model.from_map(k1))

        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')

        if m.get('VccName') is not None:
            self.vcc_name = m.get('VccName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpdBaseInfo') is not None:
            temp_model = main_models.GetVccResponseBodyContentVpdBaseInfo()
            self.vpd_base_info = temp_model.from_map(m.get('VpdBaseInfo'))

        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class GetVccResponseBodyContentVpdBaseInfo(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        create_time: str = None,
        vpd_id: str = None,
        vpd_name: str = None,
    ):
        # Network address segment
        self.cidr = cidr
        # The time when the data address was created.
        self.create_time = create_time
        # Lingjun CIDR block instance ID
        self.vpd_id = vpd_id
        # Lingjun CIDR block instance name
        self.vpd_name = vpd_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id

        if self.vpd_name is not None:
            result['VpdName'] = self.vpd_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')

        if m.get('VpdName') is not None:
            self.vpd_name = m.get('VpdName')

        return self

class GetVccResponseBodyContentVbrInfos(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        status: str = None,
        vbr_bgp_peers: List[main_models.GetVccResponseBodyContentVbrInfosVbrBgpPeers] = None,
        vbr_id: str = None,
    ):
        # CEN ID
        self.cen_id = cen_id
        # The time when the data address was created.
        self.gmt_create = gmt_create
        # The time when the agent was last modified.
        self.gmt_modified = gmt_modified
        # The status of the VBR. Valid values:
        # 
        # *   unconfirmed
        # *   active: The VPN gateway is in a normal state.
        # *   terminating: The connection is being terminated.
        # *   terminated: The connection is terminated.
        # *   recovering: The task is being recovered.
        # *   deleting: The GDN is being deleted.
        # *   Available: The service is available.
        self.status = status
        # BGP neighbor information list
        self.vbr_bgp_peers = vbr_bgp_peers
        # The ID of the border router.
        self.vbr_id = vbr_id

    def validate(self):
        if self.vbr_bgp_peers:
            for v1 in self.vbr_bgp_peers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.status is not None:
            result['Status'] = self.status

        result['VbrBgpPeers'] = []
        if self.vbr_bgp_peers is not None:
            for k1 in self.vbr_bgp_peers:
                result['VbrBgpPeers'].append(k1.to_map() if k1 else None)

        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.vbr_bgp_peers = []
        if m.get('VbrBgpPeers') is not None:
            for k1 in m.get('VbrBgpPeers'):
                temp_model = main_models.GetVccResponseBodyContentVbrInfosVbrBgpPeers()
                self.vbr_bgp_peers.append(temp_model.from_map(k1))

        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')

        return self

class GetVccResponseBodyContentVbrInfosVbrBgpPeers(DaraModel):
    def __init__(
        self,
        bgp_group_id: str = None,
        bgp_peer_id: str = None,
        peer_asn: str = None,
        peer_ip_address: str = None,
        status: str = None,
    ):
        # BGP Group ID
        self.bgp_group_id = bgp_group_id
        # BGP peer ID
        self.bgp_peer_id = bgp_peer_id
        # Peer AS No.
        self.peer_asn = peer_asn
        # BGP peer IP address
        self.peer_ip_address = peer_ip_address
        # The status of the BGP peer. Valid values:
        # 
        # *   Pending: pending
        # *   Available: The route is available.
        # *   Modifying: being modified
        # *   Deleting: The IPv4 gateway is being deleted.
        # *   Deleted
        # *   Not Available
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bgp_group_id is not None:
            result['BgpGroupId'] = self.bgp_group_id

        if self.bgp_peer_id is not None:
            result['BgpPeerId'] = self.bgp_peer_id

        if self.peer_asn is not None:
            result['PeerAsn'] = self.peer_asn

        if self.peer_ip_address is not None:
            result['PeerIpAddress'] = self.peer_ip_address

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgpGroupId') is not None:
            self.bgp_group_id = m.get('BgpGroupId')

        if m.get('BgpPeerId') is not None:
            self.bgp_peer_id = m.get('BgpPeerId')

        if m.get('PeerAsn') is not None:
            self.peer_asn = m.get('PeerAsn')

        if m.get('PeerIpAddress') is not None:
            self.peer_ip_address = m.get('PeerIpAddress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetVccResponseBodyContentTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        # 
        # You cannot specify an empty string as a tag key. It can be up to 64 characters in length and cannot start with aliyun or acs:. It cannot contain http:// or https://.
        # 
        # You can specify at most 20 tag keys in each call.
        self.tag_key = tag_key
        # The value of the tag that is added to the resource.
        # 
        # The tag value can be empty or a string of up to 128 characters. It cannot start with aliyun or acs:, and cannot contain http:// or https://.
        # 
        # Each key-value pair must be unique. You can specify values for at most 20 tag keys in each call.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class GetVccResponseBodyContentErInfos(DaraModel):
    def __init__(
        self,
        connections: int = None,
        create_time: str = None,
        description: str = None,
        er_id: str = None,
        er_name: str = None,
        gmt_modified: str = None,
        master_zone_id: str = None,
        message: str = None,
        region_id: str = None,
        route_maps: int = None,
        status: str = None,
        tenant_id: str = None,
    ):
        # Connections
        self.connections = connections
        # The time when the data address was created.
        self.create_time = create_time
        # Description
        self.description = description
        # Lingjun HUB ID
        self.er_id = er_id
        # Lingjun HUB Instance Name
        self.er_name = er_name
        # The time when the agent was last modified.
        self.gmt_modified = gmt_modified
        # Primary Zone
        self.master_zone_id = master_zone_id
        # The message that is returned.
        self.message = message
        # Lingjun HUB Region Information
        self.region_id = region_id
        # Number of routing policy
        self.route_maps = route_maps
        # The status of the intervention entry. Valid value:
        self.status = status
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connections is not None:
            result['Connections'] = self.connections

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.er_id is not None:
            result['ErId'] = self.er_id

        if self.er_name is not None:
            result['ErName'] = self.er_name

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id

        if self.message is not None:
            result['Message'] = self.message

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.route_maps is not None:
            result['RouteMaps'] = self.route_maps

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Connections') is not None:
            self.connections = m.get('Connections')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')

        if m.get('ErName') is not None:
            self.er_name = m.get('ErName')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RouteMaps') is not None:
            self.route_maps = m.get('RouteMaps')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

class GetVccResponseBodyContentCisRouterInfo(DaraModel):
    def __init__(
        self,
        cc_infos: List[main_models.GetVccResponseBodyContentCisRouterInfoCcInfos] = None,
        ccr_id: str = None,
    ):
        # Leased Line Information List
        self.cc_infos = cc_infos
        # The ID of the on-cloud router instance.
        self.ccr_id = ccr_id

    def validate(self):
        if self.cc_infos:
            for v1 in self.cc_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CcInfos'] = []
        if self.cc_infos is not None:
            for k1 in self.cc_infos:
                result['CcInfos'].append(k1.to_map() if k1 else None)

        if self.ccr_id is not None:
            result['CcrId'] = self.ccr_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cc_infos = []
        if m.get('CcInfos') is not None:
            for k1 in m.get('CcInfos'):
                temp_model = main_models.GetVccResponseBodyContentCisRouterInfoCcInfos()
                self.cc_infos.append(temp_model.from_map(k1))

        if m.get('CcrId') is not None:
            self.ccr_id = m.get('CcrId')

        return self

class GetVccResponseBodyContentCisRouterInfoCcInfos(DaraModel):
    def __init__(
        self,
        cc_id: str = None,
        local_gateway_ip: str = None,
        remote_gateway_ip: str = None,
        status: str = None,
        subnet_mask: str = None,
        vlan_id: str = None,
    ):
        # Leased Line ID
        self.cc_id = cc_id
        # Lingjun Side Interconnection IPv4 Address
        self.local_gateway_ip = local_gateway_ip
        # Lingjun Side Interconnection IPv4 Address
        self.remote_gateway_ip = remote_gateway_ip
        # The state of the rule.
        self.status = status
        # Subnet mask
        self.subnet_mask = subnet_mask
        # Vlan ID of the leased line
        self.vlan_id = vlan_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cc_id is not None:
            result['CcId'] = self.cc_id

        if self.local_gateway_ip is not None:
            result['LocalGatewayIp'] = self.local_gateway_ip

        if self.remote_gateway_ip is not None:
            result['RemoteGatewayIp'] = self.remote_gateway_ip

        if self.status is not None:
            result['Status'] = self.status

        if self.subnet_mask is not None:
            result['SubnetMask'] = self.subnet_mask

        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CcId') is not None:
            self.cc_id = m.get('CcId')

        if m.get('LocalGatewayIp') is not None:
            self.local_gateway_ip = m.get('LocalGatewayIp')

        if m.get('RemoteGatewayIp') is not None:
            self.remote_gateway_ip = m.get('RemoteGatewayIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubnetMask') is not None:
            self.subnet_mask = m.get('SubnetMask')

        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')

        return self

class GetVccResponseBodyContentAliyunRouterInfo(DaraModel):
    def __init__(
        self,
        local_gateway_ip: str = None,
        mask: str = None,
        pc_id: str = None,
        peer_gateway_ip: str = None,
        vbr_id: str = None,
        vlan_id: str = None,
    ):
        # IPv4 address of Alibaba Cloud-side interconnection
        self.local_gateway_ip = local_gateway_ip
        # Masking
        self.mask = mask
        # Express Connect circuit ID
        self.pc_id = pc_id
        # Lingjun Side Interconnection IPv4 Address
        self.peer_gateway_ip = peer_gateway_ip
        # The ID of the VBR.
        self.vbr_id = vbr_id
        # VLAN ID of the VBR
        self.vlan_id = vlan_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.local_gateway_ip is not None:
            result['LocalGatewayIp'] = self.local_gateway_ip

        if self.mask is not None:
            result['Mask'] = self.mask

        if self.pc_id is not None:
            result['PcId'] = self.pc_id

        if self.peer_gateway_ip is not None:
            result['PeerGatewayIp'] = self.peer_gateway_ip

        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id

        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalGatewayIp') is not None:
            self.local_gateway_ip = m.get('LocalGatewayIp')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        if m.get('PcId') is not None:
            self.pc_id = m.get('PcId')

        if m.get('PeerGatewayIp') is not None:
            self.peer_gateway_ip = m.get('PeerGatewayIp')

        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')

        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')

        return self

