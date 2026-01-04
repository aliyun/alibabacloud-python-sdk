# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeExpressConnectTrafficQosResponseBody(DaraModel):
    def __init__(
        self,
        count: str = None,
        max_results: int = None,
        next_token: str = None,
        qos_list: List[main_models.DescribeExpressConnectTrafficQosResponseBodyQosList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The total number of entries returned.
        self.count = count
        # The number of entries per page. Valid values: **1 to 100**. Default value: 20.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value is returned for **NextToken**, the value can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The information about QoS policies.
        self.qos_list = qos_list
        # The request ID.
        self.request_id = request_id
        # The number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.qos_list:
            for v1 in self.qos_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['QosList'] = []
        if self.qos_list is not None:
            for k1 in self.qos_list:
                result['QosList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.qos_list = []
        if m.get('QosList') is not None:
            for k1 in m.get('QosList'):
                temp_model = main_models.DescribeExpressConnectTrafficQosResponseBodyQosList()
                self.qos_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeExpressConnectTrafficQosResponseBodyQosList(DaraModel):
    def __init__(
        self,
        associated_instance_list: List[main_models.DescribeExpressConnectTrafficQosResponseBodyQosListAssociatedInstanceList] = None,
        progressing: int = None,
        qos_description: str = None,
        qos_id: str = None,
        qos_name: str = None,
        queue_list: List[main_models.DescribeExpressConnectTrafficQosResponseBodyQosListQueueList] = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.DescribeExpressConnectTrafficQosResponseBodyQosListTags] = None,
    ):
        # The information about the instances to which the QoS policy is associated.
        self.associated_instance_list = associated_instance_list
        # The configuration progress of the QoS policy. Valid values: **0** to **100**.
        self.progressing = progressing
        # The description of the QoS policy.
        # 
        # The description can be up to 256 characters in length. It cannot start with `http://` or `https://`.
        self.qos_description = qos_description
        # The ID of the QoS policy.
        self.qos_id = qos_id
        # The name of the QoS policy.
        # 
        # The name can be up to 128 characters in length and cannot start with `http://` or `https://`.
        self.qos_name = qos_name
        # The information about the QoS queues.
        self.queue_list = queue_list
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The state of the QoS policy. Valid values:
        # 
        # - **Normal**: The QoS policy is available.
        # - **Configuring**: The QoS policy is being configured.
        # 
        #  > If a QoS policy is in the Configuring state, you cannot perform most of the operations to create, update, or delete QoS policies, QoS queues, or QoS rules.
        self.status = status
        # The tag list.
        self.tags = tags

    def validate(self):
        if self.associated_instance_list:
            for v1 in self.associated_instance_list:
                 if v1:
                    v1.validate()
        if self.queue_list:
            for v1 in self.queue_list:
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
        result['AssociatedInstanceList'] = []
        if self.associated_instance_list is not None:
            for k1 in self.associated_instance_list:
                result['AssociatedInstanceList'].append(k1.to_map() if k1 else None)

        if self.progressing is not None:
            result['Progressing'] = self.progressing

        if self.qos_description is not None:
            result['QosDescription'] = self.qos_description

        if self.qos_id is not None:
            result['QosId'] = self.qos_id

        if self.qos_name is not None:
            result['QosName'] = self.qos_name

        result['QueueList'] = []
        if self.queue_list is not None:
            for k1 in self.queue_list:
                result['QueueList'].append(k1.to_map() if k1 else None)

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.associated_instance_list = []
        if m.get('AssociatedInstanceList') is not None:
            for k1 in m.get('AssociatedInstanceList'):
                temp_model = main_models.DescribeExpressConnectTrafficQosResponseBodyQosListAssociatedInstanceList()
                self.associated_instance_list.append(temp_model.from_map(k1))

        if m.get('Progressing') is not None:
            self.progressing = m.get('Progressing')

        if m.get('QosDescription') is not None:
            self.qos_description = m.get('QosDescription')

        if m.get('QosId') is not None:
            self.qos_id = m.get('QosId')

        if m.get('QosName') is not None:
            self.qos_name = m.get('QosName')

        self.queue_list = []
        if m.get('QueueList') is not None:
            for k1 in m.get('QueueList'):
                temp_model = main_models.DescribeExpressConnectTrafficQosResponseBodyQosListQueueList()
                self.queue_list.append(temp_model.from_map(k1))

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeExpressConnectTrafficQosResponseBodyQosListTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeExpressConnectTrafficQosResponseBodyQosListTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeExpressConnectTrafficQosResponseBodyQosListQueueList(DaraModel):
    def __init__(
        self,
        bandwidth_percent: str = None,
        qos_id: str = None,
        queue_description: str = None,
        queue_id: str = None,
        queue_name: str = None,
        queue_type: str = None,
        status: str = None,
    ):
        # The percentage of bandwidth allocated to a QoS queue.
        # 
        # - If QueueType is set to **Medium**, this parameter is required. Valid values: **1** to **100**.
        # - If QueueType is set to **Default**, a value of - is returned.
        self.bandwidth_percent = bandwidth_percent
        # The ID of the QoS policy.
        self.qos_id = qos_id
        # The description of the QoS queue.
        # 
        # The description can be up to **256** characters in length. It cannot start with `http://` or `https://`.
        self.queue_description = queue_description
        # The ID of the QoS queue.
        self.queue_id = queue_id
        # The name of the QoS queue.
        # 
        # The name can be up to **128** characters in length and cannot start with `http://` or `https://`.
        self.queue_name = queue_name
        # The type of the QoS queue. Valid values:
        # 
        # - **High**: high-priority queue.
        # - **Medium**: standard queue.
        # - **Default**: default queue.
        # 
        # 
        # > You cannot create a default queue.
        self.queue_type = queue_type
        # The state of the QoS queue. Valid values:
        # 
        # - **Normal**: The QoS queue is available.
        # - **Configuring**: The QoS queue is being configured.
        # - **Deleting**: The QoS queue is being deleted.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_percent is not None:
            result['BandwidthPercent'] = self.bandwidth_percent

        if self.qos_id is not None:
            result['QosId'] = self.qos_id

        if self.queue_description is not None:
            result['QueueDescription'] = self.queue_description

        if self.queue_id is not None:
            result['QueueId'] = self.queue_id

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.queue_type is not None:
            result['QueueType'] = self.queue_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPercent') is not None:
            self.bandwidth_percent = m.get('BandwidthPercent')

        if m.get('QosId') is not None:
            self.qos_id = m.get('QosId')

        if m.get('QueueDescription') is not None:
            self.queue_description = m.get('QueueDescription')

        if m.get('QueueId') is not None:
            self.queue_id = m.get('QueueId')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('QueueType') is not None:
            self.queue_type = m.get('QueueType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeExpressConnectTrafficQosResponseBodyQosListAssociatedInstanceList(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_progressing: int = None,
        instance_status: str = None,
        instance_type: str = None,
    ):
        # The ID of the instance to which the QoS policy is associated.
        self.instance_id = instance_id
        # The configuration progress of the instance to which the QoS policy is associated. Valid values: **0** to **100**.
        self.instance_progressing = instance_progressing
        # The state of the instance to which the QoS policy is associated. Valid values:
        # 
        # - **Normal**: The instance is available.
        # - **Configuring**: The instance is being configured.
        # - **Deleting**: The instance is being deleted.
        self.instance_status = instance_status
        # The type of the instance to which the QoS policy is associated. Only **PHYSICALCONNECTION** is returned.
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

        if self.instance_progressing is not None:
            result['InstanceProgressing'] = self.instance_progressing

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceProgressing') is not None:
            self.instance_progressing = m.get('InstanceProgressing')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        return self

