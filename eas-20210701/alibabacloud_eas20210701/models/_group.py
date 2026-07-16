# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class Group(DaraModel):
    def __init__(
        self,
        access_token: str = None,
        caller_uid: str = None,
        cluster_id: str = None,
        create_time: str = None,
        internet_endpoint: str = None,
        intranet_endpoint: str = None,
        labels: List[main_models.GroupLabels] = None,
        name: str = None,
        network: main_models.GroupNetwork = None,
        parent_uid: str = None,
        queue_service: str = None,
        traffic_mode: str = None,
        update_time: str = None,
    ):
        # The access token for the traffic entry of the service group.
        self.access_token = access_token
        self.caller_uid = caller_uid
        # The region in which the service group resides.
        self.cluster_id = cluster_id
        # The time when the service group was created. The time is in UTC.
        self.create_time = create_time
        # The public endpoint of the service group.
        self.internet_endpoint = internet_endpoint
        # The internal endpoint of the service group.
        self.intranet_endpoint = intranet_endpoint
        self.labels = labels
        # The name of the service group.
        self.name = name
        self.network = network
        self.parent_uid = parent_uid
        # The queue services contained in the service group.
        self.queue_service = queue_service
        # The traffic mode.
        self.traffic_mode = traffic_mode
        # The time when the service group was last updated. The time is in UTC.
        self.update_time = update_time

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.network:
            self.network.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token is not None:
            result['AccessToken'] = self.access_token

        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint

        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.network is not None:
            result['Network'] = self.network.to_map()

        if self.parent_uid is not None:
            result['ParentUid'] = self.parent_uid

        if self.queue_service is not None:
            result['QueueService'] = self.queue_service

        if self.traffic_mode is not None:
            result['TrafficMode'] = self.traffic_mode

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')

        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')

        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.GroupLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Network') is not None:
            temp_model = main_models.GroupNetwork()
            self.network = temp_model.from_map(m.get('Network'))

        if m.get('ParentUid') is not None:
            self.parent_uid = m.get('ParentUid')

        if m.get('QueueService') is not None:
            self.queue_service = m.get('QueueService')

        if m.get('TrafficMode') is not None:
            self.traffic_mode = m.get('TrafficMode')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GroupNetwork(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.gateway_id = gateway_id
        self.security_group_id = security_group_id
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self



class GroupLabels(DaraModel):
    def __init__(
        self,
        label_key: str = None,
        label_value: str = None,
    ):
        self.label_key = label_key
        self.label_value = label_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label_key is not None:
            result['LabelKey'] = self.label_key

        if self.label_value is not None:
            result['LabelValue'] = self.label_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelKey') is not None:
            self.label_key = m.get('LabelKey')

        if m.get('LabelValue') is not None:
            self.label_value = m.get('LabelValue')

        return self

