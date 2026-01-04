# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ModifyExpressConnectTrafficQosRequest(DaraModel):
    def __init__(
        self,
        add_instance_list: List[main_models.ModifyExpressConnectTrafficQosRequestAddInstanceList] = None,
        client_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        qos_description: str = None,
        qos_id: str = None,
        qos_name: str = None,
        region_id: str = None,
        remove_instance_list: List[main_models.ModifyExpressConnectTrafficQosRequestRemoveInstanceList] = None,
        resource_owner_account: str = None,
    ):
        # The instances to be added. Ignore this parameter if no instances are to be added.
        self.add_instance_list = add_instance_list
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The description of the QoS policy.
        self.qos_description = qos_description
        # The ID of the QoS policy.
        # 
        # This parameter is required.
        self.qos_id = qos_id
        # The name of the QoS policy.
        self.qos_name = qos_name
        # The region ID of the resource.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The instances to be removed. Ignore this parameter if no instances are to be removed.
        self.remove_instance_list = remove_instance_list
        self.resource_owner_account = resource_owner_account

    def validate(self):
        if self.add_instance_list:
            for v1 in self.add_instance_list:
                 if v1:
                    v1.validate()
        if self.remove_instance_list:
            for v1 in self.remove_instance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddInstanceList'] = []
        if self.add_instance_list is not None:
            for k1 in self.add_instance_list:
                result['AddInstanceList'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.qos_description is not None:
            result['QosDescription'] = self.qos_description

        if self.qos_id is not None:
            result['QosId'] = self.qos_id

        if self.qos_name is not None:
            result['QosName'] = self.qos_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['RemoveInstanceList'] = []
        if self.remove_instance_list is not None:
            for k1 in self.remove_instance_list:
                result['RemoveInstanceList'].append(k1.to_map() if k1 else None)

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.add_instance_list = []
        if m.get('AddInstanceList') is not None:
            for k1 in m.get('AddInstanceList'):
                temp_model = main_models.ModifyExpressConnectTrafficQosRequestAddInstanceList()
                self.add_instance_list.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('QosDescription') is not None:
            self.qos_description = m.get('QosDescription')

        if m.get('QosId') is not None:
            self.qos_id = m.get('QosId')

        if m.get('QosName') is not None:
            self.qos_name = m.get('QosName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.remove_instance_list = []
        if m.get('RemoveInstanceList') is not None:
            for k1 in m.get('RemoveInstanceList'):
                temp_model = main_models.ModifyExpressConnectTrafficQosRequestRemoveInstanceList()
                self.remove_instance_list.append(temp_model.from_map(k1))

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        return self

class ModifyExpressConnectTrafficQosRequestRemoveInstanceList(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
    ):
        # The ID of the associated instance.
        self.instance_id = instance_id
        # The type of the associated instance. Set the value to **PHYSICALCONNECTION**.
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        return self

class ModifyExpressConnectTrafficQosRequestAddInstanceList(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
    ):
        # The ID of the instance to be associated.
        self.instance_id = instance_id
        # The type of instance to be associated. Set the value to **PHYSICALCONNECTION**.
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        return self

