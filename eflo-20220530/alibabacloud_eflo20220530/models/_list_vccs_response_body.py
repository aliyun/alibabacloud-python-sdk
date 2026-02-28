# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class ListVccsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: main_models.ListVccsResponseBodyContent = None,
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
            temp_model = main_models.ListVccsResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListVccsResponseBodyContent(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListVccsResponseBodyContentData] = None,
        total: int = None,
    ):
        # Lingjun Connection Information List
        self.data = data
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListVccsResponseBodyContentData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListVccsResponseBodyContentData(DaraModel):
    def __init__(
        self,
        access_point_id: str = None,
        bandwidth_str: str = None,
        bgp_asn: str = None,
        bgp_cidr: str = None,
        cen_id: str = None,
        cen_owner_id: str = None,
        commodity_code: str = None,
        connection_type: str = None,
        create_time: str = None,
        current_node: str = None,
        er_infos: List[main_models.ListVccsResponseBodyContentDataErInfos] = None,
        expiration_date: str = None,
        gmt_modified: str = None,
        line_operator: str = None,
        message: str = None,
        port_type: str = None,
        rate: float = None,
        region_id: str = None,
        resource_group_id: str = None,
        spec: str = None,
        status: str = None,
        tags: List[main_models.ListVccsResponseBodyContentDataTags] = None,
        task_id: str = None,
        tenant_id: str = None,
        vcc_id: str = None,
        vcc_name: str = None,
        vpc_id: str = None,
        vpd_base_info: main_models.ListVccsResponseBodyContentDataVpdBaseInfo = None,
        vpd_id: str = None,
        zone_id: str = None,
    ):
        # Express Connect circuit access point ID:
        # 
        # *   **ap-cn-wulanchabu-jn-ts-A**: Ulanqab-Jining-A
        # *   **ap-cn-heyuan-yc-ts-SA127**: Heyuan-Yuancheng-A
        self.access_point_id = access_point_id
        # The bandwidth of the port.
        self.bandwidth_str = bandwidth_str
        # bgp as number
        self.bgp_asn = bgp_asn
        # bgp network segment
        self.bgp_cidr = bgp_cidr
        # The ID of the CEN instance; [What is the CEN?](https://help.aliyun.com/document_detail/181681.html)
        # 
        # You can call the [DescribeCens](https://help.aliyun.com/document_detail/468215.htm) to query the information of CEN instances under the current Alibaba Cloud account.
        self.cen_id = cen_id
        # Account to which cen belongs
        self.cen_owner_id = cen_owner_id
        # Commodity code
        self.commodity_code = commodity_code
        # The connection mode. Valid values:
        # 
        # *   **VPC**
        # *   **CENTR**
        self.connection_type = connection_type
        # The time when the data address was created.
        self.create_time = create_time
        # Current process node
        self.current_node = current_node
        # List of bound Lingjun HUB information
        self.er_infos = er_infos
        # The time when the application expired.
        self.expiration_date = expiration_date
        # The time when the cluster was updated.
        self.gmt_modified = gmt_modified
        # The connectivity provider of the Express Connect circuit. Valid values:
        # 
        # *   **CO**: other connectivity providers in the Chinese mainland
        self.line_operator = line_operator
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # The port type of the Express Connect circuit. Valid values:
        # 
        # *   **100GBase-LR**: 100,000 megabytes of single-mode optical port (10 km)
        self.port_type = port_type
        # Process progress; value returns 0 to 1; not started is null
        self.rate = rate
        # The region ID.
        self.region_id = region_id
        # The ID of your Alibaba Cloud resource group.
        # 
        # For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/94475.htm?spm=a2c4g.11186623.0.0.29e15d7akXhpuu).
        self.resource_group_id = resource_group_id
        # The compute specification.
        self.spec = spec
        # The state of the rule.
        self.status = status
        # The tag information.
        # 
        # You can specify up to 20 tags.
        self.tags = tags
        # The job ID.
        self.task_id = task_id
        # The ID of the tenant.
        self.tenant_id = tenant_id
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
        if self.er_infos:
            for v1 in self.er_infos:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
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

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.current_node is not None:
            result['CurrentNode'] = self.current_node

        result['ErInfos'] = []
        if self.er_infos is not None:
            for k1 in self.er_infos:
                result['ErInfos'].append(k1.to_map() if k1 else None)

        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.line_operator is not None:
            result['LineOperator'] = self.line_operator

        if self.message is not None:
            result['Message'] = self.message

        if self.port_type is not None:
            result['PortType'] = self.port_type

        if self.rate is not None:
            result['Rate'] = self.rate

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

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

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

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CurrentNode') is not None:
            self.current_node = m.get('CurrentNode')

        self.er_infos = []
        if m.get('ErInfos') is not None:
            for k1 in m.get('ErInfos'):
                temp_model = main_models.ListVccsResponseBodyContentDataErInfos()
                self.er_infos.append(temp_model.from_map(k1))

        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('LineOperator') is not None:
            self.line_operator = m.get('LineOperator')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PortType') is not None:
            self.port_type = m.get('PortType')

        if m.get('Rate') is not None:
            self.rate = m.get('Rate')

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
                temp_model = main_models.ListVccsResponseBodyContentDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')

        if m.get('VccName') is not None:
            self.vcc_name = m.get('VccName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpdBaseInfo') is not None:
            temp_model = main_models.ListVccsResponseBodyContentDataVpdBaseInfo()
            self.vpd_base_info = temp_model.from_map(m.get('VpdBaseInfo'))

        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ListVccsResponseBodyContentDataVpdBaseInfo(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        create_time: str = None,
        vpd_id: str = None,
        vpd_name: str = None,
    ):
        # The CIDR block of the VPD.
        # 
        # *   We recommend that you use an RFC private endpoint as the Lingjun CIDR block, such as 10.0.0.0/8,172.16.0.0/12,192.168.0.0/16. In scenarios where the Doringjun CIDR block is connected to each other or where the Lingjun CIDR block is connected to a VPC, make sure that the addresses do not conflict with each other.
        # *   You can also use a custom CIDR block other than 100.64.0.0/10, 224.0.0.0/4, 127.0.0.0/8, or 169.254.0.0/16 and their subnets as the primary IPv4 CIDR block of the VPD.
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

class ListVccsResponseBodyContentDataTags(DaraModel):
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

class ListVccsResponseBodyContentDataErInfos(DaraModel):
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
        # Elastic Router ID
        self.er_id = er_id
        # ER instance name
        self.er_name = er_name
        # The time when the agent was last modified.
        self.gmt_modified = gmt_modified
        # Primary Zone
        self.master_zone_id = master_zone_id
        # The message that is returned.
        self.message = message
        # ER region information
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

