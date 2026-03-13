# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RunNotifyComponentWithMessageCenterRequest(DaraModel):
    def __init__(
        self,
        action_name: str = None,
        aliuid: str = None,
        asset_id: str = None,
        channel_type_list: List[str] = None,
        component_name: str = None,
        event_id: str = None,
        lang: str = None,
        node_name: str = None,
        params: str = None,
        playbook_uuid: str = None,
        role_for: int = None,
        role_type: str = None,
    ):
        # The action name of the playbook.
        # 
        # This parameter is required.
        self.action_name = action_name
        # The user ID receiving the message.
        # 
        # This parameter is required.
        self.aliuid = aliuid
        # Resource instance ID. This parameter is currently deprecated and no longer in use.
        self.asset_id = asset_id
        # Collection of channel types. If not provided, all channels will be used by default, and it is not required to provide this parameter by default.
        self.channel_type_list = channel_type_list
        # The component name of the playbook.
        # 
        # This parameter is required.
        self.component_name = component_name
        # Cloud Pigeon\\"s message event ID. Values:
        # - yundun_soar_incident_generate: Incident generation.
        # - yundun_soar_alert_generate: Alert generation.
        # - yundun_soar_incident_update: Incident update.
        # 
        # This parameter is required.
        self.event_id = event_id
        # The language type for requesting and receiving messages. Values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The node name of the playbook.
        # 
        # This parameter is required.
        self.node_name = node_name
        # Template parameters for the message event.
        # - For incident generation: aliyunUID, incidentName, incidentID, startTime
        # - For alert generation: aliyunUID, alertName, alertID, startTime
        # - For incident update: aliyunUID, incidentName, incidentID, startTime, endTime, status, level
        self.params = params
        # The UUID of the playbook.
        # > You can obtain this parameter by calling the [DescribePlaybooks](~~DescribePlaybooks~~) interface.
        # 
        # This parameter is required.
        self.playbook_uuid = playbook_uuid
        # The user ID when an administrator switches to another member\\"s perspective.
        self.role_for = role_for
        # View type. Values:
        # - 0 (default): Current Alibaba Cloud account view.
        # - 1: View for all accounts under the enterprise.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_name is not None:
            result['ActionName'] = self.action_name

        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid

        if self.asset_id is not None:
            result['AssetId'] = self.asset_id

        if self.channel_type_list is not None:
            result['ChannelTypeList'] = self.channel_type_list

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.params is not None:
            result['Params'] = self.params

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')

        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')

        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')

        if m.get('ChannelTypeList') is not None:
            self.channel_type_list = m.get('ChannelTypeList')

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

