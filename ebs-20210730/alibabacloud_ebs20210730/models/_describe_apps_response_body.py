# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class DescribeAppsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        app_infos: List[main_models.DescribeAppsResponseBodyAppInfos] = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        user_code: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.app_infos = app_infos
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.user_code = user_code

    def validate(self):
        if self.app_infos:
            for v1 in self.app_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['AppInfos'] = []
        if self.app_infos is not None:
            for k1 in self.app_infos:
                result['AppInfos'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.user_code is not None:
            result['UserCode'] = self.user_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.app_infos = []
        if m.get('AppInfos') is not None:
            for k1 in m.get('AppInfos'):
                temp_model = main_models.DescribeAppsResponseBodyAppInfos()
                self.app_infos.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('UserCode') is not None:
            self.user_code = m.get('UserCode')

        return self

class DescribeAppsResponseBodyAppInfos(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_tags: List[main_models.DescribeAppsResponseBodyAppInfosAppTags] = None,
        default: bool = None,
        description: str = None,
        event_bridge_send_enabled: bool = None,
        modify_time: int = None,
        monitor_send_enabled: bool = None,
        report_send_enabled: bool = None,
        sls_send_enabled: bool = None,
        subscribe_period: str = None,
        subscribe_status: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.app_tags = app_tags
        self.default = default
        self.description = description
        self.event_bridge_send_enabled = event_bridge_send_enabled
        self.modify_time = modify_time
        self.monitor_send_enabled = monitor_send_enabled
        self.report_send_enabled = report_send_enabled
        self.sls_send_enabled = sls_send_enabled
        self.subscribe_period = subscribe_period
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

        if self.default is not None:
            result['Default'] = self.default

        if self.description is not None:
            result['Description'] = self.description

        if self.event_bridge_send_enabled is not None:
            result['EventBridgeSendEnabled'] = self.event_bridge_send_enabled

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.monitor_send_enabled is not None:
            result['MonitorSendEnabled'] = self.monitor_send_enabled

        if self.report_send_enabled is not None:
            result['ReportSendEnabled'] = self.report_send_enabled

        if self.sls_send_enabled is not None:
            result['SlsSendEnabled'] = self.sls_send_enabled

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
                temp_model = main_models.DescribeAppsResponseBodyAppInfosAppTags()
                self.app_tags.append(temp_model.from_map(k1))

        if m.get('Default') is not None:
            self.default = m.get('Default')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EventBridgeSendEnabled') is not None:
            self.event_bridge_send_enabled = m.get('EventBridgeSendEnabled')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('MonitorSendEnabled') is not None:
            self.monitor_send_enabled = m.get('MonitorSendEnabled')

        if m.get('ReportSendEnabled') is not None:
            self.report_send_enabled = m.get('ReportSendEnabled')

        if m.get('SlsSendEnabled') is not None:
            self.sls_send_enabled = m.get('SlsSendEnabled')

        if m.get('SubscribePeriod') is not None:
            self.subscribe_period = m.get('SubscribePeriod')

        if m.get('SubscribeStatus') is not None:
            self.subscribe_status = m.get('SubscribeStatus')

        return self

class DescribeAppsResponseBodyAppInfosAppTags(DaraModel):
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

