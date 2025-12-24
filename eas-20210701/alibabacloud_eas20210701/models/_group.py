# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Group(DaraModel):
    def __init__(
        self,
        access_token: str = None,
        cluster_id: str = None,
        create_time: str = None,
        internet_endpoint: str = None,
        intranet_endpoint: str = None,
        name: str = None,
        queue_service: str = None,
        traffic_mode: str = None,
        update_time: str = None,
    ):
        self.access_token = access_token
        self.cluster_id = cluster_id
        self.create_time = create_time
        self.internet_endpoint = internet_endpoint
        self.intranet_endpoint = intranet_endpoint
        self.name = name
        self.queue_service = queue_service
        self.traffic_mode = traffic_mode
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token is not None:
            result['AccessToken'] = self.access_token

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint

        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint

        if self.name is not None:
            result['Name'] = self.name

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

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')

        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('QueueService') is not None:
            self.queue_service = m.get('QueueService')

        if m.get('TrafficMode') is not None:
            self.traffic_mode = m.get('TrafficMode')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

