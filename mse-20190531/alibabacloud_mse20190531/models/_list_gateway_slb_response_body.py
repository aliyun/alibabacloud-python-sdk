# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListGatewaySlbResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListGatewaySlbResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned.
        self.code = code
        # The data entries returned.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListGatewaySlbResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListGatewaySlbResponseBodyData(DaraModel):
    def __init__(
        self,
        edit_enable: bool = None,
        gateway_id: str = None,
        gateway_slb_mode: str = None,
        gateway_slb_status: str = None,
        gmt_create: str = None,
        http_port: int = None,
        https_port: int = None,
        https_vserver_group_id: str = None,
        id: str = None,
        service_weight: int = None,
        slb_id: str = None,
        slb_ip: str = None,
        slb_port: str = None,
        slb_type: str = None,
        status_desc: str = None,
        type: str = None,
        vserver_group_id: str = None,
        vservice_list: List[main_models.ListGatewaySlbResponseBodyDataVServiceList] = None,
        vs_meta_info: str = None,
    ):
        # Indicates whether the edit operation is supported.
        self.edit_enable = edit_enable
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # The mode of the SLB instance.
        self.gateway_slb_mode = gateway_slb_mode
        # The association status.
        self.gateway_slb_status = gateway_slb_status
        # The creation time.
        self.gmt_create = gmt_create
        # The port number of the HTTP virtual service group.
        self.http_port = http_port
        # The port number of the HTTPS virtual service group.
        self.https_port = https_port
        # The ID of the HTTPS virtual service group.
        self.https_vserver_group_id = https_vserver_group_id
        # The ID.
        self.id = id
        # The service weight.
        self.service_weight = service_weight
        # The ID of the SLB instance.
        self.slb_id = slb_id
        # The IP address of the SLB instance.
        self.slb_ip = slb_ip
        # The port number of the SLB instance.
        self.slb_port = slb_port
        self.slb_type = slb_type
        # The description of the status.
        self.status_desc = status_desc
        # The type.
        self.type = type
        # The ID of the HTTP virtual service group.
        self.vserver_group_id = vserver_group_id
        self.vservice_list = vservice_list
        self.vs_meta_info = vs_meta_info

    def validate(self):
        if self.vservice_list:
            for v1 in self.vservice_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edit_enable is not None:
            result['EditEnable'] = self.edit_enable

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_slb_mode is not None:
            result['GatewaySlbMode'] = self.gateway_slb_mode

        if self.gateway_slb_status is not None:
            result['GatewaySlbStatus'] = self.gateway_slb_status

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.http_port is not None:
            result['HttpPort'] = self.http_port

        if self.https_port is not None:
            result['HttpsPort'] = self.https_port

        if self.https_vserver_group_id is not None:
            result['HttpsVServerGroupId'] = self.https_vserver_group_id

        if self.id is not None:
            result['Id'] = self.id

        if self.service_weight is not None:
            result['ServiceWeight'] = self.service_weight

        if self.slb_id is not None:
            result['SlbId'] = self.slb_id

        if self.slb_ip is not None:
            result['SlbIp'] = self.slb_ip

        if self.slb_port is not None:
            result['SlbPort'] = self.slb_port

        if self.slb_type is not None:
            result['SlbType'] = self.slb_type

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        if self.type is not None:
            result['Type'] = self.type

        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id

        result['VServiceList'] = []
        if self.vservice_list is not None:
            for k1 in self.vservice_list:
                result['VServiceList'].append(k1.to_map() if k1 else None)

        if self.vs_meta_info is not None:
            result['VsMetaInfo'] = self.vs_meta_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EditEnable') is not None:
            self.edit_enable = m.get('EditEnable')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewaySlbMode') is not None:
            self.gateway_slb_mode = m.get('GatewaySlbMode')

        if m.get('GatewaySlbStatus') is not None:
            self.gateway_slb_status = m.get('GatewaySlbStatus')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('HttpPort') is not None:
            self.http_port = m.get('HttpPort')

        if m.get('HttpsPort') is not None:
            self.https_port = m.get('HttpsPort')

        if m.get('HttpsVServerGroupId') is not None:
            self.https_vserver_group_id = m.get('HttpsVServerGroupId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ServiceWeight') is not None:
            self.service_weight = m.get('ServiceWeight')

        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')

        if m.get('SlbIp') is not None:
            self.slb_ip = m.get('SlbIp')

        if m.get('SlbPort') is not None:
            self.slb_port = m.get('SlbPort')

        if m.get('SlbType') is not None:
            self.slb_type = m.get('SlbType')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        self.vservice_list = []
        if m.get('VServiceList') is not None:
            for k1 in m.get('VServiceList'):
                temp_model = main_models.ListGatewaySlbResponseBodyDataVServiceList()
                self.vservice_list.append(temp_model.from_map(k1))

        if m.get('VsMetaInfo') is not None:
            self.vs_meta_info = m.get('VsMetaInfo')

        return self

class ListGatewaySlbResponseBodyDataVServiceList(DaraModel):
    def __init__(
        self,
        port: str = None,
        protocol: str = None,
        vserver_group_id: str = None,
        vserver_group_name: str = None,
    ):
        self.port = port
        self.protocol = protocol
        self.vserver_group_id = vserver_group_id
        self.vserver_group_name = vserver_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id

        if self.vserver_group_name is not None:
            result['VServerGroupName'] = self.vserver_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        if m.get('VServerGroupName') is not None:
            self.vserver_group_name = m.get('VServerGroupName')

        return self

