# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListKyuubiServicesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListKyuubiServicesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListKyuubiServicesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListKyuubiServicesResponseBodyData(DaraModel):
    def __init__(
        self,
        kyuubi_services: List[main_models.ListKyuubiServicesResponseBodyDataKyuubiServices] = None,
    ):
        self.kyuubi_services = kyuubi_services

    def validate(self):
        if self.kyuubi_services:
            for v1 in self.kyuubi_services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['kyuubiServices'] = []
        if self.kyuubi_services is not None:
            for k1 in self.kyuubi_services:
                result['kyuubiServices'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kyuubi_services = []
        if m.get('kyuubiServices') is not None:
            for k1 in m.get('kyuubiServices'):
                temp_model = main_models.ListKyuubiServicesResponseBodyDataKyuubiServices()
                self.kyuubi_services.append(temp_model.from_map(k1))

        return self

class ListKyuubiServicesResponseBodyDataKyuubiServices(DaraModel):
    def __init__(
        self,
        compute_instance: str = None,
        create_time: str = None,
        creator: str = None,
        inner_endpoint: str = None,
        kyuubi_configs: str = None,
        kyuubi_release_version: str = None,
        kyuubi_service_id: str = None,
        name: str = None,
        public_endpoint: str = None,
        queue: str = None,
        release_version: str = None,
        replica: int = None,
        spark_configs: str = None,
        start_time: str = None,
        state: str = None,
    ):
        self.compute_instance = compute_instance
        self.create_time = create_time
        self.creator = creator
        self.inner_endpoint = inner_endpoint
        self.kyuubi_configs = kyuubi_configs
        self.kyuubi_release_version = kyuubi_release_version
        # KyuubiServer ID。
        self.kyuubi_service_id = kyuubi_service_id
        self.name = name
        self.public_endpoint = public_endpoint
        self.queue = queue
        self.release_version = release_version
        self.replica = replica
        self.spark_configs = spark_configs
        self.start_time = start_time
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_instance is not None:
            result['computeInstance'] = self.compute_instance

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.creator is not None:
            result['creator'] = self.creator

        if self.inner_endpoint is not None:
            result['innerEndpoint'] = self.inner_endpoint

        if self.kyuubi_configs is not None:
            result['kyuubiConfigs'] = self.kyuubi_configs

        if self.kyuubi_release_version is not None:
            result['kyuubiReleaseVersion'] = self.kyuubi_release_version

        if self.kyuubi_service_id is not None:
            result['kyuubiServiceId'] = self.kyuubi_service_id

        if self.name is not None:
            result['name'] = self.name

        if self.public_endpoint is not None:
            result['publicEndpoint'] = self.public_endpoint

        if self.queue is not None:
            result['queue'] = self.queue

        if self.release_version is not None:
            result['releaseVersion'] = self.release_version

        if self.replica is not None:
            result['replica'] = self.replica

        if self.spark_configs is not None:
            result['sparkConfigs'] = self.spark_configs

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.state is not None:
            result['state'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeInstance') is not None:
            self.compute_instance = m.get('computeInstance')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('innerEndpoint') is not None:
            self.inner_endpoint = m.get('innerEndpoint')

        if m.get('kyuubiConfigs') is not None:
            self.kyuubi_configs = m.get('kyuubiConfigs')

        if m.get('kyuubiReleaseVersion') is not None:
            self.kyuubi_release_version = m.get('kyuubiReleaseVersion')

        if m.get('kyuubiServiceId') is not None:
            self.kyuubi_service_id = m.get('kyuubiServiceId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('publicEndpoint') is not None:
            self.public_endpoint = m.get('publicEndpoint')

        if m.get('queue') is not None:
            self.queue = m.get('queue')

        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')

        if m.get('replica') is not None:
            self.replica = m.get('replica')

        if m.get('sparkConfigs') is not None:
            self.spark_configs = m.get('sparkConfigs')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('state') is not None:
            self.state = m.get('state')

        return self

