# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateMonitorGroupByResourceGroupIdRequest(DaraModel):
    def __init__(
        self,
        contact_group_list: List[str] = None,
        enable_install_agent: bool = None,
        enable_subscribe_event: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_group_name: str = None,
    ):
        # The alert contact group. Alert notifications for the application group are sent to the alert contacts in this alert contact group.
        # 
        # An alert contact group is a collection of alert contacts and can contain one or more alert contacts. For more information about how to create alert contacts and alert contact groups, see [PutContact](https://help.aliyun.com/document_detail/114923.html) and [PutContactGroup](https://help.aliyun.com/document_detail/114929.html). For more information about how to obtain alert contact groups, see [DescribeContactGroupList](https://help.aliyun.com/document_detail/114922.html).
        # 
        # This parameter is required.
        self.contact_group_list = contact_group_list
        # Specifies whether to enable automatic installation of the CloudMonitor agent for the application group. CloudMonitor automatically installs the CloudMonitor agent on hosts in the application group. Valid values:
        # 
        # - true: Enabled.
        # 
        # - false: Disabled. Default value.
        self.enable_install_agent = enable_install_agent
        # Specifies whether to enable automatic subscription to event notifications for the application group. When critical or warning events occur on resources in the application group, CloudMonitor sends alert notifications. Valid values:
        # 
        # - true: Enabled.
        # 
        # - false: Disabled. Default value.
        self.enable_subscribe_event = enable_subscribe_event
        # The region ID of the resource group.
        # 
        # For more information about how to obtain the region ID of a resource group, see [GetResourceGroup](https://help.aliyun.com/document_detail/158866.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        # 
        # For more information about how to obtain the resource group ID, see [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html).
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # The name of the resource group.
        # 
        # For more information about how to obtain the resource group name, see [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html).
        # 
        # This parameter is required.
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group_list is not None:
            result['ContactGroupList'] = self.contact_group_list

        if self.enable_install_agent is not None:
            result['EnableInstallAgent'] = self.enable_install_agent

        if self.enable_subscribe_event is not None:
            result['EnableSubscribeEvent'] = self.enable_subscribe_event

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupList') is not None:
            self.contact_group_list = m.get('ContactGroupList')

        if m.get('EnableInstallAgent') is not None:
            self.enable_install_agent = m.get('EnableInstallAgent')

        if m.get('EnableSubscribeEvent') is not None:
            self.enable_subscribe_event = m.get('EnableSubscribeEvent')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        return self

