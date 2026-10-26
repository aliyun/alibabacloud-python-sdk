# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyProjectNotifyReceiverRequest(DaraModel):
    def __init__(
        self,
        email: str = None,
        instance_id: str = None,
        name: str = None,
        phone: str = None,
        receiver_id: int = None,
        region_id: str = None,
    ):
        # The new email address of the notification recipient.
        self.email = email
        # The ID of the bastion host instance.
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the bastion host instance ID.
        self.instance_id = instance_id
        # The new name of the notification recipient. The name must be 1 to 128 characters in length, cannot start with a special character, and can contain only the following special characters: periods (.), underscores (_), hyphens (-), backslashes (\\), and spaces.
        # > If this parameter is not specified, the name remains unchanged.
        # 
        # This parameter is required.
        self.name = name
        # The new phone number of the notification recipient.
        self.phone = phone
        # The ID of the notification recipient.
        # > You can call the ListProjectNotifyReceivers operation to query this parameter.
        # 
        # This parameter is required.
        self.receiver_id = receiver_id
        # The region ID of the bastion host.
        # > For the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
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

        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id

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

        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

