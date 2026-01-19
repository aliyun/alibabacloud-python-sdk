# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApiGroupResponseBody(DaraModel):
    def __init__(
        self,
        base_path: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        request_id: str = None,
        sub_domain: str = None,
        tag_status: bool = None,
    ):
        self.base_path = base_path
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.request_id = request_id
        self.sub_domain = sub_domain
        self.tag_status = tag_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_path is not None:
            result['BasePath'] = self.base_path

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain

        if self.tag_status is not None:
            result['TagStatus'] = self.tag_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasePath') is not None:
            self.base_path = m.get('BasePath')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')

        if m.get('TagStatus') is not None:
            self.tag_status = m.get('TagStatus')

        return self

