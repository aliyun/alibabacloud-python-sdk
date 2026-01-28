# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class ModifyAppRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_tags: List[main_models.ModifyAppRequestAppTags] = None,
        client_token: str = None,
        description: str = None,
        owner: str = None,
        region_id: str = None,
        report_send_enabled: bool = None,
        subscribe_period: str = None,
        subscribe_status: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        # This parameter is required.
        self.app_tags = app_tags
        self.client_token = client_token
        self.description = description
        self.owner = owner
        self.region_id = region_id
        self.report_send_enabled = report_send_enabled
        # This parameter is required.
        self.subscribe_period = subscribe_period
        # This parameter is required.
        self.subscribe_status = subscribe_status

    def validate(self):
        if self.app_tags:
            for v1 in self.app_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        result['AppTags'] = []
        if self.app_tags is not None:
            for k1 in self.app_tags:
                result['AppTags'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.report_send_enabled is not None:
            result['ReportSendEnabled'] = self.report_send_enabled

        if self.subscribe_period is not None:
            result['SubscribePeriod'] = self.subscribe_period

        if self.subscribe_status is not None:
            result['SubscribeStatus'] = self.subscribe_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        self.app_tags = []
        if m.get('AppTags') is not None:
            for k1 in m.get('AppTags'):
                temp_model = main_models.ModifyAppRequestAppTags()
                self.app_tags.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReportSendEnabled') is not None:
            self.report_send_enabled = m.get('ReportSendEnabled')

        if m.get('SubscribePeriod') is not None:
            self.subscribe_period = m.get('SubscribePeriod')

        if m.get('SubscribeStatus') is not None:
            self.subscribe_status = m.get('SubscribeStatus')

        return self

class ModifyAppRequestAppTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

