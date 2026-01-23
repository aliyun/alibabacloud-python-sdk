# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetQualityAlertOfAllRuleScopeByWatchIdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        quality_alert_info: main_models.GetQualityAlertOfAllRuleScopeByWatchIdResponseBodyQualityAlertInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.quality_alert_info = quality_alert_info
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.quality_alert_info:
            self.quality_alert_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.quality_alert_info is not None:
            result['QualityAlertInfo'] = self.quality_alert_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('QualityAlertInfo') is not None:
            temp_model = main_models.GetQualityAlertOfAllRuleScopeByWatchIdResponseBodyQualityAlertInfo()
            self.quality_alert_info = temp_model.from_map(m.get('QualityAlertInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetQualityAlertOfAllRuleScopeByWatchIdResponseBodyQualityAlertInfo(DaraModel):
    def __init__(
        self,
        alert_duty_channel_list: List[str] = None,
        alert_duty_list: List[main_models.GetQualityAlertOfAllRuleScopeByWatchIdResponseBodyQualityAlertInfoAlertDutyList] = None,
        alert_quality_owner_channel_list: List[str] = None,
        alert_user_channel_list: List[str] = None,
        alert_user_list: List[main_models.GetQualityAlertOfAllRuleScopeByWatchIdResponseBodyQualityAlertInfoAlertUserList] = None,
        enable_alert_quality_owner: bool = None,
        watch_id: int = None,
    ):
        self.alert_duty_channel_list = alert_duty_channel_list
        self.alert_duty_list = alert_duty_list
        self.alert_quality_owner_channel_list = alert_quality_owner_channel_list
        self.alert_user_channel_list = alert_user_channel_list
        self.alert_user_list = alert_user_list
        self.enable_alert_quality_owner = enable_alert_quality_owner
        self.watch_id = watch_id

    def validate(self):
        if self.alert_duty_list:
            for v1 in self.alert_duty_list:
                 if v1:
                    v1.validate()
        if self.alert_user_list:
            for v1 in self.alert_user_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_duty_channel_list is not None:
            result['AlertDutyChannelList'] = self.alert_duty_channel_list

        result['AlertDutyList'] = []
        if self.alert_duty_list is not None:
            for k1 in self.alert_duty_list:
                result['AlertDutyList'].append(k1.to_map() if k1 else None)

        if self.alert_quality_owner_channel_list is not None:
            result['AlertQualityOwnerChannelList'] = self.alert_quality_owner_channel_list

        if self.alert_user_channel_list is not None:
            result['AlertUserChannelList'] = self.alert_user_channel_list

        result['AlertUserList'] = []
        if self.alert_user_list is not None:
            for k1 in self.alert_user_list:
                result['AlertUserList'].append(k1.to_map() if k1 else None)

        if self.enable_alert_quality_owner is not None:
            result['EnableAlertQualityOwner'] = self.enable_alert_quality_owner

        if self.watch_id is not None:
            result['WatchId'] = self.watch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertDutyChannelList') is not None:
            self.alert_duty_channel_list = m.get('AlertDutyChannelList')

        self.alert_duty_list = []
        if m.get('AlertDutyList') is not None:
            for k1 in m.get('AlertDutyList'):
                temp_model = main_models.GetQualityAlertOfAllRuleScopeByWatchIdResponseBodyQualityAlertInfoAlertDutyList()
                self.alert_duty_list.append(temp_model.from_map(k1))

        if m.get('AlertQualityOwnerChannelList') is not None:
            self.alert_quality_owner_channel_list = m.get('AlertQualityOwnerChannelList')

        if m.get('AlertUserChannelList') is not None:
            self.alert_user_channel_list = m.get('AlertUserChannelList')

        self.alert_user_list = []
        if m.get('AlertUserList') is not None:
            for k1 in m.get('AlertUserList'):
                temp_model = main_models.GetQualityAlertOfAllRuleScopeByWatchIdResponseBodyQualityAlertInfoAlertUserList()
                self.alert_user_list.append(temp_model.from_map(k1))

        if m.get('EnableAlertQualityOwner') is not None:
            self.enable_alert_quality_owner = m.get('EnableAlertQualityOwner')

        if m.get('WatchId') is not None:
            self.watch_id = m.get('WatchId')

        return self

class GetQualityAlertOfAllRuleScopeByWatchIdResponseBodyQualityAlertInfoAlertUserList(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetQualityAlertOfAllRuleScopeByWatchIdResponseBodyQualityAlertInfoAlertDutyList(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

