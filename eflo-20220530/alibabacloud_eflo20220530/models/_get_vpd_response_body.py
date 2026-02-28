# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class GetVpdResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: main_models.GetVpdResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The data returned.
        self.content = content
        # The additional information that is returned.
        self.message = message
        # The request ID.
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
            temp_model = main_models.GetVpdResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetVpdResponseBodyContent(DaraModel):
    def __init__(
        self,
        attach_er_status: bool = None,
        cidr: str = None,
        create_time: str = None,
        er_infos: List[main_models.GetVpdResponseBodyContentErInfos] = None,
        gmt_modified: str = None,
        message: str = None,
        nc_count: int = None,
        network_interface_count: int = None,
        private_ip_count: int = None,
        quota: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        secondary_cidr_blocks: List[str] = None,
        service_cidr: str = None,
        status: str = None,
        subnet_count: int = None,
        tags: List[main_models.GetVpdResponseBodyContentTags] = None,
        tenant_id: str = None,
        vpd_id: str = None,
        vpd_name: str = None,
    ):
        # Whether the Lingjun HUB(ER) has been bound.
        # 
        # *   **true**: ER is bound.
        # *   **false**: No ER is bound.
        self.attach_er_status = attach_er_status
        # The CIDR block.
        self.cidr = cidr
        # The time when the activation code was created.
        self.create_time = create_time
        # The information of the bound Lingjun HUB(ER).
        self.er_infos = er_infos
        # The time when the O\\&M task was modified.
        self.gmt_modified = gmt_modified
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # The number of NCs.
        self.nc_count = nc_count
        # Number of Lingjun network interface controller.
        self.network_interface_count = network_interface_count
        # The total number of secondary private IP addresses.
        self.private_ip_count = private_ip_count
        # The total quota information.
        self.quota = quota
        # The region ID.
        self.region_id = region_id
        # The ID of your Alibaba Cloud resource group.
        # 
        # For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/94475.htm?spm=a2c4g.11186623.0.0.29e15d7akXhpuu).
        self.resource_group_id = resource_group_id
        # The list of additional CIDR blocks.
        self.secondary_cidr_blocks = secondary_cidr_blocks
        # Internal Service CIDR block.
        self.service_cidr = service_cidr
        # The current state of the instance.
        # 
        # Valid value:
        # 
        # *   Not Available: Not Available.
        # *   Available: Normal: Available: Normal.
        # *   Deleting: Deleting: Deleting: Deleting.
        # *   Executing: executing: Executing: executing.
        self.status = status
        # The number of subnets.
        self.subnet_count = subnet_count
        # The tag information.
        # 
        # You can specify up to 20 tags.
        self.tags = tags
        # The tenant ID.
        self.tenant_id = tenant_id
        # The ID of the VPD instance.
        self.vpd_id = vpd_id
        # The name of the Lingjun CIDR block.
        self.vpd_name = vpd_name

    def validate(self):
        if self.er_infos:
            for v1 in self.er_infos:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_er_status is not None:
            result['AttachErStatus'] = self.attach_er_status

        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['ErInfos'] = []
        if self.er_infos is not None:
            for k1 in self.er_infos:
                result['ErInfos'].append(k1.to_map() if k1 else None)

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.message is not None:
            result['Message'] = self.message

        if self.nc_count is not None:
            result['NcCount'] = self.nc_count

        if self.network_interface_count is not None:
            result['NetworkInterfaceCount'] = self.network_interface_count

        if self.private_ip_count is not None:
            result['PrivateIpCount'] = self.private_ip_count

        if self.quota is not None:
            result['Quota'] = self.quota

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.secondary_cidr_blocks is not None:
            result['SecondaryCidrBlocks'] = self.secondary_cidr_blocks

        if self.service_cidr is not None:
            result['ServiceCidr'] = self.service_cidr

        if self.status is not None:
            result['Status'] = self.status

        if self.subnet_count is not None:
            result['SubnetCount'] = self.subnet_count

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id

        if self.vpd_name is not None:
            result['VpdName'] = self.vpd_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachErStatus') is not None:
            self.attach_er_status = m.get('AttachErStatus')

        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.er_infos = []
        if m.get('ErInfos') is not None:
            for k1 in m.get('ErInfos'):
                temp_model = main_models.GetVpdResponseBodyContentErInfos()
                self.er_infos.append(temp_model.from_map(k1))

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NcCount') is not None:
            self.nc_count = m.get('NcCount')

        if m.get('NetworkInterfaceCount') is not None:
            self.network_interface_count = m.get('NetworkInterfaceCount')

        if m.get('PrivateIpCount') is not None:
            self.private_ip_count = m.get('PrivateIpCount')

        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecondaryCidrBlocks') is not None:
            self.secondary_cidr_blocks = m.get('SecondaryCidrBlocks')

        if m.get('ServiceCidr') is not None:
            self.service_cidr = m.get('ServiceCidr')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubnetCount') is not None:
            self.subnet_count = m.get('SubnetCount')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetVpdResponseBodyContentTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')

        if m.get('VpdName') is not None:
            self.vpd_name = m.get('VpdName')

        return self

class GetVpdResponseBodyContentTags(DaraModel):
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

class GetVpdResponseBodyContentErInfos(DaraModel):
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
        # The number of connections.
        self.connections = connections
        # The time when the activation code was created.
        self.create_time = create_time
        # The description of the synchronization task.
        self.description = description
        # The ID of the Elastic Router (ER) instance.
        self.er_id = er_id
        # Elastic Router (ER) Instance Name
        self.er_name = er_name
        # The time when the O\\&M task was modified.
        self.gmt_modified = gmt_modified
        # The primary zone.
        self.master_zone_id = master_zone_id
        # The returned message.
        self.message = message
        # The ID of the region to which the Elastic Router (ER) belongs.
        self.region_id = region_id
        # The number of routing policy.
        self.route_maps = route_maps
        # The task status.
        self.status = status
        # The tenant ID.
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

