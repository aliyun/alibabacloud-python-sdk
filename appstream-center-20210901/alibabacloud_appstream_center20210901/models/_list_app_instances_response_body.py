# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListAppInstancesResponseBody(DaraModel):
    def __init__(
        self,
        app_instance_models: List[main_models.ListAppInstancesResponseBodyAppInstanceModels] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The app instances.
        self.app_instance_models = app_instance_models
        # The page number of the returned page. We recommend that you configure this parameter.
        self.page_number = page_number
        # The number of entries returned on each page. The value cannot be greater than `100`. We recommend that you configure this parameter.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.app_instance_models:
            for v1 in self.app_instance_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppInstanceModels'] = []
        if self.app_instance_models is not None:
            for k1 in self.app_instance_models:
                result['AppInstanceModels'].append(k1.to_map() if k1 else None)

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
        self.app_instance_models = []
        if m.get('AppInstanceModels') is not None:
            for k1 in m.get('AppInstanceModels'):
                temp_model = main_models.ListAppInstancesResponseBodyAppInstanceModels()
                self.app_instance_models.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAppInstancesResponseBodyAppInstanceModels(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        bind_info: main_models.ListAppInstancesResponseBodyAppInstanceModelsBindInfo = None,
        charge_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        main_eth_public_ip: str = None,
        network_interface_id: str = None,
        network_interface_ip: str = None,
        node_id: str = None,
        session_status: str = None,
        status: str = None,
    ):
        # The ID of the delivery group.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the application instance.
        self.app_instance_id = app_instance_id
        # The information about the binding between the application instance and end users.
        self.bind_info = bind_info
        # The billing method of the app instance. Valid values:
        # 
        # *   **PrePaid**: subscription.
        # *   **PostPaid**: pay-as-you-go
        # 
        # >  This parameter is returned only if the ChargeResourceMode parameter of the delivery group to which the app instance belongs is set to Node.
        self.charge_type = charge_type
        # The time when the application instance was created.
        self.gmt_create = gmt_create
        # The time when the application instance was updated.
        self.gmt_modified = gmt_modified
        # The public IP address associated with the primary NIC. This value is returned only if `StrategyType` is set to `Mixed`.
        self.main_eth_public_ip = main_eth_public_ip
        self.network_interface_id = network_interface_id
        self.network_interface_ip = network_interface_ip
        # The ID of the node on which the app instance runs.
        # 
        # >  This parameter is returned only if the ChargeResourceMode parameter of the delivery group to which the app instance belongs is set to Node.
        self.node_id = node_id
        # The session status. This parameter is returned only if the application instance is in the `RUNNING` state.
        # 
        # Valid values:
        # 
        # *   disconnect: disconnected
        # *   connect: connected
        self.session_status = session_status
        # The status of the application instance.
        self.status = status

    def validate(self):
        if self.bind_info:
            self.bind_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id

        if self.bind_info is not None:
            result['BindInfo'] = self.bind_info.to_map()

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.main_eth_public_ip is not None:
            result['MainEthPublicIp'] = self.main_eth_public_ip

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.network_interface_ip is not None:
            result['NetworkInterfaceIp'] = self.network_interface_ip

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.session_status is not None:
            result['SessionStatus'] = self.session_status

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')

        if m.get('BindInfo') is not None:
            temp_model = main_models.ListAppInstancesResponseBodyAppInstanceModelsBindInfo()
            self.bind_info = temp_model.from_map(m.get('BindInfo'))

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('MainEthPublicIp') is not None:
            self.main_eth_public_ip = m.get('MainEthPublicIp')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('NetworkInterfaceIp') is not None:
            self.network_interface_ip = m.get('NetworkInterfaceIp')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('SessionStatus') is not None:
            self.session_status = m.get('SessionStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListAppInstancesResponseBodyAppInstanceModelsBindInfo(DaraModel):
    def __init__(
        self,
        end_user_id: str = None,
        usage_duration: int = None,
    ):
        # The ID of the end user that is bound to the application instance.
        self.end_user_id = end_user_id
        # The use duration of the application instance. Unit: seconds.
        self.usage_duration = usage_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.usage_duration is not None:
            result['UsageDuration'] = self.usage_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('UsageDuration') is not None:
            self.usage_duration = m.get('UsageDuration')

        return self

