# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstancesWithEcsInfoShrinkRequest(DaraModel):
    def __init__(
        self,
        current: int = None,
        health_status: str = None,
        instance_id: str = None,
        instance_id_name: str = None,
        instance_name: str = None,
        instance_tag_shrink: str = None,
        is_managed: int = None,
        os_name: str = None,
        page_size: int = None,
        private_ip: str = None,
        public_ip: str = None,
        region: str = None,
        resource_group_id: str = None,
        resource_group_id_name: str = None,
        resource_group_name: str = None,
    ):
        self.current = current
        self.health_status = health_status
        self.instance_id = instance_id
        self.instance_id_name = instance_id_name
        self.instance_name = instance_name
        self.instance_tag_shrink = instance_tag_shrink
        self.is_managed = is_managed
        self.os_name = os_name
        self.page_size = page_size
        self.private_ip = private_ip
        self.public_ip = public_ip
        # This parameter is required.
        self.region = region
        self.resource_group_id = resource_group_id
        self.resource_group_id_name = resource_group_id_name
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current is not None:
            result['current'] = self.current

        if self.health_status is not None:
            result['health_status'] = self.health_status

        if self.instance_id is not None:
            result['instance_id'] = self.instance_id

        if self.instance_id_name is not None:
            result['instance_id_name'] = self.instance_id_name

        if self.instance_name is not None:
            result['instance_name'] = self.instance_name

        if self.instance_tag_shrink is not None:
            result['instance_tag'] = self.instance_tag_shrink

        if self.is_managed is not None:
            result['is_managed'] = self.is_managed

        if self.os_name is not None:
            result['os_name'] = self.os_name

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.private_ip is not None:
            result['private_ip'] = self.private_ip

        if self.public_ip is not None:
            result['public_ip'] = self.public_ip

        if self.region is not None:
            result['region'] = self.region

        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id

        if self.resource_group_id_name is not None:
            result['resource_group_id_name'] = self.resource_group_id_name

        if self.resource_group_name is not None:
            result['resource_group_name'] = self.resource_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')

        if m.get('health_status') is not None:
            self.health_status = m.get('health_status')

        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')

        if m.get('instance_id_name') is not None:
            self.instance_id_name = m.get('instance_id_name')

        if m.get('instance_name') is not None:
            self.instance_name = m.get('instance_name')

        if m.get('instance_tag') is not None:
            self.instance_tag_shrink = m.get('instance_tag')

        if m.get('is_managed') is not None:
            self.is_managed = m.get('is_managed')

        if m.get('os_name') is not None:
            self.os_name = m.get('os_name')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('private_ip') is not None:
            self.private_ip = m.get('private_ip')

        if m.get('public_ip') is not None:
            self.public_ip = m.get('public_ip')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')

        if m.get('resource_group_id_name') is not None:
            self.resource_group_id_name = m.get('resource_group_id_name')

        if m.get('resource_group_name') is not None:
            self.resource_group_name = m.get('resource_group_name')

        return self

