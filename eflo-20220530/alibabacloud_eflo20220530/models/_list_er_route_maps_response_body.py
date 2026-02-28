# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class ListErRouteMapsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: main_models.ListErRouteMapsResponseBodyContent = None,
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
            temp_model = main_models.ListErRouteMapsResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListErRouteMapsResponseBodyContent(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListErRouteMapsResponseBodyContentData] = None,
        total: int = None,
    ):
        # routing policy information list
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
                temp_model = main_models.ListErRouteMapsResponseBodyContentData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListErRouteMapsResponseBodyContentData(DaraModel):
    def __init__(
        self,
        action: str = None,
        create_time: str = None,
        description: str = None,
        destination_cidr_block: str = None,
        er_id: str = None,
        er_route_map_id: str = None,
        gmt_modified: str = None,
        message: str = None,
        reception_instance_id: str = None,
        reception_instance_name: str = None,
        reception_instance_owner: str = None,
        reception_instance_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        route_map_num: int = None,
        status: str = None,
        tenant_id: str = None,
        transmission_instance_id: str = None,
        transmission_instance_name: str = None,
        transmission_instance_owner: str = None,
        transmission_instance_type: str = None,
    ):
        # Policy behavior; optional values:
        # 
        # *   **permit**: Allow
        # *   **deny**: Prohibited
        self.action = action
        # The time when the data address was created.
        self.create_time = create_time
        # Policy description
        self.description = description
        # Destination CIDR Block
        self.destination_cidr_block = destination_cidr_block
        # Lingjun HUB ID
        self.er_id = er_id
        # routing policy ID
        self.er_route_map_id = er_route_map_id
        # The time when the agent was last modified.
        self.gmt_modified = gmt_modified
        # The message that is returned.
        self.message = message
        # Receive Instance ID
        self.reception_instance_id = reception_instance_id
        # Receive Instance Name
        self.reception_instance_name = reception_instance_name
        # The tenant to which the receiving instance belongs
        self.reception_instance_owner = reception_instance_owner
        # The type of the received instance. Possible values:
        # 
        # *   **VPD**: Lingjun network segment.
        # *   **VCC**: Lingjun Connection.
        self.reception_instance_type = reception_instance_type
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The ID of the policy.
        # 
        # A smaller sequence number indicates a lower priority. When a route is matched, a policy with a higher priority is preferentially matched.
        # 
        # **Valid values: 1001 to 2000**
        self.route_map_num = route_map_num
        # Status The status of the instance. Valid values:
        # 
        # *   **Available**
        # *   **Not Available**: Unavailable
        # *   **Executing**: Executing
        # *   **Deleting**: The node is being deleted.
        self.status = status
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # Release Instance ID
        self.transmission_instance_id = transmission_instance_id
        # Release Instance Name
        self.transmission_instance_name = transmission_instance_name
        # The tenant to which the published instance belongs
        self.transmission_instance_owner = transmission_instance_owner
        # The type of the published instance. Possible values:
        # 
        # *   **VPD**: Lingjun network segment.
        # *   **VCC**: Lingjun Connection.
        self.transmission_instance_type = transmission_instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.er_id is not None:
            result['ErId'] = self.er_id

        if self.er_route_map_id is not None:
            result['ErRouteMapId'] = self.er_route_map_id

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.message is not None:
            result['Message'] = self.message

        if self.reception_instance_id is not None:
            result['ReceptionInstanceId'] = self.reception_instance_id

        if self.reception_instance_name is not None:
            result['ReceptionInstanceName'] = self.reception_instance_name

        if self.reception_instance_owner is not None:
            result['ReceptionInstanceOwner'] = self.reception_instance_owner

        if self.reception_instance_type is not None:
            result['ReceptionInstanceType'] = self.reception_instance_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.route_map_num is not None:
            result['RouteMapNum'] = self.route_map_num

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.transmission_instance_id is not None:
            result['TransmissionInstanceId'] = self.transmission_instance_id

        if self.transmission_instance_name is not None:
            result['TransmissionInstanceName'] = self.transmission_instance_name

        if self.transmission_instance_owner is not None:
            result['TransmissionInstanceOwner'] = self.transmission_instance_owner

        if self.transmission_instance_type is not None:
            result['TransmissionInstanceType'] = self.transmission_instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')

        if m.get('ErRouteMapId') is not None:
            self.er_route_map_id = m.get('ErRouteMapId')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ReceptionInstanceId') is not None:
            self.reception_instance_id = m.get('ReceptionInstanceId')

        if m.get('ReceptionInstanceName') is not None:
            self.reception_instance_name = m.get('ReceptionInstanceName')

        if m.get('ReceptionInstanceOwner') is not None:
            self.reception_instance_owner = m.get('ReceptionInstanceOwner')

        if m.get('ReceptionInstanceType') is not None:
            self.reception_instance_type = m.get('ReceptionInstanceType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RouteMapNum') is not None:
            self.route_map_num = m.get('RouteMapNum')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TransmissionInstanceId') is not None:
            self.transmission_instance_id = m.get('TransmissionInstanceId')

        if m.get('TransmissionInstanceName') is not None:
            self.transmission_instance_name = m.get('TransmissionInstanceName')

        if m.get('TransmissionInstanceOwner') is not None:
            self.transmission_instance_owner = m.get('TransmissionInstanceOwner')

        if m.get('TransmissionInstanceType') is not None:
            self.transmission_instance_type = m.get('TransmissionInstanceType')

        return self

