# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribeClustersResponse(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[main_models.DescribeClustersResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['headers'] = self.headers

        if self.status_code is not None:
            result['statusCode'] = self.status_code

        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')

        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.DescribeClustersResponseBody()
                self.body.append(temp_model.from_map(k1))

        return self

class DescribeClustersResponseBody(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_type: str = None,
        created: str = None,
        current_version: str = None,
        data_disk_category: str = None,
        data_disk_size: int = None,
        deletion_protection: bool = None,
        docker_version: str = None,
        external_loadbalancer_id: str = None,
        init_version: str = None,
        master_url: str = None,
        meta_data: str = None,
        name: str = None,
        network_mode: str = None,
        private_zone: bool = None,
        profile: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        size: int = None,
        state: str = None,
        subnet_cidr: str = None,
        tags: List[main_models.DescribeClustersResponseBodyTags] = None,
        updated: str = None,
        vpc_id: str = None,
        vswitch_cidr: str = None,
        vswitch_id: str = None,
        worker_ram_role_name: str = None,
        zone_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_type = cluster_type
        self.created = created
        self.current_version = current_version
        self.data_disk_category = data_disk_category
        self.data_disk_size = data_disk_size
        self.deletion_protection = deletion_protection
        self.docker_version = docker_version
        self.external_loadbalancer_id = external_loadbalancer_id
        self.init_version = init_version
        self.master_url = master_url
        self.meta_data = meta_data
        self.name = name
        self.network_mode = network_mode
        self.private_zone = private_zone
        self.profile = profile
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.security_group_id = security_group_id
        self.size = size
        self.state = state
        self.subnet_cidr = subnet_cidr
        self.tags = tags
        self.updated = updated
        self.vpc_id = vpc_id
        self.vswitch_cidr = vswitch_cidr
        self.vswitch_id = vswitch_id
        self.worker_ram_role_name = worker_ram_role_name
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type

        if self.created is not None:
            result['created'] = self.created

        if self.current_version is not None:
            result['current_version'] = self.current_version

        if self.data_disk_category is not None:
            result['data_disk_category'] = self.data_disk_category

        if self.data_disk_size is not None:
            result['data_disk_size'] = self.data_disk_size

        if self.deletion_protection is not None:
            result['deletion_protection'] = self.deletion_protection

        if self.docker_version is not None:
            result['docker_version'] = self.docker_version

        if self.external_loadbalancer_id is not None:
            result['external_loadbalancer_id'] = self.external_loadbalancer_id

        if self.init_version is not None:
            result['init_version'] = self.init_version

        if self.master_url is not None:
            result['master_url'] = self.master_url

        if self.meta_data is not None:
            result['meta_data'] = self.meta_data

        if self.name is not None:
            result['name'] = self.name

        if self.network_mode is not None:
            result['network_mode'] = self.network_mode

        if self.private_zone is not None:
            result['private_zone'] = self.private_zone

        if self.profile is not None:
            result['profile'] = self.profile

        if self.region_id is not None:
            result['region_id'] = self.region_id

        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id

        if self.security_group_id is not None:
            result['security_group_id'] = self.security_group_id

        if self.size is not None:
            result['size'] = self.size

        if self.state is not None:
            result['state'] = self.state

        if self.subnet_cidr is not None:
            result['subnet_cidr'] = self.subnet_cidr

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.updated is not None:
            result['updated'] = self.updated

        if self.vpc_id is not None:
            result['vpc_id'] = self.vpc_id

        if self.vswitch_cidr is not None:
            result['vswitch_cidr'] = self.vswitch_cidr

        if self.vswitch_id is not None:
            result['vswitch_id'] = self.vswitch_id

        if self.worker_ram_role_name is not None:
            result['worker_ram_role_name'] = self.worker_ram_role_name

        if self.zone_id is not None:
            result['zone_id'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('current_version') is not None:
            self.current_version = m.get('current_version')

        if m.get('data_disk_category') is not None:
            self.data_disk_category = m.get('data_disk_category')

        if m.get('data_disk_size') is not None:
            self.data_disk_size = m.get('data_disk_size')

        if m.get('deletion_protection') is not None:
            self.deletion_protection = m.get('deletion_protection')

        if m.get('docker_version') is not None:
            self.docker_version = m.get('docker_version')

        if m.get('external_loadbalancer_id') is not None:
            self.external_loadbalancer_id = m.get('external_loadbalancer_id')

        if m.get('init_version') is not None:
            self.init_version = m.get('init_version')

        if m.get('master_url') is not None:
            self.master_url = m.get('master_url')

        if m.get('meta_data') is not None:
            self.meta_data = m.get('meta_data')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('network_mode') is not None:
            self.network_mode = m.get('network_mode')

        if m.get('private_zone') is not None:
            self.private_zone = m.get('private_zone')

        if m.get('profile') is not None:
            self.profile = m.get('profile')

        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')

        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')

        if m.get('security_group_id') is not None:
            self.security_group_id = m.get('security_group_id')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('subnet_cidr') is not None:
            self.subnet_cidr = m.get('subnet_cidr')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.DescribeClustersResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        if m.get('vpc_id') is not None:
            self.vpc_id = m.get('vpc_id')

        if m.get('vswitch_cidr') is not None:
            self.vswitch_cidr = m.get('vswitch_cidr')

        if m.get('vswitch_id') is not None:
            self.vswitch_id = m.get('vswitch_id')

        if m.get('worker_ram_role_name') is not None:
            self.worker_ram_role_name = m.get('worker_ram_role_name')

        if m.get('zone_id') is not None:
            self.zone_id = m.get('zone_id')

        return self

class DescribeClustersResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

