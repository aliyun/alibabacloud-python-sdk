# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProjectNotifyReceiverRequest(DaraModel):
    def __init__(
        self,
        email: str = None,
        instance_id: str = None,
        name: str = None,
        phone: str = None,
        project_id: int = None,
        region_id: str = None,
    ):
        # The email address of the recipient.
        # > You must specify at least one of the mobile phone number and the email address.
        self.email = email
        # The instance ID of the Bastionhost instance.
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/462953.html) operation to retrieve this parameter.
        self.instance_id = instance_id
        # The name of the recipient. The name must be 1 to 128 characters in length. It cannot start with a special character and can contain only the following special characters: periods (.), underscores (_), hyphens (-), backslashes (\\), and spaces.
        # 
        # This parameter is required.
        self.name = name
        # The mobile phone number of the recipient.
        # > You must specify at least one of the mobile phone number and the email address.
        self.phone = phone
        # The project ID.
        # > You can call the ListProjects operation to retrieve this parameter.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The region ID of the Bastionhost instance.
        # > For the mappings between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

