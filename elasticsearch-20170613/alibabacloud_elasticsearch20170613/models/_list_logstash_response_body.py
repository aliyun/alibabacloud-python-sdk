# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListLogstashResponseBody(DaraModel):
    def __init__(
        self,
        headers: main_models.ListLogstashResponseBodyHeaders = None,
        request_id: str = None,
        result: List[main_models.ListLogstashResponseBodyResult] = None,
    ):
        # The billing method of the instance. Supported: prepaid (subscription) and postpaid (pay-as-you-go).
        self.headers = headers
        # Detailed information about the matching instances.
        self.request_id = request_id
        # The name of the VPC.
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = main_models.ListLogstashResponseBodyHeaders()
            self.headers = temp_model.from_map(m.get('Headers'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListLogstashResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListLogstashResponseBodyResult(DaraModel):
    def __init__(
        self,
        tags: List[main_models.ListLogstashResponseBodyResultTags] = None,
        created_at: str = None,
        description: str = None,
        instance_id: str = None,
        network_config: main_models.ListLogstashResponseBodyResultNetworkConfig = None,
        node_amount: int = None,
        node_spec: main_models.ListLogstashResponseBodyResultNodeSpec = None,
        payment_type: str = None,
        resource_group_id: str = None,
        status: str = None,
        updated_at: str = None,
        version: str = None,
    ):
        # The configuration information of the data node.
        self.tags = tags
        # The ID of the instance.
        self.created_at = created_at
        # The time when the instance was last updated.
        self.description = description
        # The tag value of the cloud disk.
        self.instance_id = instance_id
        # The network type. Currently, only Virtual Private Cloud (VPC) is supported.
        self.network_config = network_config
        # The state of the instance. Valid values: Normal, Active, Inactive, and Invalid.
        self.node_amount = node_amount
        # Specifies whether to use disk encryption. Valid values:
        # 
        # *   true: Enables the concurrent query feature for queries other than aggregate queries.
        # *   false: Disables the concurrent query feature for queries other than aggregate queries.
        self.node_spec = node_spec
        # The time when the instance was created.
        self.payment_type = payment_type
        self.resource_group_id = resource_group_id
        # The version of the instance. Currently, only 6.7.0_with_X-Pack and 7.4.0_with_X-Pack are supported.
        self.status = status
        # The tag of the instance. Valid values:
        self.updated_at = updated_at
        # The tag key of the cloud disk.
        self.version = version

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.network_config:
            self.network_config.validate()
        if self.node_spec:
            self.node_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()

        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount

        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['status'] = self.status

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListLogstashResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('networkConfig') is not None:
            temp_model = main_models.ListLogstashResponseBodyResultNetworkConfig()
            self.network_config = temp_model.from_map(m.get('networkConfig'))

        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')

        if m.get('nodeSpec') is not None:
            temp_model = main_models.ListLogstashResponseBodyResultNodeSpec()
            self.node_spec = temp_model.from_map(m.get('nodeSpec'))

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class ListLogstashResponseBodyResultNodeSpec(DaraModel):
    def __init__(
        self,
        disk: int = None,
        disk_encryption: bool = None,
        disk_type: str = None,
        spec: str = None,
    ):
        # The network configurations.
        self.disk = disk
        # The ID of the VPC.
        self.disk_encryption = disk_encryption
        # The zone where the cluster resides.
        self.disk_type = disk_type
        # The type of the disk.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk is not None:
            result['disk'] = self.disk

        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption

        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.spec is not None:
            result['spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disk') is not None:
            self.disk = m.get('disk')

        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')

        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        return self

class ListLogstashResponseBodyResultNetworkConfig(DaraModel):
    def __init__(
        self,
        type: str = None,
        vpc_id: str = None,
        vs_area: str = None,
        vswitch_id: str = None,
    ):
        self.type = type
        # The ID of the vSwitch.
        self.vpc_id = vpc_id
        self.vs_area = vs_area
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        if self.vs_area is not None:
            result['vsArea'] = self.vs_area

        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')

        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')

        return self

class ListLogstashResponseBodyResultTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The disk size of the node.
        self.tag_key = tag_key
        # The instance type of the ECS instance.
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

class ListLogstashResponseBodyHeaders(DaraModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        # The number of data nodes.
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')

        return self

