# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class PutContactGroupRequest(DaraModel):
    def __init__(
        self,
        contact_group_name: str = None,
        contact_names: List[str] = None,
        describe: str = None,
        enable_subscribed: bool = None,
    ):
        # The name of the alert contact group.
        # 
        # For information about how to obtain the name of an alert contact group, see [DescribeContactGroupList](https://help.aliyun.com/document_detail/114922.html).
        # 
        # This parameter is required.
        self.contact_group_name = contact_group_name
        # The name of the alert contact. Valid values of N: 1 to 100.
        self.contact_names = contact_names
        # The description of the alert contact group.
        self.describe = describe
        # Specifies whether to enable the weekly report subscription feature. Valid values:
        # 
        # *   true: The weekly report subscription feature is enabled.
        # *   false: The weekly report subscription feature is disabled.
        # 
        # >  You can enable the weekly report subscription feature only for an Alibaba Cloud account that has at least five Elastic Compute Service (ECS) instances.
        self.enable_subscribed = enable_subscribed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name

        if self.contact_names is not None:
            result['ContactNames'] = self.contact_names

        if self.describe is not None:
            result['Describe'] = self.describe

        if self.enable_subscribed is not None:
            result['EnableSubscribed'] = self.enable_subscribed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')

        if m.get('ContactNames') is not None:
            self.contact_names = m.get('ContactNames')

        if m.get('Describe') is not None:
            self.describe = m.get('Describe')

        if m.get('EnableSubscribed') is not None:
            self.enable_subscribed = m.get('EnableSubscribed')

        return self

